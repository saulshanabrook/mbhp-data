from playwright.sync_api import sync_playwright, expect
import json

with sync_playwright() as p:
    browser = p.chromium.launch()
    context = browser.new_context()

    # Start tracing before creating / navigating a page.
    # context.tracing.start(screenshots=True, snapshots=True, sources=True)

    page = context.new_page()
    print("Going...")
    page.goto("https://www.masspartnership.com/member/FindBHProvider.aspx")
    print("Clicking...")
    page.get_by_role("button", name="Search", exact=True).click()

    print("Finding...")

    prev_state = None
    with open("data.jsonl", "w") as outfile:
        while True:
            new_state = page.locator("#MainContent_FindBHProvider1_lblPageMsg")
            if prev_state:
                expect(new_state).not_to_have_text(prev_state)
            prev_state = new_state.text_content()
            print(prev_state)
            print(
                json.dumps(
                    page.locator("#MainContent_FindBHProvider1_DataList1").inner_html()
                ),
                file=outfile,
            )

            try:
                page.get_by_role("button", name="Next Page", exact=True).click()
            except Exception:
                break

    browser.close()
