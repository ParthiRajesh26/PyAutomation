# Authentication Test Cases

## Negative Login Test Case for Invalid Credentials

### Overview
This section documents the negative login test case implemented to verify that the authentication module correctly rejects invalid credentials.

### Test Scenarios
- Invalid username with valid password
- Valid username with invalid password
- Both username and password invalid

### Implementation Details
- Implemented in `tests/test_login.py` as `test_orangehrm_login_invalid_credentials` using pytest parameterization.
- Utilizes Selenium WebDriver for UI automation.
- Checks for error message display and ensures login does not succeed.

### Expected Behavior
- Login attempts with invalid credentials should fail.
- Error message ('Invalid credentials') must be shown.

### Troubleshooting
- If test fails, check:
  - Error message locator correctness
  - Test data for invalid credentials
  - Selenium driver setup
- Ensure no sensitive data is exposed in logs or error messages.

### Maintenance Procedures
- To add new negative scenarios, extend the parameterized list in `test_orangehrm_login_invalid_credentials`.
- Review authentication logic and error handling periodically.

### Knowledge Transfer
- New contributors should review this document and the test implementation in `tests/test_login.py` for onboarding.
