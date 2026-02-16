from crewai import Agent, LLM
from crewai_tools import SerperDevTool
from tools import ResumeReaderTool
import os
from dotenv import load_dotenv

load_dotenv()

# if you want to use gemini key and model
# llm = LLM(
#     model="gemini/gemini-1.5-flash-002",
#     api_key=os.getenv("GOOGLE_API_KEY")
# )

search_tool = SerperDevTool()
resume_reader = ResumeReaderTool()


job_analyzer = Agent(
  role="Job Posting Analyzer",
  goal="Extract and analyze key requirements, skills, and qualifications from job postings",
  backstory="""You are an expert at reading job postings and identifying what employers 
    really want. You can spot required vs. preferred qualifications, understand company 
    culture signals, and identify the core problems this role needs to solve.""",
  verbose=True,
  allow_delegation=False,
  # llm=llm
)

company_researcher = Agent(
  role="Company Research Specialist",
  goal="Research companies to find relevant information for personalized applications",
  backstory="""You are a skilled researcher who finds key information about companies - 
    their mission, recent news, products, culture, and achievements. You help candidates 
    understand what makes each company unique.""",
  tools=[search_tool],
  verbose=True,
  allow_delegation=False,
  # llm=llm
)

resume_tailor = Agent(
  role="Resume Customization Expert",
  goal="Tailor resumes to highlight relevant experience for specific job postings",
  backstory="""You are an expert resume writer who knows how to emphasize relevant 
    experience and skills. You restructure and reframe accomplishments to match job 
    requirements while keeping everything truthful and impactful.""",
  tools=[resume_reader],
  verbose=True,
  allow_delegation=False,
  # llm=llm
)

cover_letter_writer = Agent(
  role="Cover Letter Specialist",
  goal="Write compelling, personalized cover letters that connect candidate experience to job requirements",
  backstory="""You are a master at writing cover letters that tell a story. You connect 
    a candidate's background to the company's needs, reference specific company details, 
    and create genuine enthusiasm that stands out.""",
  verbose=True,
  allow_delegation=False,
  # llm=llm
)