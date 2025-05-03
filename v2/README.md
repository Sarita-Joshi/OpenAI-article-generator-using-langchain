# V1 – Agentic Article Generator (LangChain)

This version uses LangChain to build a modular, agent-based article generation system.

It takes a topic and builds an article through sequential steps like researching, outlining, writing, and summarizing — optionally using tools like Wikipedia, web search, or retrieval-augmented generation (RAG).

---

## 🛠️ Architecture Overview

User Prompt
↓
[Research Agent] (Wikipedia, Search, RAG)
↓
[Outline Agent] (based on topic/tone/purpose)
↓
[Writer Agent] (writes full article)
↓
[Summary Agent] (optional abstract/overview)

yaml
Always show details

Copy

Each agent runs independently and passes structured outputs to the next.

---


## 🔍 Key Features

- Modular agents: research, outline, writer, summary
- Optional tool usage: Wikipedia, Tavily, RAG over uploaded files
- Built-in LLM adapter to support GPT-3.5, GPT-4, Claude (if configured)
- Flag-based configuration: auto-research, auto-outline, summary toggle
- Clean prompts and parameterized agent behaviors

---


## ⚙️ Tools Used

| Tool        | Purpose                        |
|-------------|--------------------------------|
| Wikipedia   | Lightweight, cached lookup     |
| Web Search  | Fetch current facts or trends  |
| RAG (FAISS) | Retrieve from uploaded docs    |
| LangChain   | Tool abstraction, agent logic  |

---


## 🔧 Usage (From Root)

```bash
streamlit run app.py
Select "V1: Agentic Flow" in the interface. Fill in the form and toggle options like:

Use Web Search

Auto-generate Outline

Include Summary

📁 File Structure (v1/)
Always show details

Copy
v1/
├── agents/
│   ├── research_agent.py
│   ├── outline_agent.py
│   ├── writer_agent.py
│   └── summary_agent.py
│
├── tools/
│   ├── wikipedia_tool.py
│   ├── rag_tool.py
│   └── tool_wrappers.py
│
├── chains/
│   └── rag_chain.py
│
├── prompts/
│   └── *.txt (structured templates)
│
└── llm/
    └── adapter.py
🔭 What’s Missing (by design)
No internal retry logic (yet)

Sequential, not parallel or DAG-based

No feedback loops / validation agents

Those are introduced in V2.

📄 License
MIT