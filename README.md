# PyAutomation

PyAutomation is a Python-based automation and testing framework utilizing Selenium and pytest for robust web application testing.

## Features
- Automates login functionality for OrangeHRM
- Includes both positive and negative test cases
- Headless browser execution for CI environments
- HTML test reports via pytest-html

## Test Cases

### Positive Login Test
Validates that users can log in with correct credentials and are redirected to the dashboard.
- **Test Function:** `test_orangehrm_login`
- **Expected Result:** User is redirected to the dashboard page and dashboard header is visible.

### Negative Login Test Case
The framework includes a test (`test_login_invalid_credentials`) to verify that login attempts with invalid credentials are correctly rejected. This ensures robust authentication handling and prevents unauthorized access.
- **Test Function:** `test_login_invalid_credentials`
- **Steps:**
  1. Navigate to the login page.
  2. Enter invalid username and/or password.
  3. Click on Login button.
  4. Validate error message is displayed and login fails.
- **Expected Result:** Login should fail and an appropriate error message should be shown.

## Running the Tests

1. Install dependencies:
   ```bash
   pip install selenium pytest pytest-html webdriver-manager
   ```

2. Run all tests:
   ```bash
   pytest tests/ --html=report.html --self-contained-html
   ```

## Continuous Integration
All tests in `tests/` are executed automatically via GitHub Actions CI workflow defined in `.github/workflows/selenium.yml`.

## Troubleshooting Guide
- **Test not detected:** Ensure test function names start with `test_`.
- **Selenium WebDriver errors:** Verify that ChromeDriver is compatible with your local Chrome version or use `webdriver-manager` as shown.
- **Login test failures:**
  - For invalid credential test: Confirm the error message locator is correct and the application returns an error for bad credentials.
  - For valid login test: Ensure demo credentials are unchanged and OrangeHRM is accessible.

## Maintenance Guide
- To add more negative test scenarios (e.g., empty fields, SQL injection), duplicate the structure of `test_login_invalid_credentials`.
- Update locators and expected results as needed if the application UI changes.

## Contribution
Contributions are welcome! Please ensure new tests are robust, well-documented, and follow pytest conventions.
