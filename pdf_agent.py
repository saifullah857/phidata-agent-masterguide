from phi.agent import Agent
from phi.model.groq import Groq
from pypdf import PdfReader
from dotenv import load_dotenv

load_dotenv()

# 1️⃣ Load PDF manually (NO embeddings, NO vector DB)
def load_pdf_text(path):
    reader = PdfReader(path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text


def pdf_agent():
    pdf_text = load_pdf_text("Phidata Complete Agent Building Master Guide.pdf")

    agent = Agent(
        model=Groq(id="llama-3.3-70b-versatile"),
        markdown=True
    )

    query = input("Ask something from PDF: ")

    prompt = f"""
    
    QUESTION:
    {query}
    """

    agent.print_response(prompt)


pdf_agent()