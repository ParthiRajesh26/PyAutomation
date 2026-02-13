import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class OrangeHRMLoginTest:
    """
    Test Case: Automate login functionality for OrangeHRM
    Jira Ticket: KAN-15

    This class encapsulates configuration and locators for maintainability and scalability.
    """
    LOGIN_URL = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
    USERNAME = 'Admin'
    PASSWORD = 'admin123'
    USERNAME_XPATH = "//input[@name='username']"
    PASSWORD_XPATH = "//input[@name='password']"
    LOGIN_BUTTON_XPATH = "//button[@type='submit']"
    DASHBOARD_URL_FRAGMENT = '/dashboard'
    DASHBOARD_HEADER_XPATH = "//h6[text()='Dashboard']"
    TIMEOUT = 15
    # Error message locator for failed login
    ERROR_MESSAGE_XPATH = "//p[contains(@class, 'oxd-alert-content-text')]"

    @staticmethod
    def get_chrome_driver():
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--window-size=1920,1080')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome(options=chrome_options)
        driver.set_page_load_timeout(30)
        return driver

@pytest.mark.login
def test_orangehrm_login():
    """
    Test Steps:
    1. Navigate to the login page.
    2. Enter valid username.
    3. Enter valid password.
    4. Click on Login button.
    5. Validate redirect to dashboard and dashboard header presence.

    Expected Result:
    User should be redirected to the dashboard page.
    """
    driver = None
    try:
        driver = OrangeHRMLoginTest.get_chrome_driver()
        driver.get(OrangeHRMLoginTest.LOGIN_URL)

        # Wait for username input
        WebDriverWait(driver, OrangeHRMLoginTest.TIMEOUT).until(
            EC.presence_of_element_located((By.XPATH, OrangeHRMLoginTest.USERNAME_XPATH))
        )
        username_input = driver.find_element(By.XPATH, OrangeHRMLoginTest.USERNAME_XPATH)
        password_input = driver.find_element(By.XPATH, OrangeHRMLoginTest.PASSWORD_XPATH)
        login_button = driver.find_element(By.XPATH, OrangeHRMLoginTest.LOGIN_BUTTON_XPATH)

        username_input.clear()
        username_input.send_keys(OrangeHRMLoginTest.USERNAME)
        password_input.clear()
        password_input.send_keys(OrangeHRMLoginTest.PASSWORD)
        login_button.click()

        # Wait for dashboard page load
        WebDriverWait(driver, OrangeHRMLoginTest.TIMEOUT).until(
            EC.url_contains(OrangeHRMLoginTest.DASHBOARD_URL_FRAGMENT)
        )
        assert OrangeHRMLoginTest.DASHBOARD_URL_FRAGMENT in driver.current_url, (
            f"Login failed or did not redirect to dashboard. Current URL: {driver.current_url}"
        )

        # Additional validation: check dashboard element presence
        WebDriverWait(driver, OrangeHRMLoginTest.TIMEOUT).until(
            EC.presence_of_element_located((By.XPATH, OrangeHRMLoginTest.DASHBOARD_HEADER_XPATH))
        )
        dashboard_header = driver.find_element(By.XPATH, OrangeHRMLoginTest.DASHBOARD_HEADER_XPATH)
        assert dashboard_header.is_displayed(), "Dashboard header not visible after login."

    except Exception as e:
        pytest.fail(f"Test failed due to error: {e}")
    finally:
        if driver:
            driver.quit()

def login_with_credentials(username, password):
    """
    Utility function to perform login and return result dict.
    """
    driver = OrangeHRMLoginTest.get_chrome_driver()
    result = {"success": False, "error": None}
    try:
        driver.get(OrangeHRMLoginTest.LOGIN_URL)
        WebDriverWait(driver, OrangeHRMLoginTest.TIMEOUT).until(
            EC.presence_of_element_located((By.XPATH, OrangeHRMLoginTest.USERNAME_XPATH))
        )
        username_input = driver.find_element(By.XPATH, OrangeHRMLoginTest.USERNAME_XPATH)
        password_input = driver.find_element(By.XPATH, OrangeHRMLoginTest.PASSWORD_XPATH)
        login_button = driver.find_element(By.XPATH, OrangeHRMLoginTest.LOGIN_BUTTON_XPATH)
        username_input.clear()
        username_input.send_keys(username)
        password_input.clear()
        password_input.send_keys(password)
        login_button.click()

        # Wait for either dashboard or error message
        try:
            WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, OrangeHRMLoginTest.ERROR_MESSAGE_XPATH))
            )
            error_elem = driver.find_element(By.XPATH, OrangeHRMLoginTest.ERROR_MESSAGE_XPATH)
            result["error"] = error_elem.text
            result["success"] = False
        except Exception:
            # Check for dashboard
            if OrangeHRMLoginTest.DASHBOARD_URL_FRAGMENT in driver.current_url:
                result["success"] = True
            else:
                result["error"] = "Unknown error during login."
                result["success"] = False
    finally:
        driver.quit()
    return result

@pytest.mark.login
@pytest.mark.parametrize("username,password,expected_error", [
    ("invalidUser", "admin123", "Invalid credentials"),
    ("Admin", "wrongPassword", "Invalid credentials"),
    ("wrongUser", "wrongPassword", "Invalid credentials")
])
def test_orangehrm_login_invalid_credentials(username, password, expected_error):
    """
    Negative Test Case: Attempt login with invalid credentials and verify failure.

    Test Steps:
    1. Navigate to the login page.
    2. Enter invalid username and/or password.
    3. Click on Login button.
    4. Validate error message is displayed.

    Expected Result:
    Login should fail and error message should indicate invalid credentials.
    """
    result = login_with_credentials(username, password)
    assert not result["success"], "Login succeeded with invalid credentials, which is incorrect."
    assert expected_error.lower() in result["error"].lower(), (
        f"Expected error message '{expected_error}' not found. Got: '{result['error']}'"
    )
