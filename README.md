
---
## Feature: Negative Login Test Case for Invalid Credentials

- Project Overview: This repository automates functional testing for OrangeHRM using Selenium WebDriver and pytest, focusing on login workflows and robust negative test coverage.

- Technology/framework used: Python, Selenium WebDriver, pytest, GitHub Actions (CI)

- Change implemented: Added a negative login test case to validate system behavior when invalid credentials are provided.

- Where the change was made: tests/test_login.py (added test_login_invalid_credentials function)

- Setup/installation steps:
  1. Clone the repository: `git clone https://github.com/ParthiRajesh26/PyAutomation.git`
  2. Install dependencies: `pip install -r requirements.txt`
  3. Ensure ChromeDriver is installed and available in PATH.

- Dependencies required:
  * Python >= 3.7
  * selenium
  * pytest
  * ChromeDriver

- How to run the tests:
  * Run all tests: `pytest tests/`
  * Run only login tests: `pytest tests/test_login.py`

- Example run command:
  ```bash
  pytest tests/test_login.py
  ```

- Expected behaviour/output:
  * Valid login: User is redirected to dashboard.
  * Invalid login: Login fails, error message is displayed (e.g., "Invalid credentials").

- CI Integration:
  * GitHub Actions workflow (.github/workflows/selenium.yml) automatically runs tests on push and pull requests.

- Troubleshooting Guide:
  * Test not discovered: Ensure function is named with 'test_' prefix and located in tests/ directory.
  * CI pipeline errors: Validate workflow configuration and review logs in GitHub Actions.
  * ChromeDriver issues: Ensure ChromeDriver is installed and compatible with your Chrome version.
  * Error message not shown: Verify application state and locator for error message.

- Maintenance procedures:
  * Update test cases as authentication logic evolves.
  * Review negative test coverage periodically (e.g., for SQL injection, XSS).
  * Document rationale for each test and update README.md accordingly.

- Recommendations for future improvements:
  * Parameterize negative login tests for multiple invalid credential scenarios.
  * Expand coverage to include additional security and edge cases.
  * Automate test plan validation and generation.
