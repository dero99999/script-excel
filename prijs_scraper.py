# prijs_scraper.py
import sys
from playwright.sync_api import sync_playwright
import re

def extract_price(text):
    matches = re.findall(r"€\s?[0-9]+(?:[.,][0-9]{2})?", text)
    prijzen = [m for m in matches if float(m.replace("€", "").replace(",", ".").strip()) >= 5]
    return prijzen[0] if prijzen else "Prijs niet gevonden"

def main():
    url = sys.argv[1]

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url, timeout=60000)
        content = page.content()
        price = extract_price(content)
        print(price)
        browser.close()

if __name__ == "__main__":
    main()
