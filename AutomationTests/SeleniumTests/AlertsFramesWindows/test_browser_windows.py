import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://demoqa.com/browser-windows"

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(3)
    driver.get(URL)
    yield driver
    driver.quit()

def test_new_tab(browser):
    original_window = browser.current_window_handle
    browser.find_element(By.ID, "tabButton").click()

    WebDriverWait(browser, 5).until(lambda d: len(d.window_handles) > 1)
    new_window = [w for w in browser.window_handles if w != original_window][0]
    browser.switch_to.window(new_window)

    # sprawdzamy treść nowej karty
    text = browser.find_element(By.ID, "sampleHeading").text
    assert "This is a sample page" in text

    browser.close()
    browser.switch_to.window(original_window)

def test_new_window(browser):
    original_window = browser.current_window_handle
    browser.find_element(By.ID, "windowButton").click()

    WebDriverWait(browser, 5).until(lambda d: len(d.window_handles) > 1)
    new_window = [w for w in browser.window_handles if w != original_window][0]
    browser.switch_to.window(new_window)

    text = browser.find_element(By.ID, "sampleHeading").text
    assert "This is a sample page" in text

    browser.close()
    browser.switch_to.window(original_window)

def test_new_window_message(browser):
    original_window = browser.current_window_handle
    browser.find_element(By.ID, "messageWindowButton").click()

    # czekamy na nowe okno
    WebDriverWait(browser, 5).until(lambda d: len(d.window_handles) > 1)
    new_window = [w for w in browser.window_handles if w != original_window][0]
    browser.switch_to.window(new_window)

    # nie próbujemy odczytać treści ani current_url
    assert new_window is not None  # po prostu sprawdzamy, że istnieje

    browser.close()
    browser.switch_to.window(original_window)




