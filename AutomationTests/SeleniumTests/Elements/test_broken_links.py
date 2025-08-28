import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://demoqa.com/broken"

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(3)
    driver.get(URL)
    yield driver
    driver.quit()


def test_valid_image(browser):
    """ 
    Tu musimy sprawdzać po szerokości i na tej podstawie stwierdzić,
    czy załadował się obrazek czy nie
    """
    # Valid image = 347x100px
    img = browser.find_element(By.XPATH, "//p[text()='Valid image']/following-sibling::img")
    width = browser.execute_script("return arguments[0].naturalWidth;", img)
    assert width > 0, "Valid image NIE załadował się poprawnie"


def test_broken_image(browser):
    # Broken image = 16x16px
    img = browser.find_element(By.XPATH, "//p[text()='Broken image']/following-sibling::img")
    width = browser.execute_script("return arguments[0].naturalWidth;", img)
    assert width == 0, "Broken image POWINIEN być uszkodzony"


def test_valid_link(browser):
    old_url = browser.current_url

    link = browser.find_element(By.LINK_TEXT, "Click Here for Valid Link")
    link.click()

    # czekamy aż adres się zmieni
    WebDriverWait(browser, 5).until(EC.url_changes(old_url))

    # sprawdzamy nowy adres
    assert "demoqa.com" in browser.current_url


def test_broken_link(browser):
    link = browser.find_element(By.LINK_TEXT, "Click Here for Broken Link")
    link.click()


    WebDriverWait(browser, 5).until(EC.url_contains("500"))

    assert "500" in browser.current_url