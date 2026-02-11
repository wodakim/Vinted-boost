from playwright.sync_api import sync_playwright
import os

def run():
    print("Starting visual verification...")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Load the file
        file_path = os.path.abspath("index.html")
        page.goto(f"file://{file_path}")

        # Wait for potential JS execution
        page.wait_for_timeout(1000)

        # Take screenshot of the full dashboard which includes the restored Tips and Spoons
        page.screenshot(path="verification/dashboard_fixed.png", full_page=True)
        print("Screenshot saved to verification/dashboard_fixed.png")

        # Also switch to Studio and take a screenshot to prove content there
        page.click('button[onclick="switchTab(\'studio\')"]')
        page.wait_for_timeout(500)
        page.screenshot(path="verification/studio_fixed.png")
        print("Screenshot saved to verification/studio_fixed.png")

        browser.close()

if __name__ == "__main__":
    run()
