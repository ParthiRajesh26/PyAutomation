
---
## Feature: Negative Login Test Case for Invalid Credentials

- **Project Overview:**
  PyAutomation is an automation testing framework for validating web application functionality using Selenium and pytest. This project automates login tests for OrangeHRM.

- **Technology/Framework Used:**
  Python, Selenium WebDriver, pytest, GitHub Actions CI

- **Change Implemented:**
  Added a negative login test case to verify that the system correctly handles invalid credentials by displaying an error message and preventing access.

- **Where the Change Was Made:**
  - `tests/test_login.py`: Added `test_login_invalid_credentials` function.

- **Setup/Installation Steps:**
  1. Clone the repository.
  2. Install dependencies:
     ```bash
     pip install -r requirements.txt
     ```
  3. Ensure ChromeDriver is installed and available in your PATH.

- **Dependencies Required:**
  - Python 3.7+
  - selenium
  - pytest
  - ChromeDriver

- **How to Run the Tests:**
  ```bash
  pytest tests/test_login.py
  ```

- **Example Run Command:**
  ```bash
  pytest tests/test_login.py::test_login_invalid_credentials
  ```

- **Expected Behaviour/Output:**
  - The test attempts login with invalid credentials (`invalid_user` / `wrong_pass`).
  - Login should fail.
  - An error message indicating invalid credentials should be displayed.
  - Test assertion ensures login does not succeed and the correct error message is present.

---
