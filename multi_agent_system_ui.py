from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.duckduckgo import DuckDuckGo
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

# ---------------- PAGE CONFIG ---------------- #
st.set_page_config(
    page_title="Multi Agent AI System",
    page_icon="🤖",
    layout="wide"
)

# ---------------- TITLE ---------------- #
st.title("🤖 Multi Agent AI Startup System")

st.markdown("""
This AI system uses multiple specialized agents:
- 🔍 Research Agent
- 💰 Finance Agent
- 💻 Developer Agent
- 📈 Marketing Agent
""")

# ---------------- USER INPUT ---------------- #
user_query = st.text_area(
    "Enter Your Startup Idea / Query",
    height=180,
    placeholder="Example: I want to build an AI fitness app..."
)

# ---------------- BUTTON ---------------- #
generate = st.button(
    "🚀 Generate Startup Plan",
    use_container_width=True
)

# ---------------- GENERATE RESPONSE ---------------- #
if generate:

    if not user_query:
        st.error("⚠ Please enter your query")
    
    else:
        with st.spinner("🤖 AI agents are collaborating..."):

            # ---------------- RESEARCH AGENT ---------------- #
            research_agent = Agent(
                name="Research Agent",
                role="Analyzes market trends and competitors",
                model=Groq(id="llama-3.3-70b-versatile"),
                tools=[DuckDuckGo()],
                instructions=[
                    "Research startup competitors",
                    "Find market trends",
                    "Analyze business opportunities",
                    "Use web search when required"
                ],
                markdown=True
            )

            # ---------------- FINANCE AGENT ---------------- #
            finance_agent = Agent(
                name="Finance Agent",
                role="Calculates revenue models and business metrics",
                model=Groq(id="llama-3.3-70b-versatile"),
                instructions=[
                    "Estimate startup costs",
                    "Suggest pricing strategy",
                    "Generate revenue ideas",
                    "Estimate profitability"
                ],
                markdown=True
            )

            # ---------------- DEVELOPER AGENT ---------------- #
            developer_agent = Agent(
                name="Developer Agent",
                role="Designs MVP and technical architecture",
                model=Groq(id="llama-3.3-70b-versatile"),
                instructions=[
                    "Create MVP roadmap",
                    "Suggest tech stack",
                    "Design system architecture",
                    "Suggest AI tools and APIs"
                ],
                markdown=True
            )

            # ---------------- MARKETING AGENT ---------------- #
            marketing_agent = Agent(
                name="Marketing Agent",
                role="Creates startup growth and marketing strategy",
                model=Groq(id="llama-3.3-70b-versatile"),
                instructions=[
                    "Create marketing strategy",
                    "Suggest social media growth plan",
                    "Generate branding ideas",
                    "Suggest customer acquisition strategies"
                ],
                markdown=True
            )

            # ---------------- TEAM AGENT ---------------- #
            startup_agent = Agent(
                team=[
                    research_agent,
                    finance_agent,
                    developer_agent,
                    marketing_agent
                ],
                model=Groq(id="llama-3.3-70b-versatile"),
                instructions=[
                    "Combine outputs from all agents",
                    "Generate a complete startup execution plan",
                    "Make the response structured and professional"
                ],
                markdown=True,
            )

            # ---------------- PROMPT ---------------- #
            prompt = f"""
                User Startup Idea:
                {user_query}

                Create a professional startup execution report.

                Include:
                # Startup Overview
                # Market Research
                # Competitor Analysis
                # Revenue Model
                # MVP Features
                # Tech Stack
                # System Architecture
                # Marketing Strategy
                # Growth Strategy
                # Monetization Plan
                # Launch Plan
                # Future Scaling
                # Development Road Map

                Important:
                - Do NOT show internal agent communication
                - Do NOT show tool transfer logs
                - Return only final polished response
                """

            # ---------------- RESPONSE ---------------- #
            response = startup_agent.run(prompt)

            # ---------------- OUTPUT ---------------- #
            st.markdown("## 🤖 Multi-Agent AI Response")

            st.markdown(response.content)