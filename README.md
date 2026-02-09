
---
## Feature: Negative Login Test Case for Invalid Credentials

- **Project Overview:**
  This repository automates testing of the OrangeHRM login functionality using Selenium and pytest. It now includes a negative test case to verify that invalid credentials are properly rejected.

- **Technology/framework used:**
  Python, Selenium WebDriver, pytest, GitHub Actions CI

- **Change implemented:**
  Added a negative login test case (`test_login_invalid_credentials`) to ensure the application displays an error and prevents access when invalid credentials are used.

- **Where the change was made:**
  - `tests/test_login.py`: Added `test_login_invalid_credentials` function
  - Branch: `feature/negative-login-invalid-credentials`

- **Setup/installation steps:**
  1. Install dependencies:
     ```bash
     pip install selenium pytest
     ```
  2. Ensure ChromeDriver is installed and available in PATH.

- **Dependencies required:**
  - selenium
  - pytest
  - ChromeDriver

- **How to run the tests:**
  Run all tests (including the negative login test) with:
  ```bash
  pytest tests/
  ```
  Or run only the login tests:
  ```bash
  pytest tests/test_login.py
  ```

- **Example run command:**
  ```bash
  pytest -k test_login_invalid_credentials tests/test_login.py
  ```

- **Expected behaviour/output:**
  The negative login test attempts to log in with username `invalid_user` and password `wrong_pass`. The test will pass if the application displays an error message containing "Invalid credentials" and does not allow login.

  Example output:
  ```
  ============================= test session =============================
  tests/test_login.py::test_login_invalid_credentials PASSED
  ```

- **CI Integration:**
  The GitHub Actions workflow (`.github/workflows/selenium.yml`) will run all tests in `tests/`, including the new negative login test case.

- **Troubleshooting Guide:**
  - If the test fails due to element not found, verify selectors in `tests/test_login.py` and ensure the OrangeHRM login page has not changed.
  - If error message assertion fails, check the actual error text and update the test if the application changes its error messaging.
  - If ChromeDriver is not found, ensure it is installed and accessible from your PATH.
  - If tests are not discovered by pytest, ensure test function names start with `test_` and are located in the `tests/` directory.

- **Maintenance Procedures:**
  - If the login page changes (e.g., new selectors, error message format), update the locators and assertions in the test function.
  - Periodically review test coverage for login scenarios, and add additional negative cases as needed (e.g., locked account, SQL injection attempts).
  - Document any updates or issues in this section for future contributors.

- **Knowledge Transfer:**
  New contributors should review this section for guidance on adding or maintaining negative login tests. Follow pytest and Selenium best practices, and reference the utility function `login_with_credentials` for consistent test logic.
