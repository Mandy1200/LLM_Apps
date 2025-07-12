# Requirements to install first

# ollama
# chromadb
# pdfplumber 
# langchain
# langchain-core
# langchain-ollama
# langchain-community
# langchain_text_splitters
# unstructured
# unstructured[all-docs]
# fastembed
# pikepdf
# sentence-transformers
# elevenlabs



import streamlit as st
import os
import shutil
import logging
import pdfplumber
from langchain.schema import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_ollama import OllamaEmbeddings
from langchain.prompts import ChatPromptTemplate, PromptTemplate
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain.retrievers.multi_query import MultiQueryRetriever
import ollama

# ------------------------ Configuration ------------------------ #
logging.basicConfig(level=logging.INFO)
DOC_PATH = "./data/BOI.pdf"  # You can make this dynamic for uploads
MODEL_NAME = "llama3.2"
EMBEDDING_MODEL = "nomic-embed-text"
VECTOR_STORE_NAME = "simple-rag"
PERSIST_DIRECTORY = "./chroma_db"
# --------------------------------------------------------------- #


def ingest_pdf(doc_path):
    """Load PDF documents using pdfplumber and return LangChain Document list."""
    if not os.path.exists(doc_path):
        logging.error(f"PDF file not found at path: {doc_path}")
        st.error("PDF file not found.")
        return None

    texts = []
    try:
        with pdfplumber.open(doc_path) as pdf:
            for page in pdf.pages:
                text = page.extract_text()
                if text:
                    texts.append(text)
        logging.info("PDF loaded successfully with pdfplumber.")
    except Exception as e:
        logging.error(f"Error reading PDF: {e}")
        st.error(f"Error reading PDF: {e}")
        return None

    documents = [Document(page_content=txt) for txt in texts]
    return documents


def split_documents(documents):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1200, chunk_overlap=300)
    chunks = text_splitter.split_documents(documents)
    logging.info("Documents split into chunks.")
    return chunks


@st.cache_resource
def load_vector_db():
    ollama.pull(EMBEDDING_MODEL)
    embedding = OllamaEmbeddings(model=EMBEDDING_MODEL)

    # Use a persistent directory
    if os.path.exists(PERSIST_DIRECTORY) and os.path.isdir(PERSIST_DIRECTORY):
        vector_db = Chroma(
            embedding_function=embedding,
            collection_name=VECTOR_STORE_NAME,
            persist_directory=PERSIST_DIRECTORY,
        )
        logging.info("Loaded existing vector database.")
    else:
        os.makedirs(PERSIST_DIRECTORY, exist_ok=True)

        data = ingest_pdf(DOC_PATH)
        if data is None:
            return None

        chunks = split_documents(data)

        vector_db = Chroma.from_documents(
            documents=chunks,
            embedding=embedding,
            collection_name=VECTOR_STORE_NAME,
            persist_directory=PERSIST_DIRECTORY,
        )
        vector_db.persist()
        logging.info("Vector database created and persisted.")
    return vector_db


def create_retriever(vector_db, llm):
    QUERY_PROMPT = PromptTemplate(
        input_variables=["question"],
        template="""You are an AI language model assistant. Your task is to generate five
different versions of the given user question to retrieve relevant documents from
a vector database. By generating multiple perspectives on the user question, your
goal is to help the user overcome some of the limitations of the distance-based
similarity search. Provide these alternative questions separated by newlines.
Original question: {question}""",
    )

    retriever = MultiQueryRetriever.from_llm(
        vector_db.as_retriever(), llm, prompt=QUERY_PROMPT
    )
    logging.info("Retriever created.")
    return retriever


def create_chain(retriever, llm):
    template = """Answer the question based ONLY on the following context:
{context}
Question: {question}
"""

    prompt = ChatPromptTemplate.from_template(template)

    chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )

    logging.info("Chain created with preserved syntax.")
    return chain


def main():
    st.set_page_config(page_title="RAG PDF Assistant", layout="wide", page_icon="📄")
    st.title("📄 RAG PDF Assistant")

    user_input = st.text_input("🔍 Ask something about the document:")

    if user_input:
        with st.spinner("Generating answer..."):
            try:
                llm = ChatOllama(model=MODEL_NAME)
                vector_db = load_vector_db()

                if vector_db is None:
                    st.error("❌ Failed to load or create the vector database.")
                    return

                retriever = create_retriever(vector_db, llm)
                chain = create_chain(retriever, llm)

                response = chain.invoke(input=user_input)

                st.markdown("### 💬 Answer:")
                st.write(response)

                # Optional: download answer
                st.download_button("⬇️ Download Response", response, file_name="response.txt")

            except Exception as e:
                st.error(f"⚠️ An error occurred: {str(e)}")
    else:
        st.info("Enter a question to begin...")


if __name__ == "__main__":
    main()
