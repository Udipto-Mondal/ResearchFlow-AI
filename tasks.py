from crewai import Task
from agents import researcher, analyst, writer, editor

# Task 1: Research
research_task = Task(
    description='''Conduct a comprehensive research on the topic: "{topic}". 
    Use the search tool to find recent articles, data, and key insights. 
    Compile a detailed list of facts, statistics, and sources.''',
    expected_output='A raw document containing detailed research findings, facts, and URLs of sources.',
    agent=researcher
)

# Task 2: Analyze & Structure
analyze_task = Task(
    description='''Review the research data provided by the researcher on "{topic}". 
    Extract the most important points and create a detailed outline with headings 
    and subheadings for a professional report.''',
    expected_output='A structured outline of the report with clear sections and bullet points.',
    agent=analyst
)

# Task 3: Write Draft
write_task = Task(
    description='''Using the outline provided by the strategist, write a full draft of the report on "{topic}". 
    Ensure the tone is professional and engaging. Include an introduction, body paragraphs, and a conclusion. 
    Incorporate the sources/citations naturally.''',
    expected_output='A complete draft of the report written in markdown format.',
    agent=writer
)

# Task 4: Edit & Polish
edit_task = Task(
    description='''Review the draft report on "{topic}". 
    Check for grammatical errors, improve the flow, and ensure professional formatting. 
    Output the final, polished report in pristine Markdown format ready for PDF conversion.''',
    expected_output='A final, polished, error-free report in Markdown format.',
    agent=editor
)
