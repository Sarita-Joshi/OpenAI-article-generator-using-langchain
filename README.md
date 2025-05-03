# 🧠 LLM Article Generator Hub

> A modular, multi-agent, multi-LLM system to explore and benchmark different architectures for AI-powered article generation — from simple prompt pipelines to deep LangGraph reasoning workflows.


## 📚 Table of Contents

- [🧩 Project Motivation](#-project-motivation)
- [🧠 System Capabilities](#-system-capabilities)
- [🔄 Evolution of the Architecture](#-evolution-of-the-architecture)
- [🔧 Achievements So Far](#-achievements-so-far)
- [🧪 Benchmark Goals](#-benchmark-goals)
- [🚀 Current Implementations](#-current-implementations)
- [⚖️ Comparison of Approaches](#-comparison-of-approaches)
- [📦 Directory Structure](#-directory-structure)
- [📌 Getting Started](#-getting-started)
- [🛤️ Roadmap & Next Phases](#-roadmap--next-phases)
- [📜 License](#-license)


## 🧩 Project Motivation

This project started as a simple OpenAI-based prompt wrapper for generating blog-style articles. As I explored more real-world use cases and enterprise LLM patterns, the system evolved into a **research platform** to test and compare:

- Prompt-only vs Tool-using vs Multi-agent designs  
- One-shot text vs modular section-based writing  
- Static generation vs interactive reasoning graphs  
- Single-model dependence vs LLM portability  

This repo now acts as a sandbox for testing different approaches to LLM-driven generation systems — not just for the final output, but also for how we structure and scale the process itself.

The goal is not just to generate content — but to **analyze and benchmark reliability, explainability, scalability, and extensibility** using a simple usecase!



## 🧠 System Capabilities

This hub currently supports:

✅ **Multi-Agent Design**  
- Research agents (Web, Academic, RAG, Validator)  
- Writer agents (Outline, Section Writer, Editor)  
- Quality agents (Fact Checker, Plagiarism, SEO)  
- Controller & Planner models in graph mode

✅ **Multi-Model Support (LLM Factory)**  
- OpenAI (GPT-3.5, GPT-4, GPT-4o)  
- Anthropic (Claude 3 family)  
- Cohere, Gemini (planned)  
- Adapter-based config system with shared prompt schema

✅ **Multi-Tool Retrieval**  
- Wikipedia (cached)  
- Tavily, Serper, Exa, PubMed, Arxiv  
- Local file RAG with chunked vector storage (FAISS)

✅ **Execution Modes**  
- **Quick mode (V1):** Chain-of-agents with optional RAG  
- **Deep mode (V2):** LangGraph-based reasoning and retry DAG

✅ **Streamlit UI with Mode Switcher**  
- Form-based UI that adapts between modes  
- Optional flags (summary, outline, research toggle)  
- Customizable LLM behavior: temperature, model, etc.



## 🔄 Evolution of the Architecture

| Stage | Description | Status |
|-------|-------------|--------|
| ✅ Stage 1 | Prompt wrapper with OpenAI | Completed |
| ✅ Stage 2 | LangChain agent tools (Wikipedia, RAG, etc.) | Completed |
| ✅ Stage 3 | Multi-agent flow with LangGraph | Completed |
| 🔜 Stage 4 | Graph-based planner (Minigraph-style) | Planned |
| 🔮 Stage 5 | Multimodal + voice-based interaction | In Research |



## 🔧 Achievements So Far

- Built a working **multi-agent research → writer → editor** system with optional summary
- Added **MultiPrompt + RAG** pipelines using LangChain tools
- Developed a **LangGraph DAG** with built-in retries, QA gates, and modular agent nodes
- Created a **LLM Adapter Factory** for model switching at runtime
- Designed a **versioned architecture**: `v1/`, `v2/` with flexible UI routing
- Implemented simple caching, structured prompts, vector search fallback
- Developed `pytest`-based testing suite for modular nodes
- Ready to scale with Minigraph, external APIs, Notion/Slack exports



## 🧪 Benchmark Goals

Not a benchmarking tool (yet), but this project can evolve to help measure:

| Aspect            | Intention                     |
|-------------------|-------------------------------|
| Repeatability     | How consistent is generation? |
| Cost efficiency   | Token usage across workflows  |
| Output quality    | Clarity, tone, factuality     |
| Tool effectiveness| When RAG or search helps most |
| Model flexibility | LLM portability in real flows |




## 🚀 Current Implementations

### ✅ [V1 — Lightweight Agentic System](v1/README.md)

- Tools: Wikipedia, RAG, WebSearch  
- Agents: Research, Outline, Writer, Summary  
- Control: Sequential routing (if/else logic)  
- LLM: OpenAI GPT-3.5 / GPT-4  

### ✅ [V2 — LangGraph Multi-Agent Pipeline](v2/README.md)

- Pods: Research → Writing → Quality  
- Tools: + Validators (Fact, SEO, Plagiarism)  
- Architecture: StateGraph with retries + node state  
- LLM: OpenAI, Claude, etc. via Adapter Factory



## ⚖️ Comparison of Approaches

| Feature              | V1: RouterChain Agents | V2: LangGraph Pipeline |
|----------------------|------------------------|------------------------|
| Flow Control         | Sequential             | Graph DAG              |
| Modularity           | Medium                 | High                   |
| Tools                | RAG, WebSearch, Wiki   | All V1 + QA pods       |
| Revisions / Retry    | Manual                 | Built-in via edges     |
| LLM Portability      | OpenAI only            | Multi-provider Adapter |
| Token Budgeting      | None                   | Per-agent budgeting    |
| Best For             | Fast blogs             | Long-form, formal docs |
| Planning Layer       | None                   | Planned                |
| Multimodal Input     | N/A                    | In progress            |



## 📦 Directory Structure

```
.
├── app.py               # Unified Streamlit UI
├── generate.py          # Delegates to V1 / V2
├── requirements.txt
│
├── v1/                  # RouterChain agentic workflow
│   └── README.md
│
├── v2/                  # LangGraph-based agent system
│   └── README.md
```



## 📌 Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/yourname/llm-article-generator-hub.git
cd llm-article-generator-hub
```

### 2. Create Environment

```bash
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Keys

```
OPENAI_API_KEY=
TAVILY_API_KEY=
...
```



## 🛤️ Roadmap & Next Phases

| Feature                     | Status     |
|----------------------------|------------|
| ✅ Multi-agent workflow     | Done       |
| ✅ LLM Adapter pattern      | Done       |
| ✅ Tool integration (RAG)   | Done       |
| 🔄 Graph planning (Minigraph) | Upcoming   |
| 🧠 Auto section reasoning   | In progress|
| 🖼️ Multimodal/vision LLM    | Researching|
| 🔗 Notion + Slack export    | Planned    |
| 🛡️ Guardrails + EvalSuite   | Planned    |


## 🧭 Features to explore...

- ✅ Multi-agent workflow
- ✅ LLM Adapter pattern
- ✅ Tool integration (RAG)
- Section-wise RAG + adaptive search queries  
- Minigraph-based planning before generation  
- Quality control layers: fact-checking, plagiarism, tone analysis  
- Export support: PDF, Markdown, Notion  
- Community prompts and evaluation modes  
- LLM feedback + edit suggestions
- Guardrails + EvalSuite
- Multimodal/vision LLM 

## 📜 License

MIT License.  
Feel free to fork, extend, experiment, or collaborate!