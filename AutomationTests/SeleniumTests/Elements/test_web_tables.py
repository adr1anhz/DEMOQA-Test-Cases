import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

URL = "https://demoqa.com/webtables"

# buttony id
add = "addNewRecordButton"
firstname = "firstName"
lastname = "lastName"
email = "userEmail"
age = "age"
salary = "salary"
department = "department"
submit = "submit"


# wartosci
wartosci = ["Adrian", "Adrianowski", "23", "adrian@mail.com", "5000", "QA"]



@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.implicitly_wait(3)
    browser.get(URL)
    yield browser
    browser.quit()


def test_web_tables(browser):
    # Add przycisk
    add_button = browser.find_element(By.ID, add)
    add_button.click()
    check_click = browser.find_element(By.ID, firstname)
    assert check_click.is_displayed(), "Nie kliknelo add lub nie widac pola"

    # firstname
    firstname_button = browser.find_element(By.ID, firstname)
    firstname_button.send_keys("Adrian")

    # lastname
    lastname_button = browser.find_element(By.ID, lastname)
    lastname_button.send_keys("Adrianowski")

    # email
    email_button = browser.find_element(By.ID, email)
    email_button.send_keys("adrian@mail.com")

    # age
    age_button = browser.find_element(By.ID, age)
    age_button.send_keys("23")

    # salary
    salary_button = browser.find_element(By.ID, salary)
    salary_button.send_keys("5000")

    # salary
    department_button = browser.find_element(By.ID, department)
    department_button.send_keys("QA")

    # submit
    submit_button = browser.find_element(By.ID, submit)
    submit_button.click()

    # sleep + screenshot
    time.sleep(2)
    browser.save_screenshot("screenshots/web_tables.png")


    rows = browser.find_elements(By.CSS_SELECTOR, ".rt-tr-group .rt-tr")

    # szukamy wiersza z "Adrian"
    matching_row = None
    for row in rows:
        cells = row.find_elements(By.CSS_SELECTOR, ".rt-td")
        if len(cells) < 6:
            continue
        if cells[0].text == "Adrian":  # pierwsza kolumna = imię
            matching_row = cells
            break

    assert matching_row is not None, "Nie znaleziono wiersza z imieniem Adrian"

    # szukanie kolumn z "wartosci"
    for cell, expected in zip(matching_row, wartosci):
        assert cell.text == expected, f"Szukalismy '{expected}', a jest '{cell.text}'"


