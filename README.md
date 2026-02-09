

---
## Feature: Negative Login Test Case for Invalid Credentials
- Project Overview: PyAutomation is an automated test suite for OrangeHRM, focusing on robust login functionality and error handling using Selenium and pytest.
- Technology/framework used: Python, Selenium WebDriver, pytest, GitHub Actions CI
- Change implemented: Added a negative login test case to validate that the system correctly handles invalid credentials and displays appropriate error messages.
- Where the change was made: tests/test_login.py (new test function: test_login_invalid_credentials)
- Setup/installation steps:
    1. Clone the repository: `git clone https://github.com/ParthiRajesh26/PyAutomation.git`
    2. Checkout the feature branch: `git checkout feature/negative-login-invalid-credentials`
    3. Install dependencies: `pip install -r requirements.txt` (ensure ChromeDriver is available in PATH)
- Dependencies required: Python 3.x, Selenium, pytest, ChromeDriver
- How to run the tests: `pytest tests/test_login.py`
- Example run command:
    ```bash
    pytest tests/test_login.py -k test_login_invalid_credentials
    ```
- Expected behaviour/output:
    - For invalid login attempts, the test should fail to log in and display an error message such as "Invalid credentials".
    - All invalid input combinations are validated; test passes if error handling is robust.

### Troubleshooting Guide
- **Test not detected by CI**: Ensure test function starts with `test_` and is located in `tests/test_login.py`.
- **Assertion fails due to unexpected error message**: Check OrangeHRM error message text and update assertion logic if needed.
- **ChromeDriver issues**: Verify ChromeDriver is installed and available in PATH.
- **Documentation unclear**: Revise this section for clarity and completeness.

### Maintenance Procedures
- Periodically review and update negative test cases for new authentication features or error messages.
- Ensure compatibility with codebase changes and Selenium/pytest updates.

### Recommendations for Future Improvements
- Parameterize negative tests for additional authentication flows.
- Automate generation of negative test cases for scalability.
- Schedule periodic reviews to maintain robust coverage.
