
---
## Feature: Negative Login Test Case for Invalid Credentials

- **Project Overview:**
  PyAutomation is a Python-based test automation project focused on validating web application login functionality using Selenium and pytest. It ensures robust quality assurance for OrangeHRM login workflows.

- **Technology/framework used:**
  - Python 3.x
  - Selenium WebDriver
  - pytest
  - GitHub Actions (CI)

- **Change implemented:**
  Added a negative test case (`test_login_invalid_credentials`) to verify that login attempts with invalid credentials fail as expected and display an appropriate error message.

- **Where the change was made:**
  - `tests/test_login.py`: New function `test_login_invalid_credentials` added.
  - Branch: `feature/negative-login-invalid-credentials`

- **Setup/installation steps:**
  1. Clone the repository:
     ```bash
     git clone https://github.com/ParthiRajesh26/PyAutomation.git
     ```
  2. Checkout the feature branch:
     ```bash
     git checkout feature/negative-login-invalid-credentials
     ```
  3. Install dependencies:
     ```bash
     pip install -r requirements.txt
     ```
  4. Ensure ChromeDriver is installed and available in your PATH.

- **Dependencies required:**
  - selenium
  - pytest
  - chromedriver (compatible with your Chrome version)

- **How to run the tests:**
  Execute all tests with pytest:
  ```bash
  pytest tests/
  ```
  Or run only the login tests:
  ```bash
  pytest -m login
  ```

- **Example run command:**
  ```bash
  pytest tests/test_login.py
  ```

- **Expected behaviour/output:**
  - The negative login test (`test_login_invalid_credentials`) should fail the login attempt using invalid credentials and assert that an error message is displayed.
  - Sample output:
    ```
    ============================= test session ==============================
    tests/test_login.py::test_login_invalid_credentials PASSED
    ```

- **Troubleshooting Guide:**
  - **Test not discovered:** Ensure test function name starts with `test_` and file is in `tests/` directory.
  - **Assertion failure:** Check that invalid credentials are used and error message locator is correct.
  - **Error message not displayed:** Verify that the application displays an error for failed login; update locator if application UI changes.
  - **CI does not execute new test:** Confirm `.github/workflows/selenium.yml` includes `tests/test_login.py` and pytest is used.

- **Maintenance Procedures & Recommendations:**
  - Periodically review negative login test cases for coverage and effectiveness.
  - Use pytest parameterization to cover multiple invalid credential scenarios.
  - Employ fixtures for test isolation and reliability.
  - Update credentials and error message locators as application evolves.
  - Expand negative tests to include edge cases (e.g., empty fields, SQL injection).

---
