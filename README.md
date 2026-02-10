

---
## Feature: Negative Login Test for Invalid Credentials
- Project Overview: PyAutomation is a Python-based automation and testing repository focused on validating web application flows using Selenium and pytest.
- Technology/framework used: Python 3.x, Selenium WebDriver, pytest, GitHub Actions
- Change implemented: Added a negative login test case to verify that the application correctly rejects invalid credentials and returns an appropriate error message.
- Where the change was made: tests/test_login.py (function: test_login_with_invalid_credentials)
- Setup/installation steps:
  1. Ensure Python 3.x is installed.
  2. Install dependencies with `pip install -r requirements.txt` (ensure selenium and pytest are present).
  3. (Optional) Install ChromeDriver for Selenium if not already available.
- Dependencies required:
  - selenium
  - pytest
  - chromedriver (for local runs)
- How to run the tests:
  - Execute `pytest tests/test_login.py` to run all login tests including the negative case.
- Example run command:
  ```bash
  pytest tests/test_login.py
  ```
- Expected behaviour/output:
  - The negative login test (`test_login_with_invalid_credentials`) attempts login with invalid credentials and asserts that the application displays an error message such as "Invalid credentials" and does not grant access.

### Troubleshooting Guide
- If the negative test unexpectedly passes (login succeeds with invalid credentials), review application authentication logic for flaws.
- If the test fails due to timeouts or exceptions, verify ChromeDriver installation and Selenium setup.
- For flaky tests, ensure test isolation and check for shared state or race conditions.
- If CI/CD does not pick up new tests, verify test discovery patterns in `.github/workflows/selenium.yml`.

### Maintenance Procedures
- To extend negative login coverage, parameterize the test to include empty fields or injection attempts.
- Regularly review and refactor test code for maintainability.
- Update documentation when adding new negative scenarios.

### Recommendations
- Use fixtures for test data setup and teardown.
- Periodically review test suite for coverage and robustness.
- Integrate security-focused negative tests.

---