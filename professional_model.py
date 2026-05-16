from phi.agent import Agent
from phi.model.groq import Groq
from dotenv import load_dotenv

load_dotenv()

agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    instructions=[
        "Explain step by step",
        "Provide examples",
        "Use markdown",
    ],
    markdown=True,
)

agent.print_response("Line drawing algorithm in computer graphics")