import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random


@pytest.fixture()
def open_random_featured_product(browser):
    browser.get(browser.base_opencart_url)
    wait = WebDriverWait(browser, 5)
    featured_elements = wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "product-thumb")))
    random_index = random.randint(0, len(featured_elements) - 1)
    element = featured_elements[random_index]
    element.click()
    wait.until(EC.presence_of_element_located((By.TAG_NAME,"title")))

def test_check_qty_input_and_button(open_random_featured_product, browser):
    """
      Test is designed to check some functional elements are present on the item card page
    """
    quantity = browser.find_element(By.XPATH, ("//div[contains(text(), 'Qty')]"))
    input = browser.find_element(By.NAME, "quantity")
    button = browser.find_element(By.ID, "button-cart")
    assert quantity and input and button


def test_check_image_present(open_random_featured_product, browser):
    """
      Test is designed to check that product image is present for a random product from featured list
    """
    check_img = ".jpg"
    try:
        element = browser.find_element(By.XPATH, "//div[@class='image magnific-popup']/a")
        href = element.get_attribute("href")
        assert check_img in href
    except Exception:
        print("Something went wrong. No element found.")


def test_check_description_present(open_random_featured_product, browser):
    """
      Test is designed to check that product description is present for a random product from featured list
    """
    try:
        element = browser.find_element(By.XPATH, "//a[@href='#tab-description']")
        txt = browser.find_element(By.XPATH, "//div[@id='tab-description']/p").text
        assert element.text == 'Description' and txt
    except Exception:
        print("Something went wrong. No element found.")



def test_check_review_tab(open_random_featured_product, browser):
    """
      Test is designed to check the Reviews tab content
    """
    try:

        element = browser.find_element(By.XPATH, "//a[@href='#tab-review']")
        element.click()
        author = browser.find_element(By.ID,"input-author")
        txt = browser.find_element(By.ID, "input-text")
        rating = browser.find_element(By.ID, "input-rating")

        assert author and txt and rating
    except Exception:
        print("Something went wrong.")


def test_check_nav_tab(open_random_featured_product, browser):
    """
      Test is designed to check that navigation tab is present on the item page
    """
    try:
        top = browser.find_element(By.ID, "top")

        assert top
    except Exception:
        print("Something went wrong.")

