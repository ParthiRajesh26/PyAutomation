
---
## Feature: Negative Login Test Case for Invalid Credentials

- **Project Overview:**
  PyAutomation is an automation testing project for validating web application login functionality using Selenium WebDriver and pytest. It includes robust test coverage for both positive and negative authentication scenarios.

- **Technology/framework used:**
  Python, Selenium WebDriver, pytest, GitHub Actions CI

- **Change implemented:**
  Added a negative login test case to verify that invalid credentials are correctly rejected and an error message is displayed.

- **Where the change was made:**
  - tests/test_login.py (added `test_login_invalid_credentials`)
  - README.md (this section)

- **Setup/installation steps:**
  1. Clone the repository: `git clone https://github.com/ParthiRajesh26/PyAutomation.git`
  2. Checkout the branch: `git checkout feature/negative-login-invalid-credentials`
  3. Install dependencies: `pip install -r requirements.txt`
  4. Ensure ChromeDriver is installed and accessible in your PATH.

- **Dependencies required:**
  - Python 3.7+
  - selenium
  - pytest
  - chromedriver (matching your Chrome version)

- **How to run the tests:**
  - Execute all tests: `pytest tests/`
  - To run only login tests: `pytest tests/test_login.py`

- **Example run command:**
  ```bash
  pytest tests/test_login.py
  ```

- **Expected behaviour/output:**
  - The negative login test (`test_login_invalid_credentials`) attempts login with invalid username and password.
  - Test should fail the login, display an error message, and assert that login is unsuccessful.
  - Sample output:
    ```
    ============================= test session =============================
    tests/test_login.py::test_login_invalid_credentials PASSED
    ```

- **Troubleshooting Guide:**
  - **Common Issues:**
    - Login function signature changes: Update `test_login_invalid_credentials` to match new interface.
    - Error handling changes: Adjust assertion logic for error messages or exceptions.
    - ChromeDriver compatibility: Ensure correct ChromeDriver version for your Chrome browser.
    - No error message displayed: Confirm error locator (`ERROR_MESSAGE_XPATH`) matches application changes.
    - CI test discovery issues: Ensure test is named with `test_` prefix and located in `tests/` directory.
  - **Solutions:**
    - Review login module and update test accordingly.
    - Consult pytest documentation for assertion and fixture best practices.
    - Validate CI configuration for test discovery.

- **Maintenance Procedures:**
  - If login logic changes, update the test and utility function accordingly.
  - To add more negative scenarios, parameterize the test using pytest's `@pytest.mark.parametrize`.

- **Recommendations for Future Improvements:**
  - Parameterize negative login tests for broader coverage.
  - Add test coverage reports to CI pipeline for ongoing quality assessment.
  - Review negative test cases periodically as authentication logic evolves.

---
