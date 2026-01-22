import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SQAT_Assignment_Final:

    def run_tests(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        wait = WebDriverWait(driver, 10)

        try:
            # --- TASK 1: SEARCH ---
            print("Task 1: Search Functionality")
            driver.get("https://www.wikipedia.org/")
            wait.until(EC.element_to_be_clickable((By.ID, "searchInput"))).send_keys("Software Testing")
            driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
            wait.until(EC.presence_of_element_located((By.ID, "firstHeading")))
            print(f"PASS: Search successful -> {driver.title}")

            # --- TASK 2: LOGIN & LOGOUT ---
            print("\nTask 2: Login and Logout")
            driver.get("https://the-internet.herokuapp.com/login")

            wait.until(EC.visibility_of_element_located((By.ID, "username"))).send_keys("tomsmith")
            driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
            driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

            success_message = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".flash.success")))
            assert "You logged into a secure area!" in success_message.text
            print("PASS: Login Successful")

            logout_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.button.secondary")))

            driver.execute_script("arguments[0].click();", logout_btn)

            logout_message = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".flash.success")))
            assert "You logged out of the secure area!" in logout_message.text
            print("PASS: Logout Successful")

            # --- TASK 3: FLIGHT BOOKING ---
            print("\nTask 3: Flight Booking")
            driver.get("https://blazedemo.com/")

            from_select = Select(wait.until(EC.presence_of_element_located((By.NAME, "fromPort"))))
            from_select.select_by_value("Paris")
            Select(driver.find_element(By.NAME, "toPort")).select_by_value("London")
            driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

            wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@value='Choose This Flight'])[1]"))).click()

            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[value='Purchase Flight']"))).click()

            expected_title = "BlazeDemo Confirmation"
            wait.until(EC.title_is(expected_title))
            print(f"PASS: Flight Booking Title Checkpoint -> {driver.title}")

        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            print("\nClosing browser...")
            driver.quit()


if __name__ == "__main__":
    test = SQAT_Assignment_Final()
    test.run_tests()