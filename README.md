# AI Research Agent

An AI-powered research assistant that performs intelligent web research, summarizes information, and generates clean markdown reports using LangGraph-based workflows.

## Features
- Web research with Tavily
- AI summarization
- Structured markdown report generation
- Streamlit frontend
- FastAPI REST endpoint
- Docker containerization

## Tech Stack
- Python
- LangGraph
- LangChain
- Groq
- OpenRouter
- Streamlit
- FastAPI
- Docker

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

### Run Streamlit Frontend
```bash
streamlit run streamlit_frontend.py
```

### Run FastAPI Server
```bash
uvicorn api:app --reload
```

### Run with Docker
```bash
docker build -t ai-research-agent .
docker run -p 8501:8501 ai-research-agent
```
