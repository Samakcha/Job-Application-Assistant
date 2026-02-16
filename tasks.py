from crewai import Task
from agents import job_analyzer, company_researcher, resume_tailor, cover_letter_writer

def create_tasks(job_posting: str, company_name: str, resume_path:str):
 analyze_job_task = Task(
  description=f"""Analyze this job posting and extract:
    1. Required skills and qualifications
    2. Preferred skills and qualifications
    3. Key responsibilities
    4. Company culture indicators
    5. Main problems this role will solve

    Job Posting:
    {job_posting}

    Provide structured analysis that other agents can use.
  """,
  agent=job_analyzer,
  expected_output="A detailed analysis of the job posting with categorized requirements and insights"
 )
 
 research_company_task = Task(
  description=f"""Research{company_name} and find:
    1. Company mission and values
    2. Recent news or achievements (last 6 months)
    3. Products or services
    4. Company culture and work environment
    5. Any notable facts that could be referenced in an application

    Provide specific, recent information that can personalize the application.
  """,
  agent=company_researcher,
  expected_output="Comprehensive company research with specific, recent details",
  context=[analyze_job_task]
 )

 tailor_resume_task = Task(
  description=f"""Read the resume from {resume_path}:
  Using the job analysis, create a tailored version of the resume that:
  1. Emphasizes experiences relevant to the job requirements
  2. Uses keywords from the job posting naturally
  3. Highlights accomplishments that match what they're looking for
  4. Reorganizes sections if needed to put most relevant info first
  5. Keeps all information truthful
  
  Output a complete, customized resume ready to submit.
  """,
  agent=resume_tailor,
  expected_output="A fully tailored resume in a clean, professional format",
  context=[analyze_job_task]
 )

 write_cover_letter_task = Task(
    description=f"""Write a compelling cover letter for {company_name} that:
    1. Opens with genuine enthusiasm and a strong hook
    2. References specific company research findings
    3. Connects the candidate's experience to job requirements
    4. Tells a brief story about relevant accomplishments
    5. Explains why this role and company are a great fit
    6. Closes with a clear call to action

    Keep it to 3-4 paragraphs, professional but personable.
    Make it specific to this company and role - avoid generic statements.
    """,
    agent=cover_letter_writer,
    expected_output="A personalized, compelling cover letter ready to send",
    context=[analyze_job_task, research_company_task, tailor_resume_task]
 )

 return [analyze_job_task, research_company_task, tailor_resume_task, write_cover_letter_task]