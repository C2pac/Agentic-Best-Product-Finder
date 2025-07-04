from crewai import Task
from src.config import OUTPUT_DIR, NO_KEYWORDS, SCORE_THRESHOLD, TOP_RECOMMENDATIONS_NO
from src.agents import (
    search_queries_recommendation_agent, search_engine_agent, scraping_agent,
    procurement_report_author_agent, SuggestedSearchQueries, AllSearchResults, AllExtractedProducts
)
import os

search_queries_recommendation_task = Task(
    description="\n".join([
        "Rankyx is looking to buy {product_name} at the best prices (value for a price strategy)",
        "The company targets any of these websites to buy from: {websites_list}",
        "The company wants to reach all available products on the internet to be compared later in another stage.",
        "The stores must sell the product in {country_name}",
        f"Generate at maximum {NO_KEYWORDS} queries.",
        "The search keywords must be in {language} language.",
        "Search keywords must contain specific brands, types or technologies. Avoid general keywords.",
        "The search query must reach an ecommerce webpage for product, and not a blog or listing page."
    ]),
    expected_output="A JSON object containing a list of suggested search queries.",
    output_json=SuggestedSearchQueries,
    output_file=os.path.join(OUTPUT_DIR, "step_1_suggested_search_queries.json"),
    agent=search_queries_recommendation_agent
)

search_engine_task = Task(
    description="\n".join([
        "The task is to search for products based on the suggested search queries.",
        "You have to collect results from multiple search queries.",
        "Ignore any suspicious links or not an ecommerce single product website link.",
        f"Ignore any search results with confidence score less than ({SCORE_THRESHOLD}).",
        "The search results will be used to compare prices of blenders from e-commerce websites.",
    ]),
    expected_output="A JSON object containing the search results.",
    output_json=AllSearchResults,
    output_file=os.path.join(OUTPUT_DIR, "step_2_search_results.json"),
    agent=search_engine_agent
)

scraping_task = Task(
    description="\n".join([
        "The task is to extract product details from any ecommerce store page url.",
        "The task has to collect results from multiple pages urls.",
        f"Collect the best {TOP_RECOMMENDATIONS_NO} products from the search results.",
    ]),
    expected_output="A JSON object containing products details",
    output_json=AllExtractedProducts,
    output_file=os.path.join(OUTPUT_DIR, "step_3_search_results.json"),
    agent=scraping_agent
)

procurement_report_author_task = Task(
    description="\n".join([
        "The task is to generate a professional HTML page for the procurement report.",
        "You have to use Bootstrap CSS framework for a better UI.",
        "Use the provided context about the company to make a specialized report.",
        "The report will include the search results and prices of products from different websites.",
        "The report should be structured with the following sections:",
        "1. Executive Summary: A brief overview of the procurement process and key findings.",
        "2. Introduction: An introduction to the purpose and scope of the report.",
        "3. Methodology: A description of the methods used to gather and compare prices.",
        "4. Findings: Detailed comparison of prices from different websites, including tables and charts.",
        "5. Analysis: An analysis of the findings, highlighting any significant trends or observations.",
        "6. Recommendations: Suggestions for procurement based on the analysis.",
        "7. Conclusion: A summary of the report and final thoughts.",
        "8. Appendices: Any additional information, such as raw data or supplementary materials.",
    ]),
    expected_output="A professional HTML page for the procurement report.",
    output_file=os.path.join(OUTPUT_DIR, "step_4_procurement_report.html"),
    agent=procurement_report_author_agent,
)