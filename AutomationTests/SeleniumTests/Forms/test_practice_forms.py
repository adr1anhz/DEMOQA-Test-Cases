import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

URL = "https://demoqa.com/automation-practice-form"

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(3)
    driver.get(URL)
    yield driver
    driver.quit()

def test_student_registration_form(browser, tmp_path):
    # Elementy
    browser.find_element(By.ID, "firstName").send_keys("Adrian")
    browser.find_element(By.ID, "lastName").send_keys("Adrianowski")
    browser.find_element(By.ID, "userEmail").send_keys("adrianowski@mail.com")
    browser.find_element(By.ID, "userNumber").send_keys("1234567890")
    browser.find_element(By.ID, "currentAddress").send_keys("ul. Porzeczkowa, Warszawa")
    
    # Płeć
    browser.find_element(By.XPATH, "//label[text()='Male']").click()
    
    # Data urodzenia klikamy
    dob_input = browser.find_element(By.ID, "dateOfBirthInput")
    dob_input.click()
    

    browser.find_element(By.CLASS_NAME, "react-datepicker__month-select").send_keys("March")
    browser.find_element(By.CLASS_NAME, "react-datepicker__year-select").send_keys("2002")
    day_17 = browser.find_element(
    By.XPATH,
        "//div[contains(@class,'react-datepicker__day') and text()='17' and not(contains(@class,'outside-month'))]"
    )
    day_17.click()

    
    # Subjects
    subjects_input = browser.find_element(By.ID, "subjectsInput")
    subjects_input.send_keys("Matematyka")
    subjects_input.send_keys("\n") # Tab tutaj mogliśmy użyć też entera
    
    # Hobbies
    browser.find_element(By.XPATH, "//label[text()='Sports']").click()
    browser.find_element(By.XPATH, "//label[text()='Reading']").click()
    
    # Wgrywamy plik poprzez tmp file
    file_path = tmp_path / "testowe.png"
    file_path.write_text("dummy content")  # testowy plik
    browser.find_element(By.ID, "uploadPicture").send_keys(str(file_path))
    
    # State i City
    browser.find_element(By.ID, "react-select-3-input").send_keys("NCR\n")
    browser.find_element(By.ID, "react-select-4-input").send_keys("Delhi\n")
    
    # Submit
    browser.find_element(By.ID, "submit").click()
    
    # Sprawdzenie pojawienia się modalnego okna
    modal = WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.ID, "example-modal-sizes-title-lg"))
    )
    assert modal.is_displayed(), "Modal powinien być widoczny po wysłaniu formularza"
