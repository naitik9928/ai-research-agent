# AI Research Agent

An AI-powered research assistant that searches the web, summarizes information, and generates structured markdown reports using LangGraph workflows.

## Features

- Web research with Tavily
- AI summarization
- Structured report generation
- Streamlit frontend
- Markdown output

## Tech Stack

- Python
- LangGraph
- LangChain
- Groq
- OpenRouter
- Streamlit

## Installation

```bash
git clone https://github.com/naitik9928/ai-research-agent.git
cd ai-research-agent
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file:

```env
OPENROUTER_API_KEY=your_key
GROQ_API_KEY=your_key
TAVILY_API_KEY=your_key
```

## How to Run

```bash
streamlit run streamlit_frontend.py
```
