# PyAutomation

PyAutomation is an automation testing framework for validating the login functionality of the OrangeHRM demo application using Selenium and Pytest. It includes robust test cases for both positive and negative login scenarios and is configured for continuous integration (CI) with GitHub Actions.

## Features
- Automated login tests using Selenium WebDriver
- Positive and negative login test cases
- Utility functions for reusable login logic
- Headless browser execution for CI environments
- HTML test reports via pytest-html

## Test Coverage

### Login Tests

#### 1. Positive Login Test (`test_orangehrm_login`)
- **Purpose:** Verifies that a user can log in with valid credentials.
- **Steps:**
  1. Navigate to the login page.
  2. Enter valid username and password.
  3. Click the Login button.
  4. Assert that the user is redirected to the dashboard and the dashboard header is present.
- **Expected Result:** Successful login and dashboard is displayed.

#### 2. Negative Login Test (`test_login_invalid_credentials`)
- **Purpose:** Verifies that login fails with invalid credentials and an error message is shown.
- **Steps:**
  1. Navigate to the login page.
  2. Enter invalid username and password.
  3. Click the Login button.
  4. Assert that login fails and an error message is displayed.
- **Expected Result:** Login attempt fails and the user sees an error message.

## Running the Tests

### Prerequisites
- Python 3.10+
- Google Chrome browser

### Installation
```bash
pip install selenium pytest pytest-html webdriver-manager
```

### Execute Tests Locally
```bash
pytest tests/ --html=report.html --self-contained-html
```

### Continuous Integration
Tests are automatically executed via GitHub Actions on every push and pull request using the workflow defined in `.github/workflows/selenium.yml`. Test results are uploaded as an HTML report artifact.

## Troubleshooting Guide

| Issue                                  | Solution                                                                                  |
|----------------------------------------|-------------------------------------------------------------------------------------------|
| Test fails unexpectedly                | Verify that the login utility handles invalid credentials and check assertion logic.       |
| CI does not discover new test          | Ensure test file and function names follow `pytest` conventions and are in the `tests/` directory. |
| WebDriver errors (e.g., Chrome not found) | Ensure Chrome is installed and compatible with `webdriver-manager`.                        |
| Unclear error message for failed login | Check locator for error message; update test as needed.                                   |

## Maintenance
- Periodically review and update test cases for new login scenarios (e.g., edge cases, security tests).
- Update test logic and documentation if the OrangeHRM login flow changes.
- Encourage parameterization of login tests for maintainability and scalability.

## Contribution
Contributions are welcome! Please open issues or submit pull requests for enhancements and bug fixes.

## License
This project is licensed under the MIT License.
