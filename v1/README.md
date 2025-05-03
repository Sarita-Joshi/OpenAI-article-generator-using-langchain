# V1 – Agentic Article Generator (LangChain)

This version uses LangChain to build a modular, agent-based article generation system.

It takes a topic and builds an article through sequential steps like researching, outlining, writing, and summarizing — optionally using tools like Wikipedia, web search, or retrieval-augmented generation (RAG).



## 🛠️ Architecture Overview

```
User Prompt
   ↓
[Research Agent] → Wikipedia / Web Search / RAG
   ↓
[Outline Agent] → Generates section structure
   ↓
[Writer Agent] → Generates full article
   ↓
[Summary Agent] → (optional) Adds abstract
```

Each agent runs independently and passes structured outputs to the next.



## 🔍 Key Features

- Modular agents: research, outline, writer, summary  
- Tool integration: Wikipedia (cached), web search, RAG from uploaded PDFs  
- LLM-agnostic adapter: OpenAI, Claude, and more (via config)  
- Configurable flow: auto-research, outline, summary toggle  
- Clean and reusable prompt structure



## ⚙️ Tools Used

| Tool        | Purpose                        |
|-------------|--------------------------------|
| Wikipedia   | Lightweight, cached lookup     |
| Web Search  | Fetch current facts or trends  |
| RAG (FAISS) | Retrieve from uploaded docs    |
| LangChain   | Tool abstraction, agent logic  |


## 🧠 Technical Concepts

### What is Agentic AI?

Agentic AI refers to the design of systems where **autonomous, LLM-driven agents** can reason, make decisions, and perform tasks by using tools, memory, or interacting with other agents. Each agent is typically assigned a specific role or objective, such as researching a topic, generating an outline, or writing a paragraph.



### What is an Agent?

In this system, an **agent** is a wrapper around an LLM (like GPT or Claude) that performs a specific task. Each agent:

- Has a **defined prompt** and input/output contract
- May have access to **tools** like search, Wikipedia, or vector stores
- May **observe** the current state and decide next actions (in advanced setups)



### Agent Communication

Agents in this system communicate via **structured outputs** — one agent's output becomes the input to the next. For example:

- `Research Agent → Outline Agent` passes extracted facts and insights
- `Outline Agent → Writer Agent` sends structured section headers
- `Writer Agent → Summary Agent` gives full content for summarization

This avoids direct message passing or memory sharing — keeping the flow simple and modular.



### Observations and Tool Usage

Some agents (like `Research Agent`) use tools to generate **observations**, such as:

- Wikipedia lookups
- Web search results
- Retrieval from uploaded PDFs

The agent incorporates these observations into its reasoning before producing output.



### Memory and State (V1)

In this version, **memory is stateless** — there is no history or context carried across runs. Each session is fresh. Future versions (e.g., V2) explore memory, retries, and graph-aware state sharing.



### LLM Abstraction

To make the system **model-agnostic**, an adapter pattern is used so agents can call:

- `OpenAI` (gpt-3.5 / gpt-4 / gpt-4o)
- `Claude` (via Anthropic)
- `Cohere`, `Groq`, and more (planned)

This allows testing different LLMs for the same task using the same agent logic.


## 🧪 Usage (From Root)

```bash
streamlit run app.py
```

1. Select **"V1: Agentic Flow"** in the UI.  
2. Enter topic, keywords, tone, etc.  
3. Choose your options:
   - Auto-research  
   - Auto-outline  
   - Include summary  
4. Select the LLM model and temperature  
5. Click **Generate Article**



## 📁 File Structure

```
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
```



## 🚫 What’s Missing (by design)

This version avoids complexity by design. It does **not** include:

- Retry or fallback logic  
- Dynamic graph execution  
- Multi-layer validation agents  
- Planning or routing between tools  

Those are introduced in [V2 → LangGraph System](../v2/README.md).



## 📄 License

MIT  
Built for experimentation and learning.
