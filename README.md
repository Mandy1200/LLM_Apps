<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
</head>
<body>

  <h1>🧠 Chaos Dataset Structuring Assistant</h1>
  <p>This project uses <strong>LLaMA 3.2</strong> (via Ollama) to convert messy task lists (the "Chaos Dataset") into structured, categorized, and prioritized outputs ready for project management tools like Trello or Notion.</p>

  <h2>🚀 Features</h2>
  <ul>
    <li><strong>Multi-Label Classification</strong> — Tags each task (e.g., Tech, Legal, Product) with confidence scores.</li>
    <li><strong>Structured Action Items</strong> — Extracts:
      <ul>
        <li>Task Description</li>
        <li>Responsible Owner</li>
        <li>Deadlines (explicit or inferred)</li>
        <li>Tags (e.g., region, sprint, priority)</li>
      </ul>
    </li>
    <li><strong>Urgency Detection</strong> — Labels tasks as <code>Urgent</code>, <code>Due Soon</code>, or <code>Deferred</code>.</li>
    <li><strong>Kanban-Ready JSON Export</strong> — Outputs task objects in a format suitable for visual task boards.</li>
    <li><strong>Analytics Summary</strong> — Counts per category, trend detection (e.g., infra spikes), and clusters like GDPR tasks.</li>
    <li><strong>Dependency Mapping</strong> — Highlights blocked tasks or prerequisites.</li>
    <li><strong>Natural Language Query Support</strong> — Ask things like:<br>
      <em>“What legal tasks are still open?”<br>
      “Which items block the UK beta launch?”</em>
    </li>
  </ul>

  <h2>🧰 Tech Stack</h2>
  <ul>
    <li><strong>Python 3.10+</strong></li>
    <li><a href="https://ollama.com/" target="_blank">Ollama</a> — Local LLM runtime</li>
    <li><strong>LLaMA 3.2</strong> — Open-source language model</li>
    <li><strong>Filesystem I/O</strong> — Task input and output via .txt files</li>
  </ul>

  <h2>📂 File Structure</h2>
  <pre>
TheChaosDataset/
├── chaosData.txt      # Raw unstructured task list
├── struc.txt          # structured data
  </pre>

  <h2>⚙️ How to Run</h2>
  <ol>
    <li>Place your raw task list in <code>./TheChaosDataset/chaosData.txt</code></li>
    <li>Run the script:
      <pre>python main.py</pre>
    </li>
    <li>Output will be saved to  <code>struc.txt</code></li>
  </ol>

  <h2>✅ Output Sample</h2>
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

  <h2>💡 Use Cases</h2>
  <ul>
    <li>Product sprint planning</li>
    <li>Legal + Compliance reviews</li>
    <li>Cross-functional team syncs</li>
    <li>Project retros & dashboards</li>
  </ul>

  <h2>📌 Notes</h2>
  <ul>
    <li>Works entirely offline using Ollama</li>
    <li>Can be extended for Slack, Trello, Notion, or API integrations</li>
  </ul>

  <h2>📬 Feedback / Contributions</h2>
  <p>Open an issue or fork the repo to improve task categorization logic, visualization support, or integrations!</p>

</body>
</html>
