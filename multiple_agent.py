from phi.agent import Agent 
from phi.model.groq import Groq 
from phi.tools.calculator import Calculator
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv

load_dotenv()

def calculator_agent():

    agent = Agent(
        model=Groq(id="llama-3.3-70b-versatile"),
        tools=[Calculator()],
        show_tool_calls=True,
        instructions=[
            "You are a Math teacher with 10 years of experience",
            "Explain using ELI10 method with examples",
            "Use clear and structured markdown"
        ],
        markdown=True
    )
    agent.print_response("calculate 3+5*8/4-2")


def web_search_agent():
    try:
        agent = Agent(
            model=Groq(
                id="llama-3.3-70b-versatile"
            ),
            tools=[DuckDuckGo()],
            tool_choice="auto",
            reasoning=False,
            show_tool_calls=True,
            instructions=[
            "You are a helpful AI assistant",
            "Explain in simple language",
            "Use markdown formatting"
            ],
            markdown=True
        )
        response = agent.run(
            "Who is the current Prime Minister of Pakistan and his background?"
        )
        print(response.content)

    except Exception as e:
        print("Error:", e)


def python_coding_agent():

    coding_agent = Agent(
        model=Groq(id="llama-3.3-70b-versatile"),
        markdown=True,
        tool_choice="none",  
        show_tool_calls=False,
        instructions=[
            "You are an expert Python developer.",
            "ONLY generate code.",
            "Do NOT try to use tools or save files.",
            "Do NOT execute code.",
            "Return plain Python code only."
        ],
    )
    response = coding_agent.run(
        "Create a todo app in python"
    )

    print(response.content)

python_coding_agent()