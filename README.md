# Conversational Knowledge Bot
**Assignment Submission for SoulPage IT Solutions**

An intelligent, memory-aware chatbot built using **Google Gemini 2.5 Flash-Lite** and **LangChain**. This bot uses Agentic workflows to search the web via DuckDuckGo and provides cleaned, structured responses to user queries.

##  Key Features
- **Agentic Search:** Autonomously decides when to search the web for real-time information.
- **Context Retention:** Maintains a `ConversationBufferMemory` to track chat history.
- **Thought Cleaning:** Custom logic to handle and clean Gemini 2.5 "Thought Signatures."
- **Optimized for 2026:** Specifically configured for the high-quota Gemini 2.5 Flash-Lite model.

## Tech Stack
- **LLM:** Gemini 2.5 Flash-Lite
- **Framework:** LangChain (Agents, Tools, Memory)
- **Frontend:** Streamlit
- **Search API:** DuckDuckGo Search

## Getting Started

### 1. Prerequisites
- Python 3.9+
- A Google Gemini API Key from [Google AI Studio](https://aistudio.google.com/)

### 2. Installation
```bash
# Clone the repository
git clone [https://github.com/Divya920/Knowledge-Bot-Assignment_SoulPage_IT.git](https://github.com/Divya920/Knowledge-Bot-Assignment_SoulPage_IT.git)

# Install dependencies
pip install -r requirements.txt
