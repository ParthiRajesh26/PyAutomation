
---
## Feature: Negative Login Test Case for Invalid Credentials

- Project Overview: PyAutomation automates web application testing using Selenium and pytest. The repository includes functional and regression tests for OrangeHRM.
- Technology/framework used: Python, Selenium WebDriver, pytest, GitHub Actions (CI)
- Change implemented: Added a negative test case for login with invalid credentials to verify authentication failure and error message display.
- Where the change was made: tests/test_login.py (function: test_login_invalid_credentials)
- Setup/installation steps:
    1. Ensure Python 3.7+ is installed.
    2. Install dependencies: `pip install -r requirements.txt` (requirements.txt should include selenium and pytest)
    3. Install Chrome browser and ensure chromedriver is available in PATH.
- Dependencies required: selenium, pytest, chromedriver
- How to run the tests: `pytest tests/`
- Example run command:
    ```bash
    pytest tests/test_login.py -k test_login_invalid_credentials
    ```
- Expected behaviour/output:
    - Login attempt with invalid credentials should fail.
    - Error message containing "Invalid credentials" should be displayed.
    - No access to dashboard after login attempt.

### Troubleshooting Guide
- Common Issues:
    - Test fails due to incorrect assertion (error message not found).
    - Login unexpectedly succeeds (possible bug or incorrect test data).
    - Chromedriver not found or incompatible with Chrome version.
    - Selenium driver initialization fails in CI.
- Solutions:
    - Verify error message locator and text in OrangeHRM UI.
    - Update invalid credential values to ensure login fails.
    - Ensure chromedriver is installed and matches Chrome version.
    - Check CI logs for driver setup issues.

### Maintenance Procedures
- To update test data or assertion logic, modify test_login_invalid_credentials in tests/test_login.py.
- Periodically review error message locator and login workflow for UI changes.
- Expand negative test coverage by parameterizing invalid credential combinations.

### Knowledge Transfer
- Negative login tests help ensure authentication robustness and error handling.
- Use pytest fixtures and parameterization for scalable negative testing.
- Maintain test isolation and reproducibility by using dedicated test data.
