import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://demoqa.com/dynamic-properties"

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(3)
    driver.get(URL)
    yield driver
    driver.quit()

def test_enable_after_button(browser):
    btn = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.ID, "enableAfter"))
    )
    assert btn.is_enabled(), "Przycisk #enableAfter jest kliknięty"
    browser.save_screenshot("screenshots/dynamicproperties1.png")

def test_color_change_button(browser):
    btn = browser.find_element(By.ID, "colorChange")
    initial_color = btn.value_of_css_property("color")

    # czekamy, aż kolor się zmieni
    WebDriverWait(browser, 10).until(
        lambda d: btn.value_of_css_property("color") != initial_color
    )
    new_color = btn.value_of_css_property("color")
    assert new_color != initial_color, f"kolor nie zmienił się: {initial_color}"
    browser.save_screenshot("screenshots/dynamicproperties2.png")

def test_visible_after_button(browser):
    # przycisk ktory pojawia sie po 5 sekundach
    btn = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.ID, "visibleAfter"))
    )
    assert btn.is_displayed(), "Przycisk #visibleAfter jest widoczny"
    browser.save_screenshot("screenshots/dynamicproperties3.png")
