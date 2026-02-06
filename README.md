# PyAutomation

## Overview
PyAutomation is an automated test suite for validating the login functionality of OrangeHRM using Selenium and pytest. It provides both positive and negative test cases to ensure robust authentication logic.

## Test Coverage

### Positive Login Test
- **File:** `tests/test_login.py`
- **Test:** `test_orangehrm_login`
- **Purpose:** Verifies that a user with valid credentials can successfully log in and access the dashboard.
- **Expected Result:** User is redirected to the dashboard and the dashboard header is visible.

### Negative Login Test (Invalid Credentials)
- **File:** `tests/test_login.py`
- **Test:** `test_login_invalid_credentials`
- **Purpose:** Ensures that the system correctly rejects login attempts with invalid credentials.
- **Expected Result:** The login attempt fails, and an error message ("Invalid credentials") is displayed. User is not redirected to the dashboard.

## How to Run the Tests

1. **Install Dependencies:**
    ```sh
    pip install selenium pytest pytest-html webdriver-manager
    ```
2. **Run Tests:**
    ```sh
    pytest tests/ --html=report.html --self-contained-html
    ```
3. **View Results:**
    - Open `report.html` in your browser for a full test report.

## Continuous Integration
- All tests in the `tests/` directory are automatically run via GitHub Actions on push and pull request events.
- The workflow is defined in `.github/workflows/selenium.yml`.

## Troubleshooting
- **Webdriver Issues:** Ensure ChromeDriver is compatible with your Chrome browser version. The suite uses `webdriver-manager` for automatic driver management.
- **Test Failures:**
    - For negative test failures, check that invalid credentials are not valid for the test environment.
    - For CI issues, confirm that test file and function names follow `pytest` conventions.
- **Timeouts:** If tests fail due to timeouts, verify network connectivity and increase `TIMEOUT` in the test class if necessary.

## Contribution & Future Improvements
- Extend negative tests to cover scenarios like locked accounts, expired passwords, or SQL injection attempts.
- Review and update tests as the login page or logic evolves.
- Suggestions and pull requests are welcome!
