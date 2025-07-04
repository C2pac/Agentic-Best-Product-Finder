from crewai import Agent
from crewai.tools import tool
from pydantic import BaseModel, Field
from typing import List
from src.config import basic_llm, search_client, scrape_client

# Pydantic Models
class SuggestedSearchQueries(BaseModel):
    queries: List[str] = Field(..., title="Suggested search queries to be passed to the search engine",
                               min_items=1, max_items=10)

class SingleSearchResult(BaseModel):
    title: str
    url: str = Field(..., title="the page url")
    content: str
    score: float
    search_query: str

class AllSearchResults(BaseModel):
    results: List[SingleSearchResult]

class ProductSpec(BaseModel):
    specification_name: str
    specification_value: str

class SingleExtractedProduct(BaseModel):
    page_url: str = Field(..., title="The original url of the product page")
    product_title: str = Field(..., title="The title of the product")
    product_image_url: str = Field(..., title="The url of the product image")
    product_url: str = Field(..., title="The url of the product")
    product_current_price: float = Field(..., title="The current price of the product")
    product_original_price: float = Field(title="The original price of the product before discount. Set to None if no discount", default=None)
    product_discount_percentage: float = Field(title="The discount percentage of the product. Set to None if no discount", default=None)
    product_specs: List[ProductSpec] = Field(..., title="The specifications of the product. Focus on the most important specs to compare.", min_items=1, max_items=5)
    agent_recommendation_rank: int = Field(..., title="The rank of the product to be considered in the final procurement report. (out of 5, Higher is Better)")
    agent_recommendation_notes: List[str] = Field(..., title="A set of notes why would you recommend or not recommend this product to the company, compared to other products.")

class AllExtractedProducts(BaseModel):
    products: List[SingleExtractedProduct]

# Tools
@tool
def search_engine_tool(query: str):
    """Useful for search-based queries. Use this to find current information about any query related pages using a search engine"""
    return search_client.search(query)

@tool
def web_scraping_tool(page_url: str):
    """An AI Tool to help an agent to scrape a web page"""
    details = scrape_client.smartscraper(
        website_url=page_url,
        user_prompt="Extract ```json\n" + SingleExtractedProduct.schema_json() + "```\n From the web page"
    )
    return {"page_url": page_url, "details,": details}

# Agents
search_queries_recommendation_agent = Agent(
    role="Search Queries Recommendation Agent",
    goal="\n".join([
        "To provide a list of suggested search queries to be passed to the search engine.",
        "The queries must be varied and looking for specific items."
    ]),
    backstory="The agent is designed to help in looking for products by providing a list of suggested search queries to be passed to the search engine based on the context provided.",
    llm=basic_llm,
    verbose=True,
)

search_engine_agent = Agent(
    role="Search Engine Agent",
    goal="To search for products based on the suggested search query",
    backstory="The agent is designed to help in looking for products by searching for products based on the suggested search queries.",
    llm=basic_llm,
    verbose=True,
    tools=[search_engine_tool]
)

scraping_agent = Agent(
    role="Web scraping agent",
    goal="To extract details from any website",
    backstory="The agent is designed to help in looking for required values from any website url. These details will be used to decide which best product to buy.",
    llm=basic_llm,
    tools=[web_scraping_tool],
    verbose=True,
)

procurement_report_author_agent = Agent(
    role="Procurement Report Author Agent",
    goal="To generate a professional HTML page for the procurement report",
    backstory="The agent is designed to assist in generating a professional HTML page for the procurement report after looking into a list of products.",
    llm=basic_llm,
    verbose=True,
)