
from agents import (
    ScraperAgent,
    AIWriterAgent,
    AIReviewerAgent,
    HumanEditorAgent,
    ChromaStorageAgent
)

def run_pipeline():
    # Initialize agents
    scraper = ScraperAgent()
    writer = AIWriterAgent()
    reviewer = AIReviewerAgent()
    editor = HumanEditorAgent()
    storage = ChromaStorageAgent()

    print(" Running Agentic Pipeline...\n")

    raw_text = scraper.run()
    spun_text = writer.run(raw_text)
    reviewed_text = reviewer.run(spun_text)
    final_text = editor.run(reviewed_text)
    storage.run(final_text)

    print("\n Final version saved and persisted in ChromaDB.")

if __name__ == "__main__":
    run_pipeline()
