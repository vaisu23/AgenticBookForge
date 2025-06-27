
from playwright.sync_api import sync_playwright
from pathlib import Path

def scrape_and_screenshot(url, output_folder="output"):
    Path(output_folder).mkdir(exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)

        # Save screenshot
        page.screenshot(path=f"{output_folder}/chapter_screenshot.png", full_page=True)

        # Save text
        content = page.text_content("body")
        with open(f"{output_folder}/chapter_text.txt", "w", encoding="utf-8") as f:
            f.write(content)

        browser.close()

print(" Scraper ready")
