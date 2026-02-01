import logging
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Constants
BASE_URL = "https://the-internet.herokuapp.com"
LOGIN_URL = f"{BASE_URL}/login"
CHECKBOX_URL = f"{BASE_URL}/checkboxes"


class TestHerokuApp:

    def test_valid_login(self, driver):
        """
        TC-01: Verify valid login functionality.
        """
        logging.info("Step 1: Navigate to Login Page")
        driver.get(LOGIN_URL)

        logging.info("Step 2: Enter Valid Username and Password")
        driver.find_element(By.ID, "username").send_keys("tomsmith")
        driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")

        logging.info("Step 3: Click Login Button")
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        logging.info("Step 4: Verify Success Message")
        flash_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "flash"))
        ).text

        if "You logged into a secure area" in flash_message:
            logging.info("Assertion Passed: User logged in successfully.")
        else:
            logging.error(f"Assertion Failed: Actual text was '{flash_message}'")

        assert "You logged into a secure area" in flash_message

    def test_invalid_login(self, driver):
        """
        TC-02: Verify invalid login functionality
        """
        logging.info("Step 1: Navigate to Login Page")
        driver.get(LOGIN_URL)

        logging.info("Step 2: Enter Invalid Credentials")
        driver.find_element(By.ID, "username").send_keys("wronguser")
        driver.find_element(By.ID, "password").send_keys("wrongpass")

        logging.info("Step 3: Click Login Button")
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        logging.info("Step 4: Verify Error Message")
        flash_message = driver.find_element(By.ID, "flash").text

        assert "Your username is invalid!" in flash_message
        logging.info("Assertion Passed: Error message displayed correctly.")

    def test_checkbox_selection(self, driver):
        """
        TC-03: Verify Checkbox functionality
        """
        logging.info("Step 1: Navigate to Checkboxes Page")
        driver.get(CHECKBOX_URL)

        # Locator for the first checkbox
        checkbox1 = driver.find_element(By.XPATH, "//form[@id='checkboxes']/input[1]")

        logging.info("Step 2: Check Checkbox 1 if not checked")
        if not checkbox1.is_selected():
            checkbox1.click()
            logging.info("Checkbox 1 clicked.")

        logging.info("Step 3: Verify Checkbox 1 is selected")
        assert checkbox1.is_selected() is True

    def test_force_failure_example(self, driver):
        """
        TC-04: Intentional Failure to demonstrate Screenshot capturing.
        """
        logging.info("Step 1: Navigate to Home")
        driver.get(BASE_URL)

        logging.info("Step 2: Assert Title (Intentional Fail)")
        # This will fail and trigger the screenshot hook in conftest.py
        assert driver.title == "Wrong Title"