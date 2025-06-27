
import uuid
from datetime import datetime
from scrape import scrape_and_screenshot
from ai_writter import rewrite_text
from ai_reviewer import review_text
from chroma_handler import store_version
from interface import launch_editor_ui

OUTPUT_FOLDER = "output"
URL = "https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1"

class ScraperAgent:
    def run(self):
        print(" Scraping content...")
        scrape_and_screenshot(URL, OUTPUT_FOLDER)
        with open(f"{OUTPUT_FOLDER}/chapter_text.txt", "r", encoding="utf-8") as f:
            return f.read()

class AIWriterAgent:
    def run(self, text):
        print(" AI Writer rewriting content...")
        return rewrite_text(text)

class AIReviewerAgent:
    def run(self, text):
        print(" AI Reviewer refining content...")
        return review_text(text)

class HumanEditorAgent:
    def run(self, text):
        print(" Launching Human-in-the-loop editor...")
        return launch_editor_ui(text)

class ChromaStorageAgent:
    def run(self, text):
        print(" Storing final version in ChromaDB...")
        metadata = {
            "id": str(uuid.uuid4()),
            "version": 1,
            "editor": "Human/Auto",
            "timestamp": datetime.now().isoformat(),
            "source_url": URL
        }
        store_version(text, metadata)
