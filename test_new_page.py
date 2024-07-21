from playwright.sync_api import Page, BrowserContext

def test_tabs(page:Page, context:BrowserContext):
    page.goto("https://nomadlist.com/")
    with context.expect_page() as new_tab_event:
        page.get_by_alt_text("Get insured").click()
        new_tab = new_tab_event.value
    new_tab.get_by_role("button", name='Log in').click()