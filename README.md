Automation Testing Suite - Assignment 5
This repository contains an automated testing suite for the Herokuapp website. It is built using Python, Selenium, and the pytest framework. The project fulfills all requirements for test lifecycle management, logging, and reporting.

Features
Test Lifecycle Management: Implementation of setup and teardown using pytest fixtures to manage browser instances.

Logging Framework: Integrated Python logging that records test progress, success, and errors into a dedicated log file.

HTML Reporting: Generation of a detailed test report including execution summaries and results for each test case.

Screenshot Capture: Automatic capturing and embedding of screenshots into the HTML report upon any test failure.

Project Structure
assignment 5/tests/conftest.py: Contains the driver initialization and reporting hooks.

assignment 5/tests/test_herokuapp.py: Contains the functional test cases.

reports/report.html: The self contained HTML report generated after execution.

Requirements
Python 3.11 or higher

Selenium

pytest

pytest-html

webdriver-manager

Installation and Execution
Clone the repository to your local machine.

Install the necessary dependencies using the following command: pip install selenium pytest pytest-html webdriver-manager

Execute the test suite and generate the report using: pytest --html=reports/report.html --self-contained-html
