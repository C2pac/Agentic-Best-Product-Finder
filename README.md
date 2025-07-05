🧠 AI Procurement Agent: Blender Sourcing System for Morocco
An intelligent multi-agent system powered by CrewAI to help Rankyx, an AI solutions company, source the best blenders in Morocco. The system generates targeted search queries, searches e-commerce sites, scrapes product details, and produces a professional procurement report, all optimized for value-for-price in the Moroccan market.

🚀 Features

🧠 Multi-Agent Workflow: Orchestrates four specialized agents for seamless procurement.
🔍 Smart Search Queries: Generates precise search queries for blenders, focusing on specific brands and features.
🌐 E-commerce Search: Targets Moroccan online stores like Jumia, Amazon, and Noon for relevant products.
📊 Detailed Scraping: Extracts key product details (price, specs, discounts) from e-commerce pages.
📝 Professional Reports: Outputs a polished HTML procurement report using Bootstrap for easy decision-making.
🧩 Modular Design: Organized code structure for easy customization and maintenance.
🔒 Secure Setup: API keys stored securely in a .env file, ignored by Git.

📌 Use Case
Rankyx needs to procure high-quality blenders for its office in Morocco, prioritizing value for price. This system automates the process by:

Generating search queries for blenders (e.g., "Philips 700W blender Morocco").
Searching trusted Moroccan e-commerce sites.
Scraping product details like price, specs, and discounts.
Producing a professional HTML report with price comparisons and recommendations.

💡 How It Works
The system leverages CrewAI to coordinate four agents, each with a specific role:

Search Queries Agent: Crafts up to 10 targeted search queries based on the product (blender) and country (Morocco).
Search Engine Agent: Searches e-commerce sites like Jumia Morocco, Amazon, and Noon, filtering out irrelevant results.
Scraping Agent: Extracts detailed product info (e.g., price, wattage, capacity) from product pages.
Report Author Agent: Generates a professional HTML procurement report with sections like Executive Summary, Findings, and Recommendations.

Project Flowchart
graph TD
    A[User Input: Blender, Morocco] --> B[Search Queries Agent]
    B --> C[Search Engine Agent]
    C --> D[Scraping Agent]
    D --> E[Report Author Agent]
    E --> F[HTML Procurement Report]

🛠️ Tech Stack



Tool
Purpose



Python
Core programming language


CrewAI
Multi-agent orchestration and task flow


OpenRouter (Gemini 2.0 Flash)
Large Language Model for content generation and analysis


Tavily API
Real-time web search for e-commerce products


ScrapeGraph
Smart web scraping for product details


AgentOps
Monitoring and debugging agent interactions


Bootstrap
Styling for professional HTML procurement reports


python-dotenv
Secure management of API keys


📸 Example Output
The system outputs the following files in the ai-agent-output/ directory:

step_1_suggested_search_queries.json: List of search queries (e.g., "Moulinex 500W blender Morocco").
step_2_search_results.json: E-commerce search results with URLs and scores.
step_3_search_results.json: Scraped product details (prices, specs, etc.).
step_4_procurement_report.html: A professional report with price comparisons and recommendations.

Example HTML report screenshot (placeholder):
🛠️ Setup Instructions
Prerequisites

Python 11.+
Git
API Keys:
OpenRouter API Key
AgentOps API Key
Tavily API Key
ScrapeGraph API Key



Installation

Clone the Repository:
git clone https://github.com/C2pac/Agentic-Best-Product-Finder.git
cd ai-agent-project


Create a Virtual Environment:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install Dependencies:
pip install -r requirements.txt


Set Up Environment Variables:

Create a .env file in the project root:
    OPENROUTER_API_KEY=your_openrouter_api_key_here
    AGENTOPS_API_KEY=your_agentops_api_key_here
    TVLY_API_KEY=your_tavily_api_key_here
    SCRAPEGRAPH_API_KEY=your_scrapegraph_api_key_here


Replace placeholders with your actual API keys.


Run the Project:
python src/main.py


View Outputs:

Check the ai-agent-output/ directory for JSON and HTML files.
Open step_4_procurement_report.html in a browser to view the report.



📂 Project Structure
ai-agent-project/
├── src/
│   ├── __init__.py
│   ├── config.py          # API keys, LLM, and client setup
│   ├── agents.py          # Agent definitions and tools
│   ├── tasks.py           # Task definitions
│   └── main.py            # Main execution script
├── .env                   # API keys (not tracked by Git)
├── .gitignore             # Excludes sensitive files
├── requirements.txt        # Project dependencies
├── ai-agent-output/       # Output files (JSON, HTML)
└── README.md              # Project documentation

🎯 Usage Example
Run the project with the default inputs to source blenders in Morocco:
python src/main.py

Input Example (defined in main.py):

Product: Blender for the office
Country: Morocco
Websites: www.jumia.ma, www.amazon.com, www.noon.com
Language: English
Max Queries: 10
Top Recommendations: 10

Output:

A professional HTML report comparing blenders from Moroccan e-commerce sites, with prices, specs, and recommendations.

💡 Tips for Customization

Change Product: Edit product_name in src/main.py (e.g., "laptop for office").
Add Websites: Update websites_list in src/main.py with other Moroccan e-commerce sites.
Enhance Report: Modify tasks.py to add custom Bootstrap components (e.g., charts, modals).
Debugging: Use VSCode's Python extension to set breakpoints in main.py.

🙋‍♀️ Author
Mohamed Chakor — Data Scientist & AI Developer
Connect with me on LinkedIn or open an issue on GitHub for questions!


⭐ Star this repo if you find it useful! Contributions and feedback are welcome! 🚀