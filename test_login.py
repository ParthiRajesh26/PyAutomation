import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

LOGIN_URL = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
USERNAME = 'Admin'
PASSWORD = 'admin123'
USERNAME_XPATH = "//input[@name='username']"
PASSWORD_XPATH = "//input[@name='password']"
LOGIN_BTN_XPATH = "//button[@type='submit']"
DASHBOARD_URL_FRAGMENT = '/dashboard'

@pytest.fixture(scope='function')
def driver():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--window-size=1920,1080')
    driver = webdriver.Chrome(options=chrome_options)
    driver.set_page_load_timeout(30)
    yield driver
    driver.quit()

def test_automate_login_functionality_for_orangehrm(driver):
    """
    Test Case: Automate login functionality for OrangeHRM
    Jira Ticket: KAN-15

    Steps:
    1. Navigate to the login page
    2. Enter valid username
    3. Enter valid password
    4. Click on Login button
    Expected Result:
    User should be redirected to the dashboard page.
    """
    try:
        driver.get(LOGIN_URL)
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH, USERNAME_XPATH))
        )
        username_field = driver.find_element(By.XPATH, USERNAME_XPATH)
        password_field = driver.find_element(By.XPATH, PASSWORD_XPATH)
        login_button = driver.find_element(By.XPATH, LOGIN_BTN_XPATH)

        username_field.clear()
        username_field.send_keys(USERNAME)
        password_field.clear()
        password_field.send_keys(PASSWORD)
        login_button.click()

        WebDriverWait(driver, 15).until(
            EC.url_contains(DASHBOARD_URL_FRAGMENT)
        )
        assert DASHBOARD_URL_FRAGMENT in driver.current_url, (
            f"Login failed or dashboard not loaded. Current URL: {driver.current_url}"
        )
    except Exception as e:
        pytest.fail(f"Test failed due to exception: {e}")
