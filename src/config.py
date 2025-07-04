import os
from dotenv import load_dotenv
from crewai import LLM
from tavily import TavilyClient
from scrapegraph_py import Client
from crewai.knowledge.source.string_knowledge_source import StringKnowledgeSource

# Load environment variables
load_dotenv()

# API Keys
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
AGENTOPS_API_KEY = os.getenv("AGENTOPS_API_KEY")
TVLY_API_KEY = os.getenv("TVLY_API_KEY")
SCRAPEGRAPH_API_KEY = os.getenv("SCRAPEGRAPH_API_KEY")

# Initialize clients
search_client = TavilyClient(api_key=TVLY_API_KEY)
scrape_client = Client(api_key=SCRAPEGRAPH_API_KEY)

# LLM Configuration (Using Gemini)
basic_llm = LLM(model="gemini/gemini-1.5-pro", api_key=GEMINI_API_KEY, temperature=0)

# Output directory
OUTPUT_DIR = "./ai-agent-output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Company context
ABOUT_COMPANY = "Rankyx is a company that provides AI solutions to help websites refine their search and recommendation systems, with a focus on optimizing procurement in markets like Morocco."
company_context = StringKnowledgeSource(content=ABOUT_COMPANY)

# Constants
NO_KEYWORDS = 10
SCORE_THRESHOLD = 0.10
TOP_RECOMMENDATIONS_NO = 10