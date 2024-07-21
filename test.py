import time

from playwright.sync_api import Page, expect, Route
import re

def test_wiki(page: Page):
    page.goto('https://www.wikipedia.org/')
    page.get_by_role('link', name='Русский').click()
    # time.sleep(1)
    expect(page.get_by_text('Добро пожаловать в Википедию,')).to_be_visible()

def test_wiki_2(page:Page):
    page.goto('https://www.wikipedia.org/')
    page.get_by_role('link', name='Русский').click()
    page.get_by_role('link', name='Содержание').click()
    page.locator('#ca-talk').click()
    expect(page.locator('#firstHeading')).to_have_text('Обсуждение Википедии:Содержание')

def test_request_correct(page:Page):
    page.goto('https://gymlog.ru/profile/login/')
    page.locator('#email').fill("User422")
    page.locator('#password').fill("FzNgl6")
    page.get_by_role('button', name='Войти').click()

def test_request_incorrect(page:Page):
    page.goto('https://gymlog.ru/profile/login/')
    page.locator('#email').fill("User42")
    page.locator('#password').fill("FzNgl")
    page.get_by_role('button', name='Войти').click()
    expect(page.locator('.alert')).to_have_text("Неверно указана электронная почта, логин или пароль.")

def test_request_changed(page:Page):
    def change_request(route:Route):
        data = route.request.post_data
        if data:
            data = data.replace("User422", "iii")
        print(data)
        route.continue_(post_data=data)
    page.route(re.compile('profile/authenticate'), change_request)
    page.goto('https://gymlog.ru/profile/login/')
    page.locator('#email').fill("User422")
    page.locator('#password').fill("FzNgl6")
    page.get_by_role('button', name='Войти').click()
    expect(page.locator('.alert')).to_have_text("Неверно указана электронная почта, логин или пароль.")

def test_response_changed(page:Page):
    def change_response(route:Route):
        response = route.fetch()
        data = response.text()
        data = data.replace("User422", "Алексей")
        route.fulfill(response=response, body=data)
    page.route(re.compile('profile'), change_response)
    page.goto('https://gymlog.ru/profile/login/')
    page.locator('#email').fill("User422")
    page.locator('#password').fill("FzNgl6")
    page.get_by_role('button', name='Войти').click()
    page.get_by_role('link', name='Мои программы').click()
    time.sleep(5)
