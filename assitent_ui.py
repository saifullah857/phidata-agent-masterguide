import streamlit as st 
from phi.model.groq import Groq 
from dotenv import load_dotenv
from phi.agent import Agent 
from phi.tools.duckduckgo import DuckDuckGo

load_dotenv()

st.markdown("""
<style>

.stButton > button {
    background: linear-gradient(90deg, #06b6d4, #3b82f6);
    color: white;
    border: none;
    border-radius: 12px;
    padding: 12px 24px;
    font-size: 18px;
    font-weight: bold;
}

.stButton > button:hover {
    background: none;
    border-radius: 2px solid skyblue;
    border : 3px solid skyblue;
    
}

</style>
""", unsafe_allow_html=True)

st.set_page_config(
    page_title=("Personal AI Assistent"),
    page_icon=("🤖"),
    layout="wide"
)

st.title("Your Personal 🤖 AI Assistent")

query = st.text_area("How i can assist you",width=700)

if st.button("Generate"):
    if query:
        with st.spinner("🤖 AI is Thinking ...."):
            agent = Agent(
                model = Groq(
                    id = "llama-3.3-70b-versatile"
                ),
                tools=[DuckDuckGo()],
                markdown=True
            )
            
            prompt = f"""
            You are personal AI Assistent
            use structherd and clean language 
            add example 
            output proper using clear and clean markdown
            according to query
            Query :
            {query}
            and also provide current info if user asks
            using 
            {DuckDuckGo()}
            """
            
            response = agent.run(prompt)
            st.markdown(" 🤖 AI Response")
            st.write(response.content)
            
    else:
        st.error("Please Enter question for response")