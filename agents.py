import os
from crewai import Agent
from crewai.tools import tool
from tavily import TavilyClient

# Setup Tavily Client
tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

# Define Custom Web Search Tool
@tool("Search Internet")
def search_tool(query: str) -> str:
    """Useful to search the internet for information about a given topic and return relevant results."""
    try:
        response = tavily_client.search(query=query, max_results=5)
        return str(response)
    except Exception as e:
        return f"Error searching the internet: {e}"

# 1. Senior Research Analyst Agent
researcher = Agent(
    role='Senior Research Analyst',
    goal='Uncover cutting-edge developments and comprehensive information about {topic}',
    backstory='''You are an expert researcher. You have a knack for finding the most 
    accurate, relevant, and recent information on the internet. You use your tools 
    efficiently to gather raw data and sources.''',
    verbose=True,
    allow_delegation=False,
    tools=[search_tool],
    llm=os.getenv("GEMINI_MODEL", "gemini/gemini-1.5-flash"),
    max_rpm=10
)

# 2. Information Strategist Agent
analyst = Agent(
    role='Information Strategist',
    goal='Analyze the raw data provided by the researcher and create a structured outline for the report on {topic}',
    backstory='''You are a master of organizing chaos. You take raw information, filter out 
    the noise, and structure it into logical, easy-to-read sections. You plan the flow 
    of the report.''',
    verbose=True,
    allow_delegation=False,
    llm=os.getenv("GEMINI_MODEL", "gemini/gemini-1.5-flash"),
    max_rpm=10
)

# 3. Technical Writer Agent
writer = Agent(
    role='Professional Technical Writer',
    goal='Draft a compelling, well-structured, and highly readable report on {topic} based on the outline',
    backstory='''You are a renowned writer known for your clear, engaging, and professional 
    writing style. You transform outlines into final drafts that are easy to digest 
    but packed with value.''',
    verbose=True,
    allow_delegation=False,
    llm=os.getenv("GEMINI_MODEL", "gemini/gemini-1.5-flash"),
    max_rpm=10
)

# 4. Chief Editor Agent
editor = Agent(
    role='Chief Editor & Fact Checker',
    goal='Review the drafted report on {topic} for grammar, flow, factual accuracy, and proper formatting. Ensure the final output is flawless.',
    backstory='''You are a strict and detail-oriented editor. You review drafts meticulously. 
    You fix grammatical errors, improve readability, ensure tone consistency, and 
    verify that the final document is ready for professional publishing.''',
    verbose=True,
    allow_delegation=False,
    llm=os.getenv("GEMINI_MODEL", "gemini/gemini-1.5-flash"),
    max_rpm=10
)
