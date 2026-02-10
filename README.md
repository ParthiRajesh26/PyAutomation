
---
## Feature: Negative Login Test Case for Invalid Credentials
- Project Overview: This repository implements automated testing for OrangeHRM login functionality using Selenium and pytest. The new feature adds a negative test case to verify system behavior when invalid credentials are provided, improving reliability and coverage.
- Technology/framework used: Python, Selenium WebDriver, pytest, GitHub Actions
- Change implemented: Added a negative login test case to validate login failure scenarios with invalid credentials.
- Where the change was made: tests/test_login.py (function: test_login_invalid_credentials)
- Setup/installation steps:
    1. Clone the repository: `git clone https://github.com/ParthiRajesh26/PyAutomation.git`
    2. Navigate to the project directory: `cd PyAutomation`
    3. Install dependencies: `pip install -r requirements.txt`
    4. Ensure ChromeDriver is installed and accessible in your PATH.
- Dependencies required:
    - Python 3.7+
    - selenium
    - pytest
    - chromedriver (compatible with your Chrome version)
- How to run the tests:
    - Run all tests: `pytest tests/`
    - Run only login tests: `pytest tests/test_login.py`
- Example run command:
    `pytest tests/test_login.py -v`
- Expected behaviour/output:
    - The negative login test case will attempt login using invalid credentials (e.g., username="invalid", password="wrongpass") and assert that login fails, with an error message displayed and access denied.
    - Output example:
        ```
        tests/test_login.py::test_login_invalid_credentials PASSED
        ```

### Negative Login Test Case Details
- Purpose: To ensure the application correctly handles invalid login attempts by denying access and displaying appropriate error messages.
- Test Logic:
    1. Navigate to login page.
    2. Enter invalid username and password.
    3. Click login.
    4. Assert error message is visible and dashboard is not accessible.
- Sample code snippet:
    ```python
    @pytest.mark.login
    def test_login_invalid_credentials():
        result = login_with_credentials("invalid", "wrongpass")
        assert not result["success"], "Login should fail with invalid credentials."
        assert result["error"] is not None and "Invalid credentials" in result["error"], "Proper error message should be displayed."
    ```
- Troubleshooting Guide:
    - If error message is not detected, verify UI selectors and error message locator.
    - If test interferes with other login tests, ensure test isolation via setup/teardown.
    - If credentials do not trigger expected error, update test inputs and assertions.
- Maintenance Procedures:
    - To add more negative cases, parameterize login tests with various invalid inputs.
    - Update locators and assertions as UI evolves.
    - Regularly review test suite for coverage and reliability.
- Recommendations:
    - Use fixtures for credential management to scale test cases.
    - Maintain clear naming conventions and modular test structure.
    - Expand negative coverage to edge cases (e.g., empty fields, SQL injection).

---
