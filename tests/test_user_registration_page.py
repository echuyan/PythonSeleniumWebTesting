
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def test_user_reg_page(browser):
    """
         Test is designed to check the User Registration page
    """
    browser.get(browser.base_opencart_url + "/index.php?route=account/register")
    wait = WebDriverWait(browser, 2)
    browser.find_element(By.ID, "input-firstname")
    browser.find_element(By.ID, "input-lastname")
    browser.find_element(By.ID, "input-email")
    browser.find_element(By.NAME, "password")
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    browser.find_element(By.XPATH, "//*[text()='OpenCart']")
    assert browser.find_element(By.XPATH,"//div[@id='content']/h1").text == 'Register Account'
