from crewai import Crew, Process
from src.config import company_context
from src.agents import (
    search_queries_recommendation_agent, search_engine_agent, scraping_agent,
    procurement_report_author_agent
)
from src.tasks import (
    search_queries_recommendation_task, search_engine_task, scraping_task,
    procurement_report_author_task
)
import agentops

# Initialize AgentOps
agentops.init(
    api_key=os.getenv("AGENTOPS_API_KEY"),
    skip_auto_end_session=True,
    default_tags=['crewai']
)

# Define the Crew
rankyx_crew = Crew(
    agents=[
        search_queries_recommendation_agent,
        search_engine_agent,
        scraping_agent,
        procurement_report_author_agent,
    ],
    tasks=[
        search_queries_recommendation_task,
        search_engine_task,
        scraping_task,
        procurement_report_author_task,
    ],
    process=Process.sequential,
    knowledge_sources=[company_context]
)

# Run the Crew
if __name__ == "__main__":
    crew_results = rankyx_crew.kickoff(
        inputs={
            "product_name": "Blender for Smoothies",
            "websites_list": ["https://www.electroplanet.ma/", "https://www.jumia.ma/", "https://www.marjane.ma/"],
            "country_name": "morocco",
            "no_keywords": 10,
            "language": "English",
            "score_th": 0.50,
            "top_recommendations_no": 10
        }
    )
    print("Crew execution completed. Results saved in ai-agent-output/")
    agentops.end_session()