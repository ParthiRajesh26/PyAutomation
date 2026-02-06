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
    ERROR_MESSAGE_XPATH = "//p[contains(@class, 'oxd-alert-content-text')]"
    TIMEOUT = 15

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

@pytest.mark.login
def test_login_invalid_credentials():
    """
    Negative Test: Attempt login with invalid credentials.
    Steps:
    1. Navigate to the login page.
    2. Enter invalid username and/or password.
    3. Click on Login button.
    4. Validate that login fails and error message is displayed.

    Expected Result:
    Login should fail and an error message should be shown.
    """
    driver = None
    INVALID_USERNAME = "invalid_user"
    INVALID_PASSWORD = "wrong_pass"
    try:
        driver = OrangeHRMLoginTest.get_chrome_driver()
        driver.get(OrangeHRMLoginTest.LOGIN_URL)
        WebDriverWait(driver, OrangeHRMLoginTest.TIMEOUT).until(
            EC.presence_of_element_located((By.XPATH, OrangeHRMLoginTest.USERNAME_XPATH))
        )
        username_input = driver.find_element(By.XPATH, OrangeHRMLoginTest.USERNAME_XPATH)
        password_input = driver.find_element(By.XPATH, OrangeHRMLoginTest.PASSWORD_XPATH)
        login_button = driver.find_element(By.XPATH, OrangeHRMLoginTest.LOGIN_BUTTON_XPATH)

        username_input.clear()
        username_input.send_keys(INVALID_USERNAME)
        password_input.clear()
        password_input.send_keys(INVALID_PASSWORD)
        login_button.click()

        # Wait for error message
        error_message = WebDriverWait(driver, OrangeHRMLoginTest.TIMEOUT).until(
            EC.presence_of_element_located((By.XPATH, OrangeHRMLoginTest.ERROR_MESSAGE_XPATH))
        )
        assert error_message.is_displayed(), "Error message not displayed after failed login."
        assert "Invalid credentials" in error_message.text, (
            f"Expected 'Invalid credentials' in error message, got: '{error_message.text}'"
        )
    except Exception as e:
        pytest.fail(f"Negative login test failed due to error: {e}")
    finally:
        if driver:
            driver.quit()
