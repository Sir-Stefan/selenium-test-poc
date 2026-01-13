from utils.driver_factory import create_driver
from pages.example_page import ExamplePage

def test_example_page_content():
    driver = create_driver()
    page = ExamplePage(driver)

    try:
        page.open()

        assert "Example Domain" in page.get_header_text()
        assert "illustrative examples" in page.get_paragraph_text()

    finally:
        driver.quit()
