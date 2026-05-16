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
    page_title="PDF AI Agent",
    page_icon="📄",
    layout="wide"
)


st.title("📄 PDF AI Agent using Groq + Phidata")
st.write("Upload a PDF and ask questions from it.")


uploaded_file = st.file_uploader(
    "Upload PDF File",
    type=["pdf"]
)

if uploaded_file is not None:

    # Read PDF Text
    pdf_text = load_pdf_text(uploaded_file)

    st.success("✅ PDF Uploaded Successfully")

    # =========================
    # Show PDF Content
    # =========================
    with st.expander("📘 View Extracted PDF Text"):
        st.write(pdf_text[:5000])

    # =========================
    # User Question
    # =========================
    query = st.text_input(
        "Ask something from PDF"
    )

    # =========================
    # Ask Button
    # =========================
    if st.button("Generate Answer"):

        if query:

            with st.spinner("Thinking..."):

                # =========================
                # Create Agent
                # =========================
                agent = Agent(
                    model=Groq(
                        id="llama-3.3-70b-versatile"
                    ),
                    markdown=True
                )

                # =========================
                # Prompt
                # =========================
                prompt = f"""
                You are a PDF assistant.

                Answer ONLY from the given PDF content.

                PDF CONTENT:
                {pdf_text}

                QUESTION:
                {query}
                """

                # =========================
                # Get Response
                # =========================
                response = agent.run(prompt)

                # =========================
                # Display Answer
                # =========================
                st.markdown("## 🤖 AI Response")
                st.write(response.content)

        else:
            st.warning("⚠ Please enter a question.")