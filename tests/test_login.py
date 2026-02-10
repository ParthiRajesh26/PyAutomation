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
    ERROR_MESSAGE_XPATH = "//p[contains(@class