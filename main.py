from crewai import Crew, Process
from tasks import create_tasks
import os

def main():
    print("=== Job Application Assistant ===\n")
    
    # Get inputs
    company_name = input("Enter the company name: ")
    print("\nPaste the job posting (press Enter twice when done):")
    
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    job_posting = "\n".join(lines)
    
    resume_path = "resume.pdf"
    
    # Verify resume exists
    if not os.path.exists(resume_path):
        print(f"\nError: {resume_path} not found. Please add your resume to the project folder.")
        return
    
    print("\n🚀 Starting job application creation...\n")
    
    # Create tasks
    tasks = create_tasks(job_posting, company_name, resume_path)
    
    # Create crew
    crew = Crew(
        agents=[task.agent for task in tasks],
        tasks=tasks,
        process=Process.sequential,
        verbose=True
    )
    
    # Run the crew
    result = crew.kickoff()
    
    # Save outputs
    os.makedirs("outputs", exist_ok=True)
    
    with open(f"outputs/{company_name.replace(' ', '_')}_application.txt", "w") as f:
        f.write(str(result))
    
    print(f"\n✅ Application materials saved to outputs/{company_name.replace(' ', '_')}_application.txt")
    print("\n" + "="*50)
    print(result)

if __name__ == "__main__":
    main()