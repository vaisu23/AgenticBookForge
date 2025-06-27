# AgenticBookForge

An end-to-end **automated book publication system** using AI agents, human-in-the-loop editing, and intelligent search capabilities via ChromaDB.

This project was developed for evaluation purposes and demonstrates seamless integration of AI rewriting, reviewing, editing, version control, and retrieval using agent-based modular components.

---

## 🚀 Features

- ✅ **Web Scraping & Screenshot**  
  Extract content from a chapter URL and capture a screenshot (via Playwright).

- ✅ **AI Writer (LLM)**  
  Rewrites the chapter using an AI agent (Gemini/OpenAI).

- ✅ **AI Reviewer (LLM)**  
  Polishes grammar, clarity, and coherence of AI-written content.

- ✅ **Human-in-the-Loop Editing**  
  Final editing via a user-friendly UI (Flask or Streamlit).

- ✅ **Versioning with ChromaDB**  
  Stores each final version with metadata and embeddings for smart retrieval.

- ✅ **RL-Style Search Interface**  
  Streamlit-powered search using natural language queries to retrieve relevant versions.

---

## 📁 Directory Structure

├── nmain.py # Main pipeline execution

├── scrape.py # Playwright scraper

├── ai_writer.py # AI spinning agent

├── ai_reviewer.py # AI review agent

├── interface.py # Flask UI for human editing

├── chroma_handler.py # Versioning and ChromaDB logic

├── searchRL.py # Streamlit UI for RL-style query

├── output/ # Final text output

├── chroma_store/ # Persistent ChromaDB storage

└── README.md
