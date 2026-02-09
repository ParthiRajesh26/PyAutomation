

---
## Feature: Negative Login Test Case for Invalid Credentials

### Project Overview
This repository automates the login functionality and negative test scenarios for OrangeHRM using Selenium WebDriver and pytest. The project is designed for robust, scalable, and maintainable test automation.

### Technology/Framework Used
- Python 3.10
- Selenium WebDriver
- pytest
- pytest-html (for test reports)
- webdriver-manager
- GitHub Actions (CI)

### Change Implemented
- Added a negative login test case to validate system behavior for invalid credentials. Ensures the application rejects unauthorized access and displays an appropriate error message.

### Where the Change Was Made
- `tests/test_login.py`: Added `test_login_invalid_credentials` function using the existing login utility.
- CI workflow (`.github/workflows/selenium.yml`) automatically includes all tests in `tests/`.

### Setup/Installation Steps
1. Clone the repository:
   ```
   git clone https://github.com/ParthiRajesh26/PyAutomation.git
   cd PyAutomation
   ```
2. Install dependencies:
   ```
   pip install selenium pytest pytest-html webdriver-manager
   ```

### Dependencies Required
- Python 3.10+
- selenium
- pytest
- pytest-html
- webdriver-manager

### How to Run the Tests
Run all tests:
```
pytest tests/ --html=report.html --self-contained-html
```
Run only the negative login test:
```
pytest tests/test_login.py -k test_login_invalid_credentials
```

### Example Run Command
```
pytest tests/test_login.py -k test_login_invalid_credentials --html=neg_report.html --self-contained-html
```

### Expected Behaviour/Output
- The negative login test (`test_login_invalid_credentials`) attempts login with invalid credentials.
- Test should fail the login attempt, assert an error message is displayed, and confirm no dashboard access.
- Example assertion: error message contains "Invalid credentials".
- Test result is reported in the console and HTML report.

### Troubleshooting Guide
- **Selector mismatch:** Update XPATH locators in `tests/test_login.py` if the OrangeHRM UI changes.
- **No error message displayed:** Verify the error message locator matches the application's current UI.
- **CI failures:** Check GitHub Actions logs for missing dependencies or browser issues.
- **WebDriver errors:** Ensure latest Chrome and ChromeDriver are installed or use `webdriver-manager`.

### Maintenance Procedures
- Periodically review and update test selectors and expected error messages.
- Expand negative test coverage for additional invalid login scenarios (e.g., empty fields, SQL injection attempts).
- Keep dependencies up to date.

### Recommendations for Future Improvements
- Parameterize invalid login tests for broader coverage.
- Integrate test result reporting with dashboards.
- Use fixtures for browser/session setup and teardown.
- Schedule regular test and documentation reviews.

---
