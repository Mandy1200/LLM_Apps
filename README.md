<h1> Ollama locally Must Be Installed Required for This Project !</h1>

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
</head>
<body>

  <h1>📚 Combined Projects README</h1>

  <section>
    <h2>🧠 Project 1: Chaos Dataset Structuring Assistant</h2>
    <p>
      This project uses <strong>LLaMA 3.2</strong> (via local <a href="https://ollama.com/" target="_blank" rel="noopener noreferrer">Ollama</a> LLM) to convert messy, unstructured task lists (the "Chaos Dataset") into clean, structured, categorized, and prioritized action items ready for tools like Trello or Notion.
    </p>

   ### 🚀 Features

- Multi-label classification with confidence scores (Tech, Legal, Product, etc.)
- Structured extraction of tasks, owners, deadlines, and tags
- Urgency detection: `Urgent`, `Due Soon`, `Deferred`
- Kanban-ready JSON output for visual task boards
- Analytics: category counts, trend detection, clustering
- Dependency mapping for blocked/prerequisite tasks
- Natural language query interface

### 📚 Tech Stack & Dependencies

![Python 3.10+](https://img.shields.io/badge/Python-3.10+-blue)
![Ollama LLM](https://img.shields.io/badge/Ollama-local%20LLM-green)
![LLaMA 3.2](https://img.shields.io/badge/LLaMA-3.2-orange)
![Langchain](https://img.shields.io/badge/langchain-ecosystem-lightgrey)
![ChromaDB](https://img.shields.io/badge/chromadb-vectorstore-blueviolet)

### 📂 File Structure


    
TheChaosDataset/
├── chaosData.txt      # Raw unstructured task list
├── struc.txt          # Structured output
└── unchaosdata.txt    # Alternative output
    </pre>

    <details>
      <summary>⚙️ Setup & Installation</summary>
      <pre>
pip install ollama chromadb langchain langchain-core langchain-ollama langchain-community unstructured unstructured[all-docs] fastembed pikepdf sentence-transformers elevenlabs
      </pre>
      <p>Also, install <a href="https://ollama.com/docs/installation" target="_blank" rel="noopener noreferrer">Ollama locally</a> and set up LLaMA 3.2 model.</p>
    </details>

    <details>
      <summary>⚙️ How to Run</summary>
      <ol>
        <li>Place raw tasks in <code>./TheChaosDataset/chaosData.txt</code></li>
        <li>Run the script: <pre>python main.py</pre></li>
        <li>Output saved as <code>struc.txt</code> or <code>unchaosdata.txt</code></li>
      </ol>
    </details>

    <h3>✅ Sample Output</h3>
    <pre>
[
  {
    "task": "Fix logout bug on iOS 17",
    "owner": "Dev Team",
    "deadline": "Today",
    "tags": ["Tech", "iOS", "Bug Fix"]
  }
]
    </pre>

    <h3>💡 Use Cases</h3>
    <ul>
      <li>Product sprint planning</li>
      <li>Legal and compliance reviews</li>
      <li>Cross-team syncs</li>
      <li>Retrospectives and dashboards</li>
    </ul>

    <h3>📌 Notes</h3>
    <ul>
      <li>Fully offline with Ollama</li>
      <li>Extendable for Slack, Trello, Notion, or API integrations</li>
    </ul>
  </section>

  <hr />

  <section>
    <h2>📄 Project 2: RAG PDF Assistant (Streamlit App)</h2>
    <p>
      A <strong>Streamlit-based</strong> document assistant using <strong>LLaMA 3.2</strong> and Ollama embeddings to build a Retrieval-Augmented Generation (RAG) system for PDFs.<br />
      Extract text, embed, and query PDF documents interactively.
    </p>

    <h3>🚀 Features</h3>
    <ul>
      <li>PDF ingestion & text extraction with <code>pdfplumber</code></li>
      <li>Text chunking for efficient retrieval</li>
      <li>Embeddings with Ollama's <code>nomic-embed-text</code> model</li>
      <li>Persistent vector DB using Chroma</li>
      <li>Multi-query retriever for enhanced search</li>
      <li>Streamlit UI for chat and downloadable answers</li>
    </ul>

    <h3>🧰 Tech Stack & Dependencies</h3>
    <p>
      <img src="https://img.shields.io/badge/Python-3.10+-blue" alt="Python 3.10+" />
      <img src="https://img.shields.io/badge/Streamlit-UI-green" alt="Streamlit" />
      <img src="https://img.shields.io/badge/Ollama-local%20LLM-green" alt="Ollama LLM" />
      <img src="https://img.shields.io/badge/LLaMA-3.2-orange" alt="LLaMA 3.2" />
      <img src="https://img.shields.io/badge/langchain-ecosystem-lightgrey" alt="Langchain" />
      <img src="https://img.shields.io/badge/chromadb-vectorstore-blueviolet" alt="ChromaDB" />
      <img src="https://img.shields.io/badge/pdfplumber-pdf%20extraction-blue" alt="pdfplumber" />
    </p>

    <details>
      <summary>⚙️ Setup & Installation</summary>
      <pre>
pip install streamlit ollama chromadb pdfplumber langchain langchain-core langchain-ollama langchain-community langchain_text_splitters unstructured fastembed pikepdf sentence-transformers elevenlabs
      </pre>
      <p>Make sure Ollama is installed and running locally.</p>
    </details>

    <details>
      <summary>⚙️ How to Run</summary>
      <pre>streamlit run ragPdf.py</pre>
      <ul>
        <li>Upload or use the default PDF (<code>./data/BOI.pdf</code>)</li>
        <li>Ask questions in the input box</li>
        <li>View answers and download responses</li>
      </ul>
    </details>

    <h3>📌 Notes</h3>
    <ul>
      <li>Caching for vector DB to speed up reloads</li>
      <li>Error handling for PDF and queries</li>
      <li>Easily extendable UI and file uploads</li>
    </ul>
  </section>

  <hr />

  <section>
    <h2>⚙️ Common Requirements</h2>
    <p>Install these packages to run both projects:</p>
    <p>
      <img src="https://img.shields.io/badge/ollama-LLM-blueviolet" alt="ollama" />
      <img src="https://img.shields.io/badge/chromadb-vectorstore-blueviolet" alt="chromadb" />
      <img src="https://img.shields.io/badge/pdfplumber-pdf%20extraction-blue" alt="pdfplumber" />
      <img src="https://img.shields.io/badge/langchain-ecosystem-lightgrey" alt="langchain" />
      <img src="https://img.shields.io/badge/langchain--core-library-lightgrey" alt="langchain-core" />
      <img src="https://img.shields.io/badge/langchain--ollama-library-lightgrey" alt="langchain-ollama" />
      <img src="https://img.shields.io/badge/langchain--community-library-lightgrey" alt="langchain-community" />
      <img src="https://img.shields.io/badge/langchain_text_splitters-library-lightgrey" alt="langchain_text_splitters" />
      <img src="https://img.shields.io/badge/unstructured-library-lightgrey" alt="unstructured" />
      <img src="https://img.shields.io/badge/fastembed-library-lightgrey" alt="fastembed" />
      <img src="https://img.shields.io/badge/pikepdf-library-lightgrey" alt="pikepdf" />
      <img src="https://img.shields.io/badge/sentence--transformers-library-lightgrey" alt="sentence-transformers" />
      <img src="https://img.shields.io/badge/elevenlabs-library-lightgrey" alt="elevenlabs" />
      <img src="https://img.shields.io/badge/streamlit-library-green" alt="streamlit" />
    </p>
    <pre>
pip install ollama chromadb pdfplumber langchain langchain-core langchain-ollama langchain-community langchain_text_splitters unstructured fastembed pikepdf sentence-transformers elevenlabs streamlit
    </pre>
  </section>

  <hr />

  <section>
    <h2>📬 Feedback & Contributions</h2>
    <p>
      Contributions, bug reports, and feature requests are welcome! Open issues or pull requests to improve task parsing, retrieval accuracy, UI, or integrations.
    </p>
    <p><strong>Happy Coding & Structuring! 🚀✨</strong></p>
  </section>

</body>
</html>
