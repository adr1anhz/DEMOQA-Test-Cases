import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

URL = "https://demoqa.com/radio-button"


@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.implicitly_wait(3)
    browser.get(URL)
    yield browser
    browser.quit()


def test_check_box(browser):
    yes_button = browser.find_element(By.CSS_SELECTOR, "label[for='yesRadio']")
    yes_button.click()
    summary_section_yes = browser.find_element(By.CSS_SELECTOR, "p.mt-3")
    assert summary_section_yes.is_displayed(), "Brak podsumowania"
    assert "Yes" in summary_section_yes.text, "Brakuje yes w podsumowaniu"
    time.sleep(1)
    browser.save_screenshot("screenshots/radio_button_yes.png")

    impressive_button = browser.find_element(By.CSS_SELECTOR, "label[for='impressiveRadio']")
    impressive_button.click()
    summary_section_impressive = browser.find_element(By.CSS_SELECTOR, "p.mt-3")
    assert summary_section_impressive.is_displayed(), "Brak podsumowania"
    assert "Impressive" in summary_section_impressive.text, "Brakuje Impressive w podsumowaniu"
    time.sleep(1)
    browser.save_screenshot("screenshots/radio_button_impressive.png")

    # <p class="mt-3">You have selected <span class="text-success">Yes</span></p>



