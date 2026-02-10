
---
## Feature: Negative Login Test Case for Invalid Credentials

- Project Overview: This repository automates the login functionality for OrangeHRM using Selenium and pytest. The implemented feature introduces a negative test case to validate that the system correctly rejects invalid login attempts.

- Technology/framework used: Python, Selenium WebDriver, pytest, pytest-html, webdriver-manager

- Change implemented: Added a negative login test case (`test_login_invalid_credentials`) in `tests/test_login.py` to ensure invalid credentials are rejected and proper error messages are shown.

- Where the change was made:
  - `tests/test_login.py`: Added `test_login_invalid_credentials` function.
  - No CI workflow update required; `.github/workflows/selenium.yml` already runs all tests.

- Setup/installation steps:
  1. Clone the repository.
  2. Install dependencies: `pip install selenium pytest pytest-html webdriver-manager`
  3. Ensure Chrome browser and chromedriver are available (webdriver-manager handles driver installation).

- Dependencies required:
  - selenium
  - pytest
  - pytest-html
  - webdriver-manager

- How to run the tests:
  - Run all tests and generate HTML report:
    ```bash
    pytest tests/ --html=report.html --self-contained-html
    ```

- Example run command:
  ```bash
  pytest tests/test_login.py --html=report.html --self-contained-html
  ```

- Expected behaviour/output:
  - The `test_login_invalid_credentials` test should fail login with invalid credentials and assert that the error message 'Invalid credentials' is displayed.
  - All tests should pass for valid scenarios and fail for invalid login as expected.

---
### Troubleshooting Guide

- **Error message not found:**
  - If the error message selector changes, update `ERROR_MESSAGE_XPATH` in `OrangeHRMLoginTest`.
  - Ensure the login page is available and reachable.

- **Login page unavailable:**
  - Check network connectivity or OrangeHRM demo site status.
  - Add a skip marker in pytest if the site is down.

- **CI fails to discover test:**
  - Ensure tests are located in the `tests/` directory and follow pytest naming conventions (`test_*.py`).
  - `.github/workflows/selenium.yml` should use `pytest tests/`.

---
### Maintenance Procedures

- Periodically review negative test coverage and update as the login flow evolves.
- Update test and documentation if error messages, selectors, or login mechanisms change.
- Use pytest fixtures and parametrization for future negative test cases.

---
### Recommendations for Optimization and Future Improvements

- Parametrize negative login tests for multiple invalid scenarios.
- Use fixtures for test data management.
- Expand negative test cases to cover locked accounts, expired passwords, etc.
- Monitor CI logs for test failures and performance.
- Encourage modular and maintainable test design.
