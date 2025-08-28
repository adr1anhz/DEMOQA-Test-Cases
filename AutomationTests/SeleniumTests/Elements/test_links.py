import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://demoqa.com/links"

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(3)
    driver.get(URL)
    yield driver
    driver.quit()


def test_link_open_new_tab(browser):
    """Testuje link otwierający nową zakładkę"""
    original_window = browser.current_window_handle

    home_link = browser.find_element(By.ID, "simpleLink")
    home_link.click()

    # czekamy na nowe okno
    WebDriverWait(browser, 5).until(EC.new_window_is_opened)

    all_windows = browser.window_handles
    new_window = [w for w in all_windows if w != original_window][0]

    browser.switch_to.window(new_window)

    # sprawdzamy URL
    assert "demoqa.com" in browser.current_url

    browser.close()
    browser.switch_to.window(original_window)


@pytest.mark.parametrize("link_id, expected_status", [
    ("created", "201"),
    ("no-content", "204"),
    ("moved", "301"),
    ("bad-request", "400"),
    ("unauthorized", "401"),
    ("forbidden", "403"),
    ("invalid-url", "404"),
])
def test_api_links(browser, link_id, expected_status):
    """Testuje linki zwracające statusy API"""
    link = browser.find_element(By.ID, link_id)
    link.click()

    response = WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.ID, "linkResponse"))
    )

    assert expected_status in response.text, f"Link {link_id} nie zwrócił {expected_status}, tylko: {response.text}"
