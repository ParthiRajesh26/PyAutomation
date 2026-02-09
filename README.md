
---
## Feature: Negative Login Test for Invalid Credentials

- Project Overview: This repository automates functional testing for OrangeHRM, focusing on login workflows and validation using Selenium and pytest.
- Technology/framework used: Python, Selenium, pytest, GitHub Actions CI
- Change implemented: Added a negative login test case to verify that the system correctly rejects invalid credentials and displays an error message.
- Where the change was made: tests/test_login.py (function: test_login_invalid_credentials)
- Setup/installation steps:
    1. Clone the repository: `git clone https://github.com/ParthiRajesh26/PyAutomation.git`
    2. Checkout the feature branch: `git checkout feature/negative-login-invalid-credentials`
    3. Install dependencies: `pip install selenium pytest pytest-html webdriver-manager`
- Dependencies required: selenium, pytest, pytest-html, webdriver-manager
- How to run the tests: `pytest tests/ --html=report.html --self-contained-html`
- Example run command:
    ```bash
    pytest tests/test_login.py --html=report.html --self-contained-html
    ```
- Expected behaviour/output:
    - Valid credentials: User is redirected to dashboard, dashboard header is visible.
    - Invalid credentials: Login fails, error message is shown, no dashboard access.
    - CI: GitHub Actions executes all tests and uploads an HTML report artifact.

### Negative Login Test Details
- Test name: `test_login_invalid_credentials`
- Steps:
    1. Navigate to OrangeHRM login page.
    2. Enter invalid username and password (`invalid_user`, `wrong_pass`).
    3. Attempt login.
    4. Assert login fails and error message is displayed.
- Purpose: Ensure the application does not allow access with invalid credentials and provides appropriate feedback to the user.
- Troubleshooting:
    - If the test fails unexpectedly, verify login page availability and error message locator.
    - If no error message is shown, check for locator changes or site updates.
    - If CI does not pick up the new test, ensure test file and function naming follow pytest conventions.

### Maintenance & Future Improvements
- Expand negative testing to cover empty fields, SQL injection, and edge cases.
- Periodically review test suite for coverage gaps and update documentation.
- Refer to onboarding guides for negative testing best practices.

### CI Integration
- The `.github/workflows/selenium.yml` workflow runs all tests in the `tests/` directory, including the new negative login test.
- Test results and HTML reports are available as CI artifacts.

---
