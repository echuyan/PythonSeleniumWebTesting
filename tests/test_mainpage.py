from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_check_title(browser):
    """
      Test is designed to check the title of the Main Page
    """
    browser.get(browser.base_opencart_url)
    wait = WebDriverWait(browser, 5, poll_frequency=1)
    wait.until(EC.title_is("Your Store"))
    assert EC.title_is("Your Store")


def test_check_featured(browser):
    """
        Test is designed to check the Featured Section of the Main Page
        Test id designed in a way to avoid StaleElementReferenceException
        Within the for loop the test opens each featured item card and checks its title
    """
    browser.get(browser.base_opencart_url)
    wait = WebDriverWait(browser, 5)
    featured_elements = wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "product-thumb")))
    img_elements = browser.find_elements(By.XPATH, ("//div[@class='product-thumb']/div/a/img"))
    titles = [item.get_attribute("title") for item in img_elements]

    for i in range(len(featured_elements)):
        featured_elements = wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "product-thumb")))
        featured_elements[i].click()
        wait.until(EC.visibility_of_element_located((By.ID, "product-info")))
        assert EC.title_is(titles[i])
        browser.back()
        i += 1


def test_check_nav_items(browser):
    """
        Test is designed to check the Navigation Bar of the Main Page

    """
    browser.get(browser.base_opencart_url)
    wait = WebDriverWait(browser, 5)
    wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "product-thumb")))
    nav_items_dropdown = browser.find_elements(By.XPATH, ("//li[@class='nav-item dropdown']"))
    nav_items = browser.find_elements(By.XPATH, ("//li[@class='nav-item']"))
    assert len(nav_items) != 0
    assert len(nav_items_dropdown) != 0


def test_check_carousel(browser):
    """
        Test is designed to check the carousel block of the Main Page

    """
    browser.get(browser.base_opencart_url)
    wait = WebDriverWait(browser, 5)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "carousel-inner")))
    car_slides = browser.find_elements(By.XPATH, ("//div[@class='carousel slide']"))
    assert len(car_slides) == 2
    car_indicators = browser.find_elements(By.XPATH, ("//div[@class='carousel-indicators']"))
    assert len(car_indicators) == 2


def test_check_cart(browser):
    """
        Test is designed to check the presence of the cart at the Main Page

    """
    browser.get(browser.base_opencart_url)
    wait = WebDriverWait(browser, 5)
    wait.until(EC.presence_of_element_located((By.ID, "header-cart")))
    cart_text = browser.find_element(By.XPATH, ("//div[@id='header-cart']/div/button")).text
    assert cart_text == "0 item(s) - $0.00"


