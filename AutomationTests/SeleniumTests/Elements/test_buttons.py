import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time

URL = "https://demoqa.com/buttons"

# BUTTONY
doubleclick = "doubleClickBtn"
rightclick = "rightClickBtn"
click = "Tf0Ef"


@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.implicitly_wait(3)
    browser.get(URL)
    yield browser
    browser.quit()


def test_buttons(browser):
    # doubleclickme
    doubleclickme = browser.find_element(By.ID, doubleclick)
    action = ActionChains(browser)
    action.double_click(doubleclickme).perform()
    time.sleep(2)
    sprawdz_doubleclickme = browser.find_element(By.ID, "doubleClickMessage")
    assert sprawdz_doubleclickme.is_displayed(), "Brak double-click-message"
    assert "You have done a double click" in sprawdz_doubleclickme.text, "Nie odpowiedni tekst"


    # rightclickme
    rightclickme = browser.find_element(By.ID, rightclick)
    action = ActionChains(browser)
    action.context_click(rightclickme).perform()
    time.sleep(2)
    sprawdz_rightclickme = browser.find_element(By.ID, "rightClickMessage")
    assert sprawdz_rightclickme.is_displayed(), "Brak right-click-message"
    assert "You have done a right click" in sprawdz_rightclickme.text, "Nie odpowiedni tekst"


    # tutaj musimy uzyc xpatha, (id jest zmienne a klasa nie jest unikal;na)
    clickme = browser.find_element(By.XPATH, "//button[text()='Click Me']")
    clickme.click()
    time.sleep(2) #WedDriverWait jest lepsze w tej sytuacji i bardziej pewne
    sprawdz_clickme = browser.find_element(By.ID, "dynamicClickMessage")
    assert sprawdz_clickme.is_displayed(), "Brak click-message"
    assert "You have done a dynamic click" in sprawdz_clickme.text, "Nie odpowiedni tekst"


    #screenshot
    browser.save_screenshot("screenshots/buttons.png")

