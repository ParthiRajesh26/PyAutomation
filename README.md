# PyAutomation

## Overview
PyAutomation is an automation testing project for the OrangeHRM demo application. It uses Selenium WebDriver with pytest for test automation and GitHub Actions for continuous integration.

## Test Suite
All tests are located in the `tests/` directory and are executed using pytest. The CI pipeline runs all tests automatically on push and pull requests.

### Login Tests
- **Positive Test:**
  - Validates successful login with correct credentials.
  - Location: `tests/test_login.py::test_orangehrm_login`

- **Negative Test:**
  - Validates system behavior when invalid credentials are provided.
  - Location: `tests/test_login.py::test_login_invalid_credentials`
  - **Purpose:** Ensures that authentication is robust and that users cannot log in with incorrect credentials.
  - **Steps:**
    1. Navigate to the login page.
    2. Enter an invalid username and/or password.
    3. Click the Login button.
    4. Assert that login fails and an error message is displayed.
  - **Expected Outcome:**
    - The login attempt should fail.
    - An error message (e.g., "Invalid credentials") should be visible on the page.

#### Troubleshooting Guide
- If the negative login test fails unexpectedly:
  - Ensure the error message locator is correct and the page structure has not changed.
  - Check for changes in the application's login error handling.
  - Confirm that the test uses clearly invalid credentials.
  - Review CI logs for Selenium/WebDriver issues.

#### Maintenance Instructions
- To add new negative login scenarios, parameterize the test or add new test functions in `tests/test_login.py`.
- Follow pytest naming conventions and keep negative tests isolated from positive ones.

## Continuous Integration
CI is managed via GitHub Actions (`.github/workflows/selenium.yml`). All tests in the `tests/` folder are executed automatically.

## Contact
For questions or maintenance, contact the repository owner or contributors via GitHub Issues.
