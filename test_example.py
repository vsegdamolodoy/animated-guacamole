from playwright.sync_api import sync_playwright


def test_example_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://example.com ")

        assert "Example Domain" in page.title(), "Заголовок страницы не содержит 'Example'"
        print("Проверка заголовка успешна.")

        more_info_button = page.locator("a:has-text('More information')")
        more_info_button.click()

        assert page.url == "https://www.iana.org/help/example-domains ", "Перенаправление не произошло на ожидаемую страницу"
        print("Перенаправление успешно.")

        browser.close()


if __name__ == "__main__":
    test_example_page()