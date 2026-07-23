# Job Application Assistant (Agentic AI)

An AI-powered Job Application Assistant built using **CrewAI multi-agent architecture** that automatically analyzes job postings, researches companies, tailors resumes, and generates personalized cover letters.

This project demonstrates practical implementation of **Agentic AI workflows**, where multiple specialized AI agents collaborate sequentially to produce high-quality job application materials.

---

## Features

Multi-Agent AI Workflow (CrewAI)  
Job Posting Analysis  
Automated Company Research  
Resume Tailoring based on job requirements  
Personalized Cover Letter Generation  
Sequential Agent Collaboration  
Resume PDF parsing tool  

---

## How It Works

The system uses multiple specialized AI agents that collaborate like a real hiring assistant team:

### Job Posting Analyzer
- Extracts required skills
- Identifies key responsibilities
- Detects company culture signals
- Understands hiring priorities

### Company Research Specialist
- Searches company information
- Finds mission, values, products
- Retrieves recent company news
- Helps personalize applications

### Resume Customization Expert
- Reads resume PDF
- Highlights relevant experience
- Injects job-specific keywords
- Reorders content for impact

### Cover Letter Specialist
- Generates personalized cover letters
- Connects candidate experience to role
- Uses company research insights

---

## Architecture

```
User Input
   ↓
Job Posting Analyzer Agent
   ↓
Company Research Agent
   ↓
Resume Tailoring Agent
   ↓
Cover Letter Writer Agent
   ↓
Final Application Output
```

Agents run sequentially using CrewAI workflow orchestration.

---

## Project Structure

```
Job-Application-Assistant/
│
├── main.py          # Entry point (CLI application)
├── agents.py        # Agent definitions
├── tasks.py         # Task orchestration logic
├── tools.py         # Custom tools (PDF resume reader)
├── requirements.txt
├── resume.pdf       # User resume (input)
└── outputs/         # Generated applications
```

---

## Installation

### Clone repository

```bash
git clone https://github.com/Samakcha/Job-Application-Assistant.git
cd Job-Application-Assistant
```

### Create virtual environment

```bash
python -m venv venv
source venv/bin/activate      # Mac/Linux
venv\Scripts\activate         # Windows
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create `.env` file:

```
OPENAI_API_KEY=your_api_key_here
SERPER_API_KEY=your_serper_key_here
```

(Optional: Gemini LLM setup can be enabled inside `agents.py`.)

---

## Usage

Place your resume as:

```
resume.pdf
```

Run:

```bash
python main.py
```

You will be prompted to:

1. Enter company name
2. Paste job posting text

---

## Output

Generated application materials will be saved in:

```
outputs/<company_name>_application.txt
```

Includes:

- Job analysis
- Company research summary
- Tailored resume
- Personalized cover letter

---

## Technologies Used

- Python
- CrewAI (Agentic workflows)
- LLM Agents
- Serper Search Tool
- PyPDF2
- dotenv

---

## Why This Project?

This project showcases:

- Real-world Agentic AI implementation
- Multi-agent collaboration patterns
- Automated workflow orchestration
- Practical AI productivity tooling

Ideal for demonstrating:

- AI engineering skills
- LLM orchestration
- Agent-based system design

---

## Future Improvements

- Web UI (Next.js or React)
- Job scraping automation
- LinkedIn integration
- Multiple resume versions
- RAG-based resume memory
- Async agent execution

---

## Author

Built by Samakcha Mishra

---

## If you like this project

Give it a star and feel free to contribute!

