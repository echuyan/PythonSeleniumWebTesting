from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver import ActionChains

def test_add_item_to_cart(browser):
    """
        Test is designed to check adding a random item from the main page to the cart
    """
    actions = ActionChains(browser)
    browser.get(browser.base_opencart_url)
    wait = WebDriverWait(browser, 5)
    featured_elements = wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "product-thumb")))
    element = featured_elements[0]
    title = element.find_element(By.XPATH, ("//div/div/h4/a")).text
    actions.scroll_to_element(element).perform()
    addtocart = element.find_element(By.XPATH, ("//div/form/div/button"))
    actions.move_to_element(addtocart).click().perform()
    wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='alert']")))
    #browser.find_element(By.XPATH, "//div[@id='alert']/div/button[@class='btn-close']").click()
    time.sleep(5)

    wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='header-cart']/div/button")))
    browser.find_element(By.XPATH,"//div[@id='header-cart']/div/button").click()
    wait.until(EC.presence_of_element_located((By.XPATH, "//strong[contains(text(), 'View Cart')]"))).click()
    wait.until(EC.presence_of_element_located((By.XPATH, "//strong[contains(text(), 'Checkout')]")))

    items = browser.find_elements(By.XPATH,"//div[@id='shopping-cart']/div/table/tbody/tr/td[@class='text-start text-wrap']/a")
    titles = []
    for item in items:
        titles.append(item.text)

    assert title in titles

