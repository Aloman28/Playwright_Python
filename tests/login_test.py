from playwright.sync_api import Page, expect
from pages.login_page import LoginPage


def test_successful_login(page: Page):
    loginPage = LoginPage(page)

    loginPage.navigate()
    loginPage.login("standard_user", "secret_sauce")

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    expect(loginPage.productPage).to_be_visible()