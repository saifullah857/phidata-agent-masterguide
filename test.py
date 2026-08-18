from phi.agent import Agent
from phi.model.groq import Groq
from dotenv import load_dotenv

load_dotenv()

agent = Agent(
    model=Groq(id="openai/gpt-oss-20b"),
    markdown=True
)

agent.print_response("give me emails of hr in lahore thats currently work on ai ml or hiring in ai ml for internships")