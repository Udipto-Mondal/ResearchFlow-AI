# Pydantic v1 compatibility patch for ChromaDB on modern Python runtimes (Python 3.12 - 3.14)
try:
    import typing
    import pydantic.v1.fields as _pv1_fields
    _orig_set_default_and_type = _pv1_fields.ModelField._set_default_and_type

    def _patched_set_default_and_type(self):
        if getattr(self, 'type_', None) is _pv1_fields.Undefined:
            self.type_ = typing.Any
            self.annotation = typing.Any
        try:
            _orig_set_default_and_type(self)
        except Exception:
            self.type_ = typing.Any
            self.annotation = typing.Any
            if not hasattr(self, 'outer_type_'):
                self.outer_type_ = typing.Any

    _pv1_fields.ModelField._set_default_and_type = _patched_set_default_and_type
except Exception:
    pass

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
