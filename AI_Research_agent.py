from typing import TypedDict, Annotated
from pydantic import BaseModel, Field
from langgraph.graph import StateGraph, START, END
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
import os
import operator
from langchain_community.tools import TavilySearchResults
from IPython.display import Markdown

load_dotenv()

llm = ChatOpenAI(
    model="openrouter/free",
    api_key=os.environ.get("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

class report(BaseModel):
    title: str = Field(description="Title of the report")
    introduction: str = Field(description="Introduction to the report ")
    key_findings: list[str] = Field(description="What are the key findings of the report ")
    conclusion: str = Field(description="what is the conclussion of the report ")
    sources: list[str] = Field(description="what are the sources of the report ")

class ResearchState(TypedDict):
    topic: str
    search_result: Annotated[list[str], operator.add]
    summary: str
    report: report
    final: str

groq_llm = ChatGroq(model="llama-3.1-8b-instant")
structured_llm = groq_llm.with_structured_output(report)

def tavily_search(state: ResearchState):
    max_result = 10
    topic = state["topic"]
    tool = TavilySearchResults(max_results=max_result)
    response = tool.invoke(topic)
    
    # Extracts the content strings from the Tavily dictionary objects to match your state definition
    extracted_results = [item["content"] for item in response if "content" in item]
    return {"search_result": extracted_results}

summary_system = """You are the summarizer who will summarize the raw output result from the internet and organize in the form of the title,sources """

def summary_node(state: ResearchState):
    result = state["search_result"]
    response = llm.invoke([SystemMessage(content=summary_system), HumanMessage(content=f"summarise this raw internet output {result}")])
    return {"summary": response.content}

report_system = """You are a report maker you tak the raw output of the internet and arrange and make a meanigfull readable format manner like intro,key_findings,source and all like this"""

def report_node(state: ResearchState):
    topic = state["topic"]
    summary = state["summary"]
    response = structured_llm.invoke([SystemMessage(content=report_system), HumanMessage(content=f"Make a report for the topic {topic} the summary rquired for this {summary}")])
    return {"report": response}

def markdown(state: ResearchState):
    report = state["report"]
    sources = "\n".join(f"- {point}" for point in report.sources)
    key_findings = "\n".join(f"- {point}" for point in report.key_findings)
    
    markdown_content = f"""# {report.title}

## Introduction
{report.introduction}

## Key Findings
{key_findings}

## Conclusion
{report.conclusion}

## Sources
{sources}
"""
    return {"final": markdown_content}

graph = StateGraph(ResearchState)
graph.add_node("tavily_search", tavily_search)
graph.add_node("report_node", report_node)
graph.add_node("markdown", markdown)
graph.add_node("summary_node", summary_node)

graph.add_edge(START, "tavily_search")
graph.add_edge("tavily_search", "summary_node")
graph.add_edge("summary_node", "report_node")
graph.add_edge("report_node", "markdown")
graph.add_edge("markdown", END)

workflow = graph.compile()

result = workflow.invoke({"topic": "AI REVOLUTION"})

Markdown(result["final"])