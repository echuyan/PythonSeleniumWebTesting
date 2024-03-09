from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_switch_cur_main_page(browser):
    """
        Test is designed to check currency switching on the main page
    """

    browser.get(browser.base_opencart_url)
    wait = WebDriverWait(browser, 5)
    wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "product-thumb")))
    prices = browser.find_elements(By.XPATH, ("//span[@class='price-new']"))
    old_prices=[]
    for item in prices:
        old_prices.append(item.text)

    current_cur = browser.find_element(By.XPATH, ("//form[@id='form-currency']/div/a/strong")).text

    browser.find_element(By.XPATH, ("//span[contains(text(),'Currency')]")).click()

    switches = browser.find_elements(By.XPATH, ("//form[@id='form-currency']/div/ul/li/a"))
    for switch in switches:
        if current_cur in switch.text:
            pass
        else:
            switch.click()
            break

    prices = browser.find_elements(By.XPATH, ("//span[@class='price-new']"))
    new_prices = []
    for item in prices:
        new_prices.append(item.text)

    old_set = set(old_prices)
    new_set = set(new_prices)
    assert old_set.isdisjoint(new_set)

