import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

@pytest.fixture()
def receive_data():
    file_path = "../admin_credentials"
    file_descriptor = os.open(file_path, os.O_RDONLY)
    data = os.read(file_descriptor, os.path.getsize(file_path))
    print(data.decode())
    os.close(file_descriptor)
    return data.decode().split()


def test_login_logout_admin_page(receive_data, browser):
    """
         Test is designed to check the login-logout on the Admin Page
    """
    data = receive_data

    browser.get(browser.base_opencart_url + "/admin")
    wait = WebDriverWait(browser, 2)

    browser.find_element(By.ID, "input-username").send_keys(data[0])
    browser.find_element(By.NAME, "password").send_keys(data[1])
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    try:
        wait.until(EC.visibility_of_element_located((By.XPATH, "//body[@class='modal-open']")))
        browser.find_element(By.XPATH, "//body[@class='modal-open']/descendant::button[@class='btn-close']").click()
        wait.until(EC.presence_of_element_located((By.XPATH, "//h1[text()='Dashboard']")))
        element = browser.find_element(By.ID, "nav-profile")
        assert element
        browser.find_element(By.XPATH, "//span[text()='Logout']").click()
    except Exception:
        wait.until(EC.presence_of_element_located((By.XPATH, "//h1[text()='Dashboard']")))
        element = browser.find_element(By.ID, "nav-profile")
        assert element
        browser.find_element((By.XPATH, "//span[text()='Logout']")).click()
