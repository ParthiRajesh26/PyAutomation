
---
## Feature: Negative Login Test Case for Invalid Credentials

- **Project Overview:**
  This repository implements automated testing for OrangeHRM using Selenium and pytest. The new feature strengthens authentication robustness by verifying that login fails with invalid credentials.

- **Technology/framework used:**
  Python, Selenium WebDriver, pytest, pytest-html, webdriver-manager, GitHub Actions CI

- **Change implemented:**
  Added a negative test case (`test_orangehrm_login_invalid`) to verify login failure with invalid credentials.

- **Where the change was made:**
  - `tests/test_login.py`: New test function added
  - Branch: `feature/negative-login-invalid-credentials`

- **Setup/installation steps:**
  1. Clone the repository
     ```bash
     git clone https://github.com/ParthiRajesh26/PyAutomation.git
     ```
  2. Checkout the feature branch
     ```bash
     git checkout feature/negative-login-invalid-credentials
     ```
  3. Install dependencies
     ```bash
     pip install selenium pytest pytest-html webdriver-manager
     ```

- **Dependencies required:**
  - Python 3.10+
  - selenium
  - pytest
  - pytest-html
  - webdriver-manager

- **How to run the tests:**
  Run all tests (including the negative login test) with:
  ```bash
  pytest tests/ --html=report.html --self-contained-html
  ```

- **Example run command:**
  ```bash
  pytest tests/test_login.py --html=report.html --self-contained-html
  ```

- **Expected behaviour/output:**
  - The negative login test (`test_orangehrm_login_invalid`) attempts login with invalid credentials and asserts that login fails and an error message is shown.
  - Test output should indicate failure for invalid credentials and display the error message returned by OrangeHRM.

- **Example test code snippet:**
  ```python
  @pytest.mark.login
  def test_orangehrm_login_invalid():
      invalid_username = "invalid_user"
      invalid_password = "wrong_pass"
      result = login_with_credentials(invalid_username, invalid_password)
      assert not result["success"]
      assert result["error"] is not None
      assert "Invalid" in result["error"] or "credentials" in result["error"]
  ```

- **Troubleshooting Guide:**
  - If the test fails due to unexpected error messages, verify the OrangeHRM login page's current error text and update assertions accordingly.
  - If CI does not detect the new test, confirm the test function name starts with `test_` and is in the correct file/location.
  - Ensure ChromeDriver and Selenium are installed and compatible with your Python environment.
  - For credential updates or additional negative cases, modify the `login_with_credentials` function or add new test functions.

- **Maintenance Procedures:**
  - To update test credentials, edit the values in the `test_orangehrm_login_invalid` function.
  - To change error message assertions, adjust the `assert` statements to match updated UI messages.

- **Knowledge Transfer:**
  - New contributors should review `tests/test_login.py` for test structure and negative testing practices.
  - Refer to this README section for setup, test execution, and troubleshooting steps.

- **CI Integration:**
  - The GitHub Actions CI pipeline (`.github/workflows/selenium.yml`) is configured to run all tests in `tests/` automatically on push and pull requests.
  - Test results and HTML reports are uploaded as artifacts for review.
