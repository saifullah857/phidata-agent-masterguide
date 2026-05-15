<div align="center">

<!-- Animated Header Banner -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=200&section=header&text=Phidata%20AI%20Agents&fontSize=60&fontColor=fff&animation=twinkling&fontAlignY=35&desc=From%20Zero%20to%20Production-Ready%20AI%20Systems&descAlignY=60&descSize=18" width="100%"/>

<!-- Typing Animation -->
<div align="center">
  <a href="https://github.com/agentstack-ai/phidata-agent-masterguide">
    <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=22&pause=1000&color=6C63FF&center=true&vCenter=true&width=700&lines=%F0%9F%A4%96+Build+AI+Agents+from+Scratch;%F0%9F%A7%A0+Multi-Agent+Systems+%26+RAG;%F0%9F%9A%80+Deploy+to+Production+Fast;%F0%9F%9B%A0%EF%B8%8F+Tools+%2B+Memory+%2B+Knowledge+Bases;%E2%9A%A1+Powered+by+Phidata+Framework" alt="Typing SVG" />
  </a>
</div>
<br/>

<!-- Badges Row 1 -->
[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Phidata](https://img.shields.io/badge/Phidata-Framework-6C63FF?style=for-the-badge&logo=databricks&logoColor=white)](https://phidata.com)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o-412991?style=for-the-badge&logo=openai&logoColor=white)](https://openai.com)
[![License](https://img.shields.io/badge/License-MIT-22C55E?style=for-the-badge&logo=opensourceinitiative&logoColor=white)](LICENSE)

<!-- Badges Row 2 -->
[![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![Docker](https://img.shields.io/badge/Docker-Deployment-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://docker.com)
[![Streamlit](https://img.shields.io/badge/Streamlit-UI-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![Stars](https://img.shields.io/github/stars/agentstack-ai/phidata-agent-masterguide?style=for-the-badge&logo=github&color=F59E0B)](https://github.com)

<br/>

> **🎯 The most complete, beginner-to-advanced guide for building production-grade AI Agents with Phidata.**
> Perfect for developers who want to go from zero to shipping real AI-powered products.

</div>

---

## 📋 Table of Contents

<details>
<summary><b>Click to expand full table of contents</b></summary>

| # | Topic | Level |
|---|-------|-------|
| 1 | [Introduction to AI Agents](#1-introduction-to-ai-agents) | 🟢 Beginner |
| 2 | [What is Phidata?](#2-what-is-phidata) | 🟢 Beginner |
| 3 | [Why Use Phidata?](#3-why-use-phidata) | 🟢 Beginner |
| 4 | [Phidata Architecture](#4-phidata-architecture) | 🟢 Beginner |
| 5 | [Installation & Setup](#5-installation-and-environment-setup) | 🟢 Beginner |
| 6 | [Core Concepts](#6-understanding-core-concepts) | 🟢 Beginner |
| 7 | [Your First Agent](#7-your-first-agent) | 🟢 Beginner |
| 8 | [LLMs in Phidata](#8-understanding-llms-in-phidata) | 🟡 Intermediate |
| 9 | [Tools](#9-tools-in-phidata) | 🟡 Intermediate |
| 10 | [Memory Systems](#10-memory-systems) | 🟡 Intermediate |
| 11 | [Knowledge Bases](#11-knowledge-bases) | 🟡 Intermediate |
| 12 | [Multi-Agent Systems](#12-multi-agent-systems) | 🟡 Intermediate |
| 13 | [RAG](#13-rag-retrieval-augmented-generation) | 🟡 Intermediate |
| 14 | [Agent Teams](#14-agent-teams) | 🟡 Intermediate |
| 15 | [Web Search Agents](#15-web-search-agents) | 🟡 Intermediate |
| 16 | [File Processing Agents](#16-file-processing-agents) | 🟡 Intermediate |
| 17 | [Database Agents](#17-database-agents) | 🔴 Advanced |
| 18 | [Finance Agents](#18-finance-agents) | 🔴 Advanced |
| 19 | [AI Research Agents](#19-ai-research-agents) | 🔴 Advanced |
| 20 | [Autonomous Agents](#20-autonomous-agents) | 🔴 Advanced |
| 21 | [Voice Agents](#21-voice-agents) | 🔴 Advanced |
| 22 | [Vision Agents](#22-vision-agents) | 🔴 Advanced |
| 23 | [API Integration](#23-api-integration) | 🔴 Advanced |
| 24 | [Production Deployment](#24-production-deployment) | 🔴 Advanced |
| 25 | [Docker Setup](#25-docker-setup) | 🔴 Advanced |
| 26 | [FastAPI Integration](#26-fastapi-integration) | 🔴 Advanced |
| 27 | [Streamlit Integration](#27-streamlit-integration) | 🔴 Advanced |
| 28 | [Security Best Practices](#28-security-best-practices) | 🔴 Advanced |
| 29 | [Cost Optimization](#29-cost-optimization) | 🔴 Advanced |
| 30 | [Debugging & Monitoring](#30-debugging-and-monitoring) | 🔴 Advanced |
| 31 | [Real-World Projects](#31-real-world-projects) | 🏆 Expert |
| 32 | [Advanced Architectures](#32-advanced-architectures) | 🏆 Expert |
| 33 | [Best Practices](#33-best-practices) | 🏆 Expert |
| 34 | [Common Errors & Solutions](#34-common-errors-and-solutions) | 🏆 Expert |
| 35 | [Learning Roadmap](#35-complete-learning-roadmap) | 🏆 Expert |
| 36 | [Capstone Projects](#36-final-capstone-projects) | 🏆 Expert |

</details>

---

## 1. Introduction to AI Agents

<img align="right" width="350" src="https://www.phidata.com/images/ai-agent-diagram.png" alt="AI Agent Diagram" onerror="this.style.display='none'"/>

### 🤖 What is an AI Agent?

An AI Agent is an **intelligent software system** that goes far beyond a simple chatbot.

| Capability | Traditional AI | AI Agent |
|-----------|---------------|----------|
| Understands input | ✅ | ✅ |
| Uses external tools | ❌ | ✅ |
| Remembers context | ❌ | ✅ |
| Makes decisions | ❌ | ✅ |
| Executes actions | ❌ | ✅ |
| Plans autonomously | ❌ | ✅ |

```
Traditional AI:    question ──────────────────► answer

AI Agent:          question ──► reasoning ──► tools ──► memory ──► actions ──► answer
```

---

## 2. What is Phidata?

[![Phidata Docs](https://img.shields.io/badge/Docs-phidata.com-6C63FF?style=flat-square&logo=gitbook&logoColor=white)](https://docs.phidata.com)
[![GitHub](https://img.shields.io/badge/GitHub-phidatahq%2Fphidata-181717?style=flat-square&logo=github)](https://github.com/phidatahq/phidata)

**Phidata** is a powerful Python framework for building production-ready AI systems.

> 💡 Think of Phidata as the **"Django of AI Agents"** — it gives you all the building blocks, so you focus on logic, not boilerplate.

You can use it to build:

- 🤖 **AI Agents** — Single, purpose-built agents
- 🧑‍🤝‍🧑 **Multi-Agent Systems** — Teams of coordinated agents
- 📚 **RAG Applications** — Knowledge-grounded Q&A
- 🔁 **Autonomous AI Workflows** — Self-driven pipelines
- 🛠️ **Tool-Using Agents** — Agents that search, code, query DBs

---

## 3. Why Use Phidata?

<div align="center">

| Feature | Benefit |
|---------|---------|
| 🧩 **Simple Syntax** | Go from idea to agent in minutes |
| 🔌 **Tool Integration** | Web, files, databases, APIs — all built-in |
| 🧠 **Memory Support** | Agents remember across conversations |
| 👥 **Multi-Agent** | Multiple agents collaborate automatically |
| 🚀 **Production Ready** | Docker, FastAPI, monitoring — all supported |

</div>

---

## 4. Phidata Architecture

```
                        ┌─────────────────────────────────┐
                        │             USER                │
                        └──────────────┬──────────────────┘
                                       │
                        ┌──────────────▼──────────────────┐
                        │            AGENT                │
                        └──────────────┬──────────────────┘
                                       │
                        ┌──────────────▼──────────────────┐
                        │             LLM                 │
                        │    (GPT-4o / Claude / Gemini)   │
                        └──────────────┬──────────────────┘
                                       │
               ┌───────────────────────┼───────────────────────┐
               │                       │                       │
   ┌───────────▼───────┐   ┌───────────▼───────┐   ┌──────────▼────────┐
   │      TOOLS        │   │      MEMORY        │   │   KNOWLEDGE BASE  │
   │  (Web/DB/APIs)    │   │  (Conversation)    │   │   (PDFs/Docs)     │
   └───────────────────┘   └───────────────────┘   └───────────────────┘
                                       │
                        ┌──────────────▼──────────────────┐
                        │           RESPONSE              │
                        └─────────────────────────────────┘
```

---

## 5. Installation and Environment Setup

[![Python](https://img.shields.io/badge/Requires-Python%203.10%2B-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)

### Step 1 — Check Python Version

```bash
python --version
# Expected: Python 3.10+
```

### Step 2 — Create Virtual Environment

<details>
<summary><b>🪟 Windows</b></summary>

```bash
python -m venv venv
venv\Scripts\activate
```
</details>

<details>
<summary><b>🐧 Linux / 🍎 macOS</b></summary>

```bash
python3 -m venv venv
source venv/bin/activate
```
</details>

### Step 3 — Install Phidata & Dependencies

```bash
pip install phidata openai python-dotenv
```

> ⚡ Or with `uv` for faster installs:
> ```bash
> uv pip install phidata openai python-dotenv
> ```

### Step 4 — Setup API Keys

Create a `.env` file in your project root:

```env
# .env
OPENAI_API_KEY=sk-your-openai-key-here
GROQ_API_KEY=your-groq-key-here           # optional
ANTHROPIC_API_KEY=your-anthropic-key-here  # optional
```

> 🔐 **Never commit `.env` to Git.** Add it to `.gitignore` immediately.

### Step 5 — Verify Installation

```python
# test.py
from phi.agent import Agent
print("✅ Phidata installed successfully!")
```

```bash
python test.py
```

---

## 6. Understanding Core Concepts

```
┌─────────────────────────────────────────────────────────────────┐
│                        PHIDATA CONCEPTS                         │
├────────────────┬────────────────────────────────────────────────┤
│   CONCEPT      │   DESCRIPTION                                  │
├────────────────┼────────────────────────────────────────────────┤
│  🤖 Agent      │  The brain — orchestrates everything           │
│  🧠 Model      │  The LLM powering the agent (GPT-4o, etc.)    │
│  🔧 Tools      │  External capabilities (search, calc, DB)      │
│  💾 Memory     │  Stores conversation history                   │
│  📚 Knowledge  │  Custom information source (PDFs, docs)        │
└────────────────┴────────────────────────────────────────────────┘
```

---

## 7. Your First Agent

> 🎉 **Let's build your first AI agent in under 10 lines of code!**

```python
from phi.agent import Agent
from phi.model.openai import OpenAIChat

# Create the agent
agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    instructions=["Be helpful and concise."],
    markdown=True,
)

# Run it!
agent.print_response("Tell me about AI agents")
```

### How It Works

```
1. You send a message
       ↓
2. Agent receives it
       ↓
3. Agent forwards to LLM (GPT-4o)
       ↓
4. LLM generates a response
       ↓
5. Agent formats and displays it ✅
```

---

## 8. Understanding LLMs in Phidata

Phidata supports **all major LLM providers** out of the box:

<div align="center">

| Provider | Import | Model Example |
|----------|--------|---------------|
| ![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=flat-square&logo=openai&logoColor=white) | `from phi.model.openai import OpenAIChat` | `gpt-4o` |
| ![Groq](https://img.shields.io/badge/Groq-F55036?style=flat-square&logo=groq&logoColor=white) | `from phi.model.groq import Groq` | `llama3-70b-8192` |
| ![Anthropic](https://img.shields.io/badge/Anthropic-191919?style=flat-square&logo=anthropic&logoColor=white) | `from phi.model.anthropic import Claude` | `claude-3-5-sonnet` |
| ![Google](https://img.shields.io/badge/Google-4285F4?style=flat-square&logo=google&logoColor=white) | `from phi.model.google import Gemini` | `gemini-1.5-pro` |

</div>

```python
# OpenAI
from phi.model.openai import OpenAIChat
model = OpenAIChat(id="gpt-4o")

# Groq (fast & free tier)
from phi.model.groq import Groq
model = Groq(id="llama3-70b-8192")

# Anthropic Claude
from phi.model.anthropic import Claude
model = Claude(id="claude-3-5-sonnet")

# Google Gemini
from phi.model.google import Gemini
model = Gemini(id="gemini-1.5-pro")
```

---

## 9. Tools in Phidata

> 🦸 **Tools transform a chatbot into a superhero agent.**

```
Without Tools:  Agent can only talk. 💬
With Tools:     Agent can search, calculate, code, analyze, and act. ⚡
```

### 9.1 — Calculator Tool

```python
from phi.agent import Agent
from phi.tools.calculator import Calculator
from phi.model.openai import OpenAIChat

agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    tools=[Calculator()],
    show_tool_calls=True,  # Shows when a tool is used
)

agent.print_response("What is 2347 * 89 + 1234?")
```

### 9.2 — Web Search Agent

```bash
pip install duckduckgo-search
```

```python
from phi.agent import Agent
from phi.tools.duckduckgo import DuckDuckGo
from phi.model.openai import OpenAIChat

agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    tools=[DuckDuckGo()],
    show_tool_calls=True,
)

agent.print_response("What are the latest AI news today?")
```

### 9.3 — Python Code Executor

```python
from phi.agent import Agent
from phi.tools.python import PythonTools
from phi.model.openai import OpenAIChat

agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    tools=[PythonTools()],
    show_tool_calls=True,
)

agent.print_response("Plot a sine wave and save it as sine.png")
```

---

## 10. Memory Systems

> 🧠 **Without memory, every conversation starts from scratch. With memory, your agent truly learns.**

```python
from phi.agent import Agent
from phi.model.openai import OpenAIChat

agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    add_history_to_messages=True,  # 👈 This enables memory
)

agent.print_response("My name is Alex")
agent.print_response("What is my name?")  # Agent remembers: "Your name is Alex"
```

---

## 11. Knowledge Bases

> 📚 **Feed your agent custom documents, PDFs, and company data.**

```bash
pip install pypdf lancedb sentence-transformers
```

```python
from phi.knowledge.pdf import PDFKnowledgeBase
from phi.vectordb.lancedb import LanceDb
from phi.agent import Agent
from phi.model.openai import OpenAIChat

# Create knowledge base from PDF
knowledge_base = PDFKnowledgeBase(
    path="data/manual.pdf",
    vector_db=LanceDb(
        table_name="documents",
        uri="tmp/lancedb",
    ),
)
knowledge_base.load()

# Create agent with knowledge
agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    knowledge=knowledge_base,
    search_knowledge=True,  # 👈 Agent searches docs before answering
    markdown=True,
)

agent.print_response("Summarize the key points from the manual")
```

---

## 12. Multi-Agent Systems

> 👥 **Real power comes from agents working together as a team.**

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│  Research   │    │   Writer    │    │   Review    │
│   Agent     │───►│   Agent     │───►│   Agent     │
└─────────────┘    └─────────────┘    └─────────────┘
       │                  │                  │
       └──────────────────┼──────────────────┘
                          ▼
                   Final Polished Output
```

```python
from phi.agent import Agent
from phi.model.openai import OpenAIChat

research_agent = Agent(
    name="Research Agent",
    role="Researches topics in depth",
    model=OpenAIChat(id="gpt-4o"),
)

writer_agent = Agent(
    name="Writer Agent",
    role="Writes engaging, clear content",
    model=OpenAIChat(id="gpt-4o"),
)

# Team leader delegates to specialists
team = Agent(
    team=[research_agent, writer_agent],
    model=OpenAIChat(id="gpt-4o"),
    instructions=["Coordinate both agents", "Deliver comprehensive output"],
)

team.print_response("Write a detailed article about Quantum Computing")
```

---

## 13. RAG (Retrieval Augmented Generation)

> 📖 **RAG = Retrieve Information FIRST, then Generate a Response. Kills hallucinations.**

```
User Question
      │
      ▼
Search Vector Database
      │
      ▼
Retrieve Relevant Chunks
      │
      ▼
Inject into LLM Prompt
      │
      ▼
Generate Accurate, Grounded Response ✅
```

```python
from phi.agent import Agent
from phi.model.openai import OpenAIChat
from phi.knowledge.pdf import PDFKnowledgeBase
from phi.vectordb.lancedb import LanceDb

knowledge_base = PDFKnowledgeBase(
    path="documents/",           # Folder with multiple PDFs
    vector_db=LanceDb(
        table_name="pdf_docs",
        uri="tmp/lancedb",
    ),
)
knowledge_base.load(recreate=False)  # Don't re-embed on each run

agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    knowledge=knowledge_base,
    search_knowledge=True,
    markdown=True,
)

agent.print_response("Explain the main concepts from chapter 1")
```

---

## 14. Agent Teams

### 🚀 Startup Co-Founder Team Example

```python
from phi.agent import Agent
from phi.model.openai import OpenAIChat

researcher = Agent(
    name="Researcher",
    role="Finds market trends and competitor analysis",
    model=OpenAIChat(id="gpt-4o"),
)

developer = Agent(
    name="Developer",
    role="Creates technical architecture and MVP roadmap",
    model=OpenAIChat(id="gpt-4o"),
)

marketer = Agent(
    name="Marketer",
    role="Builds go-to-market strategy",
    model=OpenAIChat(id="gpt-4o"),
)

startup_team = Agent(
    team=[researcher, developer, marketer],
    model=OpenAIChat(id="gpt-4o"),
    instructions=["Think like a startup founder", "Be practical and actionable"],
)

startup_team.print_response("Create a complete AI fitness startup plan")
```

---

## 15. Web Search Agents

```python
from phi.agent import Agent
from phi.tools.duckduckgo import DuckDuckGo
from phi.model.openai import OpenAIChat

research_agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    tools=[DuckDuckGo()],
    instructions=[
        "Always cite your sources",
        "Search for the most recent information",
        "Summarize findings clearly",
    ],
    show_tool_calls=True,
    markdown=True,
)

research_agent.print_response("Latest AI agent frameworks in 2026")
```

---

## 16. File Processing Agents

```python
from phi.agent import Agent
from phi.tools.file import FileTools
from phi.model.openai import OpenAIChat

agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    tools=[FileTools()],
    show_tool_calls=True,
)

agent.print_response("Read the file report.txt and give me a 3-bullet summary")
```

---

## 17. Database Agents

```python
from phi.agent import Agent
from phi.tools.sql import SQLTools
from phi.model.openai import OpenAIChat

agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    tools=[
        SQLTools(db_url="sqlite:///students.db")
    ],
    show_tool_calls=True,
)

agent.print_response("Show me the top 5 students ranked by GPA")
```

---

## 18. Finance Agents

[![yfinance](https://img.shields.io/badge/Powered%20by-yfinance-22C55E?style=flat-square)](https://pypi.org/project/yfinance/)

```python
from phi.agent import Agent
from phi.tools.yfinance import YFinanceTools
from phi.model.openai import OpenAIChat

finance_agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    tools=[
        YFinanceTools(
            stock_price=True,
            analyst_recommendations=True,
            company_info=True,
        )
    ],
    instructions=["Present data in tables", "Always include risk warnings"],
    markdown=True,
)

finance_agent.print_response("Analyze Tesla (TSLA) stock — price, trends, and analyst views")
```

---

## 19. AI Research Agents

```python
from phi.agent import Agent
from phi.tools.duckduckgo import DuckDuckGo
from phi.model.openai import OpenAIChat

research_agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    tools=[DuckDuckGo()],
    instructions=[
        "Search multiple sources before answering",
        "Always provide citations with URLs",
        "Think step by step before concluding",
        "Summarize findings in clear sections",
    ],
    markdown=True,
)

research_agent.print_response("Deep research on quantum computing applications in 2026")
```

---

## 20. Autonomous Agents

> 🤖 **Autonomous agents plan, act, verify, and iterate — without being told each step.**

```python
from phi.agent import Agent
from phi.model.openai import OpenAIChat
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.python import PythonTools

agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    tools=[DuckDuckGo(), PythonTools()],
    instructions=[
        "Break complex problems into clear steps",
        "Think carefully before acting",
        "Verify your answers before presenting",
        "Use tools when you need real data",
    ],
    markdown=True,
)

agent.print_response("Create a complete 90-day AI startup roadmap with milestones")
```

---

## 21. Voice Agents

> 🎙️ **Voice flow:** Speech → Text → Agent → Text → Speech

```bash
pip install speechrecognition pyttsx3
```

```python
import speech_recognition as sr
import pyttsx3
from phi.agent import Agent
from phi.model.openai import OpenAIChat

agent = Agent(model=OpenAIChat(id="gpt-4o"))
recognizer = sr.Recognizer()
engine = pyttsx3.init()

with sr.Microphone() as source:
    print("🎙️ Listening... speak now!")
    audio = recognizer.listen(source)

text = recognizer.recognize_google(audio)
print(f"You said: {text}")

response = agent.run(text)

engine.say(response.content)
engine.runAndWait()
```

---

## 22. Vision Agents

> 👁️ **Let your agent see and understand images, charts, screenshots, and more.**

```python
from phi.agent import Agent
from phi.model.openai import OpenAIChat

vision_agent = Agent(
    model=OpenAIChat(id="gpt-4o"),    # GPT-4o has native vision
    markdown=True,
)

vision_agent.print_response(
    "Describe this image in detail and extract any text visible",
    images=["screenshot.jpg"],
)
```

---

## 23. API Integration

> 🔌 **Build custom tools that connect to any external API.**

```python
import requests
from phi.tools import Toolkit

class WeatherTools(Toolkit):
    def __init__(self):
        super().__init__(name="weather_tools")
        self.register(self.get_weather)

    def get_weather(self, city: str) -> str:
        """Fetch current weather for a city."""
        url = f"https://api.weatherapi.com/v1/current.json"
        params = {"key": "YOUR_API_KEY", "q": city}
        response = requests.get(url, params=params)
        data = response.json()
        return f"{city}: {data['current']['temp_c']}°C, {data['current']['condition']['text']}"
```

```python
from phi.agent import Agent
from phi.model.openai import OpenAIChat

agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    tools=[WeatherTools()],
)

agent.print_response("What's the weather in Lahore and Dubai?")
```

---

## 24. Production Deployment

```
┌─────────────────────┐
│      Frontend       │  ← Streamlit / React / Next.js
└──────────┬──────────┘
           │
┌──────────▼──────────┐
│   FastAPI Backend   │  ← REST API layer
└──────────┬──────────┘
           │
┌──────────▼──────────┐
│   Phidata Agents    │  ← Agent logic
└──────────┬──────────┘
           │
┌──────────▼──────────┐
│  Database + APIs    │  ← PostgreSQL, Redis, 3rd party APIs
└─────────────────────┘
```

---

## 25. Docker Setup

```dockerfile
# Dockerfile
FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source
COPY . .

# Run
CMD ["python", "main.py"]
```

```bash
# Build
docker build -t my-ai-agent .

# Run
docker run -p 8000:8000 --env-file .env my-ai-agent
```

---

## 26. FastAPI Integration

[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)

```bash
pip install fastapi uvicorn
```

```python
# main.py
from fastapi import FastAPI
from pydantic import BaseModel
from phi.agent import Agent
from phi.model.openai import OpenAIChat

app = FastAPI(title="AI Agent API", version="1.0.0")

agent = Agent(model=OpenAIChat(id="gpt-4o"))

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    response: str

@app.post("/chat", response_model=ChatResponse)
async def chat(data: ChatRequest):
    result = agent.run(data.message)
    return ChatResponse(response=result.content)

@app.get("/health")
async def health():
    return {"status": "healthy"}
```

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

> 📖 Docs auto-generated at: `http://localhost:8000/docs`

---

## 27. Streamlit Integration

[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)](https://streamlit.io)

```bash
pip install streamlit
```

```python
# app.py
import streamlit as st
from phi.agent import Agent
from phi.model.openai import OpenAIChat

st.set_page_config(page_title="🤖 AI Agent", page_icon="🤖")
st.title("🤖 Phidata AI Agent")
st.caption("Powered by GPT-4o and Phidata")

# Initialize agent (cached to avoid re-creating)
@st.cache_resource
def get_agent():
    return Agent(model=OpenAIChat(id="gpt-4o"), markdown=True)

agent = get_agent()

# Chat interface
if user_input := st.chat_input("Ask me anything..."):
    with st.chat_message("user"):
        st.write(user_input)
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = agent.run(user_input)
            st.write(response.content)
```

```bash
streamlit run app.py
```

---

## 28. Security Best Practices

> 🔐 **Security is non-negotiable in production.**

```python
# ❌ NEVER do this
OPENAI_API_KEY = "sk-abc123..."  # Exposed in code!

# ✅ Always do this
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
```

**Checklist:**

- [ ] API keys in `.env` file only
- [ ] `.env` added to `.gitignore`
- [ ] Use environment variables in Docker via `--env-file`
- [ ] Rate-limit your FastAPI endpoints
- [ ] Validate and sanitize all user input
- [ ] Never log API keys or secrets

---

## 29. Cost Optimization

> 💸 **Smart model selection can cut costs by 90%.**

| Task Type | Recommended Model | Cost |
|-----------|-----------------|------|
| Simple Q&A | `gpt-3.5-turbo` / `llama3-8b` | 💚 Very Low |
| Complex reasoning | `gpt-4o-mini` | 💛 Low |
| Critical analysis | `gpt-4o` | 🔴 Higher |

**Optimization Tips:**

- Use Groq (free tier) for development and testing
- Enable `add_history_to_messages=True` only when needed
- Use summarized memory instead of full history
- Keep prompts concise and specific

---

## 30. Debugging and Monitoring

```python
import logging
logging.basicConfig(level=logging.INFO)

agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    show_tool_calls=True,    # 👈 See every tool call
    debug_mode=True,         # 👈 Full debug output
    markdown=True,
)
```

**Debugging Flags:**

| Flag | Purpose |
|------|---------|
| `show_tool_calls=True` | Shows what tools the agent uses |
| `debug_mode=True` | Verbose logging |
| `markdown=True` | Pretty formatted output |

---

## 31. Real-World Projects

### 🖥️ Project 1: AI Coding Assistant

```python
from phi.agent import Agent
from phi.tools.python import PythonTools
from phi.model.openai import OpenAIChat

coding_agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    tools=[PythonTools()],
    instructions=[
        "Write clean, well-commented code",
        "Follow PEP 8 style guidelines",
        "Explain your code after writing it",
        "Always include error handling",
    ],
    markdown=True,
)

coding_agent.print_response("Build a REST API for a todo app using FastAPI")
```

---

### 🚀 Project 2: AI Startup Co-Founder

```python
from phi.agent import Agent
from phi.model.openai import OpenAIChat
from phi.tools.duckduckgo import DuckDuckGo

research_agent = Agent(
    name="Research Agent",
    role="Analyzes markets, competitors, and trends",
    model=OpenAIChat(id="gpt-4o"),
    tools=[DuckDuckGo()],
)

finance_agent = Agent(
    name="Finance Agent",
    role="Models revenue, costs, and financial projections",
    model=OpenAIChat(id="gpt-4o"),
)

developer_agent = Agent(
    name="Developer Agent",
    role="Creates technical architecture and MVP roadmap",
    model=OpenAIChat(id="gpt-4o"),
)

startup_agent = Agent(
    team=[research_agent, finance_agent, developer_agent],
    model=OpenAIChat(id="gpt-4o"),
    instructions=["Think like a Y Combinator-backed founder"],
    markdown=True,
)

startup_agent.print_response("Build an AI healthcare startup plan — market, product, finance")
```

---

### 🎧 Project 3: AI Customer Support Agent

```python
from phi.agent import Agent
from phi.model.openai import OpenAIChat

support_agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    instructions=[
        "Always be polite, empathetic, and professional",
        "Resolve issues in as few messages as possible",
        "If you cannot solve an issue, escalate clearly",
        "Never make promises about refunds without policy check",
    ],
    markdown=True,
)
```

---

## 32. Advanced Architectures

### 32.1 — Planner + Executor Architecture

```
User Query
    │
    ▼
┌─────────────┐
│   PLANNER   │  ← Breaks the problem into subtasks
└──────┬──────┘
       │
       ▼
┌─────────────┐  ┌─────────────┐  ┌─────────────┐
│  Executor 1 │  │  Executor 2 │  │  Executor 3 │
│  (Research) │  │   (Code)    │  │  (Review)   │
└─────────────┘  └─────────────┘  └─────────────┘
       │                │                │
       └────────────────┼────────────────┘
                        ▼
                 Final Result ✅
```

### 32.2 — Reflection Architecture

```
Generate Answer
       │
       ▼
Critique Answer  ← "Is this accurate? Is it complete?"
       │
       ▼
Improve Answer
       │
       ▼
Final Polished Response ✅
```

---

## 33. Best Practices

| # | Practice | Example |
|---|----------|---------|
| 1️⃣ | **Give clear instructions** | `"Provide concise technical answers with code examples"` |
| 2️⃣ | **Limit tool access** | Only give agents the tools they need |
| 3️⃣ | **Use specialized agents** | One agent per responsibility |
| 4️⃣ | **Manage memory carefully** | Too much history = higher cost |
| 5️⃣ | **Use RAG for accuracy** | Grounded responses kill hallucinations |
| 6️⃣ | **Test each agent independently** | Before adding to a team |
| 7️⃣ | **Log everything in production** | You need to debug fast |

---

## 34. Common Errors and Solutions

<details>
<summary><b>❌ Error 1: OPENAI_API_KEY not found</b></summary>

**Cause:** API key not set in environment.

**Fix:**
```bash
# Check your .env file exists and has the key
cat .env

# Load it in your script
from dotenv import load_dotenv
load_dotenv()
```
</details>

<details>
<summary><b>❌ Error 2: Tool not working / ImportError</b></summary>

**Cause:** Missing dependency for the tool.

**Fix:**
```bash
# DuckDuckGo
pip install duckduckgo-search

# YFinance
pip install yfinance

# PDF support
pip install pypdf lancedb sentence-transformers
```
</details>

<details>
<summary><b>❌ Error 3: Module not found / Import Errors</b></summary>

**Cause:** Outdated Phidata version.

**Fix:**
```bash
pip install --upgrade phidata openai
```
</details>

<details>
<summary><b>❌ Error 4: Context too long / Memory Issues</b></summary>

**Cause:** Too many messages in history.

**Fix:** Reduce history length or summarize older messages.

```python
agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    num_history_responses=5,  # Keep only last 5 responses
)
```
</details>

---

## 35. Complete Learning Roadmap

```
🟢 BEGINNER (Week 1-2)
├── Python basics & virtual environments
├── APIs & environment variables
├── Build: Chatbot Agent
├── Build: Calculator Agent
└── Build: Web Search Agent

🟡 INTERMEDIATE (Week 3-5)
├── RAG & Vector Databases
├── Memory Systems
├── Custom Tool Creation
├── Build: PDF Assistant
├── Build: Research Assistant
└── Build: Coding Assistant

🔴 ADVANCED (Week 6-8)
├── Multi-Agent Systems
├── Autonomous Workflows
├── FastAPI + Docker Deployment
├── Build: Finance Agent
├── Build: Voice Assistant
└── Build: Vision Agent

🏆 EXPERT (Week 9-12)
├── Agent Architectures (ReAct, CoT, Reflection)
├── Production Monitoring & Scaling
├── Build: AI Startup Cofounder System
├── Build: Autonomous Research Lab
└── Build: Full AI SaaS Platform
```

---

## 36. Final Capstone Projects

### 🏆 Project 1: Jarvis AI Assistant

**Features:** Voice input/output · Web search · Memory · Coding · File management

### 🔬 Project 2: Autonomous Research Lab

**Features:** Multiple research agents · Citation generation · PDF analysis · Report writing

### 💼 Project 3: AI SaaS Platform

**Features:** User auth · Agent API · Billing · Analytics Dashboard · Production deployment

---

## 🗂️ Project Structure

```
phidata-ai-agents/
│
├── 📁 agents/
│   ├── research_agent.py
│   ├── coding_agent.py
│   └── finance_agent.py
│
├── 📁 tools/
│   ├── weather_tools.py
│   └── custom_tools.py
│
├── 📁 knowledge/
│   └── documents/
│
├── 📁 api/
│   └── main.py              ← FastAPI server
│
├── 📁 frontend/
│   └── app.py               ← Streamlit UI
│
├── 📄 .env                  ← API keys (never commit!)
├── 📄 .gitignore
├── 📄 requirements.txt
├── 📄 Dockerfile
└── 📄 README.md
```

---

## 📦 requirements.txt

```txt
phidata
openai
python-dotenv
duckduckgo-search
fastapi
uvicorn
streamlit
pypdf
lancedb
sentence-transformers
sqlalchemy
yfinance
speechrecognition
pyttsx3
```

---

## 🛣️ What to Learn Next

After mastering Phidata, explore these technologies:

[![LangGraph](https://img.shields.io/badge/1-LangGraph-1C3C5A?style=flat-square&logo=langchain&logoColor=white)](https://langchain.com)
[![CrewAI](https://img.shields.io/badge/2-CrewAI-F97316?style=flat-square&logo=python&logoColor=white)](https://crewai.com)
[![AutoGen](https://img.shields.io/badge/3-AutoGen-0078D4?style=flat-square&logo=microsoft&logoColor=white)](https://microsoft.github.io/autogen)
[![OpenAI SDK](https://img.shields.io/badge/4-OpenAI%20Agents%20SDK-412991?style=flat-square&logo=openai&logoColor=white)](https://openai.com)
[![MCP](https://img.shields.io/badge/5-MCP%20Protocol-6C63FF?style=flat-square&logo=databricks&logoColor=white)](https://modelcontextprotocol.io)
[![Docker](https://img.shields.io/badge/6-Docker-2496ED?style=flat-square&logo=docker&logoColor=white)](https://docker.com)
[![Kubernetes](https://img.shields.io/badge/7-Kubernetes-326CE5?style=flat-square&logo=kubernetes&logoColor=white)](https://kubernetes.io)
[![FastAPI](https://img.shields.io/badge/8-FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)

---

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/new-agent`
3. Commit your changes: `git commit -m 'Add new agent example'`
4. Push to branch: `git push origin feature/new-agent`
5. Open a Pull Request

---

<div align="center">

## ⭐ If this guide helped you, please star the repo!

[![Star History](https://img.shields.io/github/stars/agentstack-ai/phidata-agent-masterguide?style=social)](https://github.com)

**Happy Building! 🚀🤖**

---

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=100&section=footer" width="100%"/>

*Built with ❤️ for the AI Agent developer community*

[![Made with Phidata](https://img.shields.io/badge/Made%20with-Phidata-6C63FF?style=for-the-badge&logo=databricks&logoColor=white)](https://phidata.com)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)

</div>