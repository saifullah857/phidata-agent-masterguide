from phi.agent import Agent 
from phi.model.groq import Groq 
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv


load_dotenv()

def memory_agent():
    
    agent = Agent(
        model = Groq(id = "llama-3.3-70b-versatile"),
        add_chat_history_to_messages=True,
        tools=[DuckDuckGo()],
        show_tool_calls=True,
        instructions=[
            "Give answer using resourses and proof",
            "use clean and structred format",
            "also use markdown for output"
        ],
        markdown=True
    )
    
    msg1 = input("How can i assist you : ")
    agent.print_response(msg1)
    
    msg2 = input("Can u wants know more about it :")
    agent.print_response(msg2)
    
memory_agent()
