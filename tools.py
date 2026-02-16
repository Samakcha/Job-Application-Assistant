import PyPDF2
from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import PyPDF2

class ResumeReaderInput(BaseModel):
    """Input schema for Resume Reader tool"""
    file_path: str = Field(..., description="Path to the resume PDF file")

class ResumeReaderTool(BaseTool):
    name: str = "Resume Reader"
    description: str = "Reads and extracts text from a PDF resume file. Provide the file path to the resume."
    args_schema: Type[BaseModel] = ResumeReaderInput

    def _run(self, file_path: str) -> str:
        """Reads and extracts text from a PDF resume file."""
        try:
          with open(file_path, 'rb') as file:
              pdf_reader = PyPDF2.PdfReader(file)
              text = ""
              for page in pdf_reader.pages:
                  text += page.extract_text()
              return text
        except Exception as e:
          return f"Error reading resume: {str(e)}"