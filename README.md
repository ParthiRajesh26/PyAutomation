

---
## Feature: Negative Login Test Case for Invalid Credentials

- **Project Overview:**
  PyAutomation is a Python-based automation and test framework for validating OrangeHRM login functionality using Selenium and pytest.

- **Technology/framework used:**
  Python 3.10, Selenium WebDriver, pytest, pytest-html, webdriver-manager, GitHub Actions CI

- **Change implemented:**
  Added a negative login test case (`test_login_invalid_credentials`) to verify that the system correctly handles invalid credentials and displays an error message.

- **Where the change was made:**
  - `tests/test_login.py`: Added `test_login_invalid_credentials` function.
  - `.github/workflows/selenium.yml`: CI already includes all tests in `tests/`.

- **Setup/installation steps:**
  1. Clone the repository.
     ```bash
     git clone https://github.com/ParthiRajesh26/PyAutomation.git
     cd PyAutomation
     ```
  2. Install dependencies.
     ```bash
     pip install selenium pytest pytest-html webdriver-manager
     ```

- **Dependencies required:**
  - selenium
  - pytest
  - pytest-html
  - webdriver-manager

- **How to run the tests:**
  ```bash
  pytest tests/ --html=report.html --self-contained-html
  ```

- **Example run command:**
  ```bash
  pytest tests/test_login.py --html=report.html --self-contained-html
  ```

- **Expected behaviour/output:**
  - Valid login: User is redirected to dashboard and dashboard header is visible.
  - Invalid login: Error message is displayed, user is NOT redirected to dashboard.
  - Test report is generated as `report.html`.

- **Troubleshooting Guide:**
  - **Error message not displayed:** The test asserts on login failure and checks for error message text. If not found, review selector and page structure.
  - **Test setup failures:** Ensure ChromeDriver is installed and compatible. Check Python and package versions.
  - **CI failures:** Validate `.github/workflows/selenium.yml` includes `pytest tests/` and dependencies are installed.
  - **Login succeeded unexpectedly:** Verify invalid credentials are not accepted and error message is configured in OrangeHRM.

- **Maintenance Procedures:**
  - To extend negative login tests, parameterize the test with multiple invalid credential scenarios.
  - Review test results in `report.html` and CI logs for failed logins.
  - Update selectors and error handling as OrangeHRM UI evolves.

- **Knowledge Transfer & Recommendations:**
  - The negative login test case is isolated and uses robust assertions for error handling.
  - Follow naming conventions and use constants for maintainability.
  - Recommend periodic review of test coverage and automation of additional negative scenarios.
  - Integrate analytics and reporting for failed logins in future enhancements.
