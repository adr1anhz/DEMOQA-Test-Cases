import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.implicitly_wait(3)
    browser.get("https://demoqa.com/text-box")
    yield browser
    browser.quit()


def test_fill_textbox(browser):
    fullname = browser.find_element(By.ID, "userName")
    fullname.send_keys("Adrian Kowalak")
    

    email = browser.find_element(By.ID, "userEmail")
    email.send_keys("przykladowymail@mail.com")


    current_address = browser.find_element(By.ID, "currentAddress")
    current_address.send_keys("porzeczkowa 10")


    permament_address = browser.find_element(By.ID, "permanentAddress")
    permament_address.send_keys("gwiezdna 15")

    
    submit_button = browser.find_element(By.ID, "submit")
    submit_button.click()

    time.sleep(2) # Dodany time.sleep by strona miała czas dać output i screenshot był poprawny

    browser.save_screenshot("screenshots/textbox_result.png")


    # Podsumowanie
    summary_section = browser.find_element(By.ID, "output")
    assert summary_section.is_displayed(), "Brak podsumowania"
    assert "Adrian Kowalak" in summary_section.text, "Brakuje Fullname w podsumowaniu"



