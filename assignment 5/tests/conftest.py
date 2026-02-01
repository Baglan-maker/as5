import pytest
import logging
import os
import base64
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Ensure logs directory exists
if not os.path.exists("logs"):
    os.makedirs("logs")


@pytest.fixture(scope="function")
def driver(request):
    logging.info(f"Starting Test: {request.node.name}")

    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()

    # Pass driver to test function
    yield driver

    # Teardown: Close browser
    logging.info(f"Finished Test: {request.node.name}")
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    extras = getattr(report, "extras", [])

    if report.when == "call" and report.failed:
        # Retrieve driver from the test fixture
        driver_fixture = item.funcargs.get('driver')
        if driver_fixture:
            # Capture screenshot as a base64 string directly
            screenshot_base64 = driver_fixture.get_screenshot_as_base64()

            logging.error("Test Failed! Embedding screenshot in report.")

            # Attach the base64 image to the report
            from pytest_html import extras
            html = f'<div><img src="data:image/png;base64,{screenshot_base64}" alt="screenshot" style="width:600px;height:auto;" onclick="window.open(this.src)" align="right"/></div>'
            report.extras = [extras.html(html)]