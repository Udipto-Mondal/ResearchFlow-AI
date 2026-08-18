from dotenv import load_dotenv
load_dotenv() # Load environment variables from .env

from crewai import Crew, Process
from agents import researcher, analyst, writer, editor
from tasks import research_task, analyze_task, write_task, edit_task

def generate_report(topic: str):
    # Create the Crew
    report_crew = Crew(
        agents=[researcher, analyst, writer, editor],
        tasks=[research_task, analyze_task, write_task, edit_task],
        process=Process.sequential, # Tasks will run one after another
        verbose=True
    )

    # Start the execution
    print(f"Starting research on: {topic}...\n")
    result = report_crew.kickoff(inputs={'topic': topic})
    
    # Save the output to a markdown file
    output_filename = f"{topic.replace(' ', '_')}_Report.md"
    with open(output_filename, "w", encoding="utf-8") as file:
        file.write(result.raw if hasattr(result, 'raw') else str(result))
        
    print(f"\nReport generated and saved as {output_filename}")
    return result

if __name__ == "__main__":
    print("Welcome to ResearchFlow AI")
    user_topic = input("Enter the topic you want to research and write a report on: ")
    
    if user_topic.strip():
        generate_report(user_topic)
    else:
        print("Topic cannot be empty!")
