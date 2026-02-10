
---
## Feature: Negative Login Test Case for Invalid Credentials

- Project Overview: PyAutomation is an automation testing framework for validating web application functionality, focusing on login workflows for OrangeHRM.
- Technology/framework used: Python, Selenium WebDriver, Pytest, GitHub Actions CI
- Change implemented: Added a negative login test case to verify system response to invalid credentials.
- Where the change was made: tests/test_login.py (new test function: test_login_with_invalid_credentials)
- Setup/installation steps:
    1. Ensure Python 3.x is installed.
    2. Install dependencies: `pip install selenium pytest`
    3. Download and install ChromeDriver compatible with your Chrome browser version.
- Dependencies required:
    - selenium
    - pytest
    - ChromeDriver
- How to run the tests:
    - Run all tests: `pytest tests/`
    - Run only login tests: `pytest tests/test_login.py`
- Example run command:
    ```bash
    pytest tests/test_login.py
    ```
- Expected behaviour/output:
    - Valid login: User is redirected to dashboard, dashboard header is visible.
    - Invalid login: Login fails, error message "Invalid credentials" is displayed, test asserts failure.

### Troubleshooting Guide
- If tests fail due to missing ChromeDriver, ensure it is installed and accessible in your PATH.
- If error messages differ, update test assertions to match actual application output.
- If CI fails, review GitHub Actions logs for missing dependencies or environment issues.

### Maintenance Procedures
- To add new negative test cases, create new functions in tests/test_login.py using pytest conventions.
- Keep selectors and error messages updated as application evolves.
- Periodically review test suite for flaky or outdated tests.

### Recommendations for Future Improvements
- Parameterize invalid credential scenarios for broader coverage.
- Expand negative tests to cover locked accounts, expired passwords, etc.
- Integrate test result metrics into CI reporting.
- Automate documentation updates for new test cases.

### Knowledge Transfer
- Location of login tests: tests/test_login.py
- Contact points for test maintenance: Refer to repository contributors or automation team lead.

---
