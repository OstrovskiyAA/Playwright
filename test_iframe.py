import time

from playwright.sync_api import Page, expect

def test_iframe(page:Page):
    page.goto("https://www.qa-practice.com/elements/iframe/iframe_page")
    page.frame_locator("iframe").locator(".navbar-toggler-icon").click()
    expect(page.frame_locator("iframe").locator(".text-white").first).to_have_text("About")

def test_select(page:Page):
    page.goto("https://magento.softwaretestingboard.com/men/tops-men/jackets-men.html")
    page.locator("#sorter").first.select_option("price")
    time.sleep(3)
    expect(page.locator(".product-item-name").first).to_have_text("Beaumont Summit Kit ")