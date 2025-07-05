import os
from dotenv import load_dotenv
from crewai import LLM
from tavily import TavilyClient
from scrapegraph_py import Client
from crewai.knowledge.source.string_knowledge_source import StringKnowledgeSource

# Load environment variables
load_dotenv()

# API Keys
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
AGENTOPS_API_KEY = os.getenv("AGENTOPS_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
SCRAPEGRAPH_API_KEY = os.getenv("SCRAPEGRAPH_API_KEY")

# Initialize clients
search_client = TavilyClient(api_key=TAVILY_API_KEY)
scrape_client = Client(api_key=SCRAPEGRAPH_API_KEY)

# LLM Configuration (Using OpenRouter with Gemini 2.0 Flash Experimental)
basic_llm = LLM(
    model="openrouter/cypher-alpha:free",
    api_key=OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1",
    temperature=0,
)

# Output directory
OUTPUT_DIR = "./ai-agent-output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Company context
ABOUT_COMPANY = "Rankyx is a company that provides AI solutions to help websites refine their search and recommendation systems, with a focus on optimizing procurement in markets like Morocco."
company_context = StringKnowledgeSource(content=ABOUT_COMPANY)

# Constants
NO_KEYWORDS = 5
SCORE_THRESHOLD = 0.50
TOP_RECOMMENDATIONS_NO = 5