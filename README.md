# 📧 Cold Mail Generator for Service Companies

An AI-powered cold email generation platform built using [Ollama](https://ollama.com?utm_source=chatgpt.com), [LangChain](https://www.langchain.com?utm_source=chatgpt.com), and [Streamlit](https://streamlit.io?utm_source=chatgpt.com).

This application allows service-based companies to generate highly personalized cold emails by simply providing the URL of a company’s careers page.

The system automatically:

* Extracts job listings from the careers page
* Understands hiring requirements using LLMs
* Searches a vector database for relevant portfolio projects
* Generates tailored outreach emails for business development teams

---

# 🚀 Use Case

Imagine the following scenario:

* Nike is hiring a **Principal Software Engineer**
* The hiring process involves:

  * sourcing candidates
  * onboarding
  * training
  * operational overhead

Meanwhile:

* Atliq provides dedicated software engineering talent and development services.

A business development executive from Atliq wants to reach out to Nike with a personalized cold email offering engineering services aligned with Nike’s hiring needs.

Instead of manually writing emails, this platform automates the entire workflow.

---

# ✨ Features

* Paste a company careers page URL
* Automatically scrape and extract job listings
* AI-powered understanding of job requirements
* Semantic portfolio matching using vector databases
* Personalized cold email generation
* Local LLM support using Ollama
* Interactive UI with Streamlit
* Retrieval-Augmented Generation (RAG) pipeline

---

# 🏗️ System Architecture

## Workflow

```text
User Inputs Careers Page URL
            ↓
Web Scraper Extracts Job Listings
            ↓
Job Descriptions Processed by LLM
            ↓
Relevant Portfolio Links Retrieved from Vector DB
            ↓
Personalized Cold Email Generated
            ↓
Displayed in Streamlit UI
```

---

# 🧠 Tech Stack

## Frontend

* [Streamlit](https://streamlit.io?utm_source=chatgpt.com)

## LLM Framework

* [LangChain](https://www.langchain.com?utm_source=chatgpt.com)

## Local LLM Runtime

* [Ollama](https://ollama.com?utm_source=chatgpt.com)

## Embeddings & Retrieval

* Vector Database (ChromaDB / FAISS)
* Semantic Search
* Retrieval-Augmented Generation (RAG)

## Backend Utilities

* Python
* BeautifulSoup / Web Scraping
* Environment Variable Management

---

# 📂 Project Structure

```text
project/
│
├── app/
│   ├── main.py
│   ├── chains/
│   ├── vectorstore/
│   ├── scraper/
│   └── utils/
│
├── portfolio/
├── requirements.txt
├── README.md
└── .env
```

---

# ⚙️ Installation & Setup

## 1. Clone the Repository

```bash
git clone <your-repository-url>
cd cold-email-generator
```

---

## 2. Create Virtual Environment (Recommended)

### Windows

```bash
python -m venv venv
venv\\Scripts\\activate
```

### macOS/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file inside the `app/` directory:

```env
GROQ_API_KEY=your_api_key_here
```

Get your API key from:

[Groq Console](https://console.groq.com/keys?utm_source=chatgpt.com)

---

# ▶️ Run the Application

```bash
streamlit run app/main.py
```

The application will start locally and open in your browser.

---

# 📸 Screenshots

## Application UI

```text
[ Add your application screenshot here ]
```

## Architecture Diagram

```text
[ Add your architecture diagram here ]
```

---

# 🔍 How It Works

## Step 1 — Career Page Scraping

The user provides a company careers page URL.

Example:

```text
https://jobs.nike.com
```

The application extracts available job postings and job descriptions.

---

## Step 2 — Job Understanding

The extracted content is processed using an LLM to identify:

* required skills
* experience
* technologies
* business needs

---

## Step 3 — Semantic Portfolio Matching

Relevant portfolio projects are retrieved using embeddings and vector similarity search.

This ensures the generated email contains highly relevant project references.

---

## Step 4 — Personalized Email Generation

The LLM generates a cold outreach email tailored specifically to the target company and role.

Example outputs include:

* hiring assistance proposals
* dedicated engineering team offers
* software development service pitches

---

# 🧩 Example Workflow

```text
Input:
Nike Careers Page URL

Detected Role:
Principal Software Engineer

Retrieved Portfolio:
- AI Analytics Dashboard
- Enterprise ERP Platform
- Cloud Migration System

Generated Output:
Personalized cold outreach email
```

---

# 💡 Future Improvements

* Multi-company outreach campaigns
* CRM integrations
* LinkedIn profile enrichment
* Email personalization scoring
* AI-generated follow-up sequences
* Multi-agent workflow orchestration
* Email deliverability optimization
* Automated lead scraping

---

# 🛠️ Recommended Enhancements

You can further improve this project by integrating:

* [Qdrant](https://qdrant.tech?utm_source=chatgpt.com) for scalable vector search
* [LlamaIndex](https://www.llamaindex.ai?utm_source=chatgpt.com) for advanced retrieval pipelines
* [LangGraph](https://www.langchain.com/langgraph?utm_source=chatgpt.com) for agentic workflows
* [PostgreSQL](https://www.postgresql.org?utm_source=chatgpt.com) for structured storage

---

# 📚 Learning Outcomes

This project demonstrates practical implementation of:

* Large Language Models (LLMs)
* Retrieval-Augmented Generation (RAG)
* Semantic Search
* Vector Databases
* Prompt Engineering
* AI-Powered Automation
* Personalized Content Generation

---

# 📜 License

Copyright (C) Codebasics Inc. All rights reserved.

This project is licensed under the MIT License.

## Additional Terms

* Commercial usage is prohibited without prior written permission from the author.
* Attribution must be included in all copies or substantial portions of the software.

---

# 🙌 Acknowledgements

Special thanks to:

* [Codebasics](https://codebasics.io?utm_source=chatgpt.com)
* [LangChain](https://www.langchain.com?utm_source=chatgpt.com)
* [Ollama](https://ollama.com?utm_source=chatgpt.com)
* [Streamlit](https://streamlit.io?utm_source=chatgpt.com)

for providing the tools and ecosystem that made this project possible.
