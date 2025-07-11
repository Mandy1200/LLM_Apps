import ollama
import os

model = "llama3.2"

in_file = "./TheChaosDataset/chaosData.txt"
out_file = "struc.txt"

if not os.path.exists(in_file):
    print(f"Input File '{in_file}' not found!")
    exit(1)

with open(in_file, "r") as f:
    items = f.read().strip()

prompt = f"""
You are an assistant that categorizes and sorts Chaos Dataset

Here is the list of datasets:
{items}

please:

1.Classify tasks using multi-label tagging, allowing each item to belong to multiple relevant categories such as Tech, Legal, Product, and Compliance, while displaying confidence scores or visual badges for clarity.

2.Extract structured action items by identifying the task, responsible owner, inferred or explicit deadlines, and contextual tags (e.g., project, region, sprint) for each entry.

3.Prioritize based on temporal cues and urgency, automatically tagging items as "urgent", "due soon", or "defer", and organizing them into a chronological framework like "Today", "This Week", or "Overdue".

4.Generate high-level summaries with analytics, including counts per category, trend detection (e.g. increase in infra issues), and clustering related tasks (e.g., all GDPR-related items grouped together).

5.Track task status dynamically, converting entries into togglable states like Todo, In Progress, Done, and Blocked, while also mapping out dependencies between tasks (e.g., "Awaiting approval before hiring").

6.Convert tasks into a JSON structure suitable for project management board views (like Trello or Notion-style Kanban), enabling real-time visualization of task flows and bottlenecks.

7.Use numbered sections, color-coded tags, and emojis/icons to enhance readability and user interaction, especially when grouping by department, urgency, or timeline.

8.Infer cross-functional dependencies, such as identifying how a delayed budget report can block hiring or product decisions, and flag these as interconnected tasks needing simultaneous resolution.

9.Support AI-powered querying, allowing users to ask natural questions like “What legal issues are still pending?” or “Which tasks block the UK beta launch?” with intelligent, filtered outputs.

10.Adaptively learn team behavior patterns, such as frequently missed deadlines or common task reassignees, and provide subtle nudges or summaries to optimize productivity workflows.

11. also try to The app intelligently classifies multi-domain tasks with confidence-based labels, extracts structured actionables with responsible owners and deadlines, prioritizes using urgency and time cues, 
generates analytic summaries and dependency-aware insights, tracks dynamic status across Kanban-ready JSON formats, visually enhances readability with styled tags and icons, and enables natural language querying 
while adaptively learning workflow patterns to optimize productivity.
"""

try:
    res = ollama.generate(model=model, prompt=prompt)

    print("DEBUG: Full response object from Ollama:")
    print(res)

    gen_txt = res.get("response", "")  # Try 'output', 'text', or 'message' if 'response' doesn't exist

    if not gen_txt.strip():
        print(" No text was generated. Check response format or model output.")
    else:
        print("Generated Text:")
        print(gen_txt)

        with open(out_file, "w") as f:
            f.write(gen_txt.strip())

        print(f" Categorized Dataset saved to: {out_file}")

except Exception as e:
    print(" An Error Occurred:", str(e))
