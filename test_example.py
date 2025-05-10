from playwright.sync_api import sync_playwright

def test_example_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        page.goto("https://example.com ")
        
        assert "Example Domain" in page.title(), f"Заголовок неожиданный: {page.title()}"
        print("Проверка заголовка прошла успешно.")
        
        more_info_button = page.locator("a:has-text('More information')")
        more_info_button.click()
        
        page.wait_for_url("https://www.iana.org/help/example-domains ")

        assert page.url == "https://www.iana.org/help/example-domains ", f"Переход на неожиданный URL: {page.url}"
        print("Перенаправление на страницу прошло успешно.")
        
        browser.close()

if __name__ == "__main__":
    test_example_page()
