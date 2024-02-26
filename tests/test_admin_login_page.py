from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def test_admin_login_page(browser):
    """
         Test is designed to check the Admin Login page
    """
    browser.get(browser.base_opencart_url + "/admin")
    wait = WebDriverWait(browser,2)
    browser.find_element(By.ID, "input-username")
    browser.find_element(By.NAME, "password")
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    browser.find_element(By.XPATH, "//*[text()='OpenCart']")
    assert browser.find_element(By.XPATH,"//div[@class='card-header']").text == 'Please enter your login details.'
