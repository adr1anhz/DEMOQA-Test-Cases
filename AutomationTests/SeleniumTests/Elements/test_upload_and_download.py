import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

URL = "https://demoqa.com/upload-download"

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(3)
    driver.get(URL)
    yield driver
    driver.quit()


def test_file_upload(browser, tmp_path):
    # plik testowy temp
    file_path = tmp_path / "testowyplik.txt"
    file_path.write_text("Cześć DemoQA!")

    upload_input = browser.find_element(By.ID, "uploadFile")
    upload_input.send_keys(str(file_path))

    # sprawdzamy czy DemoQA pokazało nazwę pliku
    uploaded_text = browser.find_element(By.ID, "uploadedFilePath")
    assert "testowyplik.txt" in uploaded_text.text
    time.sleep(1)
    browser.save_screenshot("screenshots/uploadfile.png")


def test_file_download(browser):
    download_btn = browser.find_element(By.ID, "downloadButton")
    href = download_btn.get_attribute("href")

    assert (
        href.startswith("data:image/jpeg;base64,") or 
        href.startswith("data:image/png;base64,")
    ), f"Zly format pliku: {href[:30]}"
    time.sleep(1)
    browser.save_screenshot("screenshots/downloadfile.png")


