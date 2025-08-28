import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

URL = "https://demoqa.com/checkbox"


@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.implicitly_wait(3)
    browser.get(URL)
    yield browser
    browser.quit()


def test_check_box(browser):
    checkbox = browser.find_element(By.CSS_SELECTOR, "span.rct-checkbox")
    checkbox.click()


    time.sleep(2) # Dodany time.sleep by strona miała czas dać output i screenshot był poprawny

    browser.save_screenshot("screenshots/checkbox_result.png")


    # Podsumowanie
    summary_section = browser.find_element(By.ID, "result")
    assert summary_section.is_displayed(), "Brak podsumowania"
    assert "desktop" in summary_section.text, "Brakuje desktop w podsumowaniu"



