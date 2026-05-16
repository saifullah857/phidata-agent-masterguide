from phi.agent import Agent
from phi.model.groq import Groq
from phi.embedder.openai import OpenAIEmbedder
from phi.knowledge.pdf import PDFUrlKnowledgeBase
from phi.vectordb.lancedb import LanceDb, SearchType
from dotenv import load_dotenv

load_dotenv()

# ---------------- KNOWLEDGE BASE ---------------- #

knowledge_base = PDFUrlKnowledgeBase(
    urls=[
        "Phidata_Groq_Complete_Guide.pdf"
    ],

    # Vector Database
    vector_db=LanceDb(
        table_name="recipes",
        uri="tmp/lancedb",
        search_type=SearchType.vector,

        # Embedding Model
        embedder=OpenAIEmbedder(
            model="text-embedding-3-small"
        ),
    ),
)

# Load PDF into Vector DB
knowledge_base.load(upsert=True)

# ---------------- AGENT ---------------- #

agent = Agent(
    model=Groq(
        id="llama-3.3-70b-versatile"
    ),

    knowledge=knowledge_base,

    markdown=True,

    show_tool_calls=False,
)

# ---------------- QUERY ---------------- #

agent.print_response(
    "How many total chapter in pdf",
    stream=True
)