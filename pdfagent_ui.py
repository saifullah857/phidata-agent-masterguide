import streamlit as st 
from phi.agent import Agent 
from phi.model.groq import Groq 
from pypdf import PdfReader
from dotenv import load_dotenv

load_dotenv()

def load_pdf_text(uploaded_file):
    reader = PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
        
    return text
    
st.set_page_config(
    page_title=" Pdf AI Agent",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 PDF AI Agent (Upload pdf and ask question from pdf)")

uploaded_file = st.file_uploader("Uploade any pdf file",type="pdf",width=1000)

if uploaded_file is not None:

    # Read PDF Text
    pdf_text = load_pdf_text(uploaded_file)
    st.success("✅ PDF Uploaded Successfully",width=1000)
    with st.expander("📘 View Extracted PDF Text",width=1000):
        st.write(pdf_text[:2000])
        
query = st.text_input("Ask anything from PDF",width=1000)

if st.button("Generate"):
    if query:
        with st.spinner("🤖 AI is thinking ...."):
            agent = Agent(
                model = Groq(
                    id = "llama-3.3-70b-versatile"
                ),
                markdown=True,
            )
            
            prompt = f"""
            You are PDF assistent 
            answer only from given pdf content
            PDF Content:
            {pdf_text}
            Query :
            {query}
            """
            
            response = agent.run(prompt)
            st.markdown("🤖 AI Response :")
            st.write(response.content)
    else:
        st.write("⚠ Please Enter Question")
