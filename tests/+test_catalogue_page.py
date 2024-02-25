import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver import ActionChains
import random
from selenium.common.exceptions import NoSuchElementException

@pytest.fixture()
def open_catalogue(browser):
    browser.get(browser.base_opencart_url)
    actions = ActionChains(browser)
    wait = WebDriverWait(browser, 5)
    wait.until(EC.visibility_of_all_elements_located((By.ID, "narbar-menu")))
    element = browser.find_element(By.XPATH, ("//div[@id='narbar-menu']/ul/li/a")).click()
    #actions.move_to_element(element).perform()
    wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "see-all")))
    browser.find_element(By.XPATH, ("//div[@id='narbar-menu']/ul/li/div/a[@class='see-all']")).click()
    yield

@pytest.fixture()
def open_catalogue_desktops(browser):
    browser.get(browser.base_opencart_url)
    actions = ActionChains(browser)
    wait = WebDriverWait(browser, 5)
    wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "product-thumb")))
    element = browser.find_element(By.XPATH, ("//div[@id='narbar-menu']/ul/li/a[contains(text(), 'Desktops')]"))
    actions.move_to_element(element).perform()
    browser.find_element(By.XPATH, ("//div[@id='narbar-menu']/ul/li/a[contains(text(), 'Desktops')]/following-sibling::div/a")).click()
    yield


def test_check_headings_cat(open_catalogue, browser):
    """
      Test is designed to check that the heading of the catalogue section corresponds to the active element in the catalogue tree
    """
    active_element = browser.find_element(By.XPATH, ("//div/a[@class='list-group-item active']"))
    heading = browser.find_element(By.XPATH, ("//div[@id='content']/h1"))
    assert heading.text in active_element.text


def test_check_pagination(open_catalogue_desktops, browser):
    """
      Test is designed to check that pagination in the catalogue
      Works with some limitations such as: section Desktops exists and contains more than 10 items
    """
    wait = WebDriverWait(browser, 5)
    wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "pagination")))
    text =  browser.find_element(By.XPATH, ("//div[@class='col-sm-6 text-end']")).text
    items_count = int(text.split()[5])
    pages = int(text.split()[6].split('(')[1])
    actions = ActionChains(browser)
    counter = 0

    for i in range (pages):
        wait.until(EC.visibility_of_all_elements_located((By.XPATH, "//div[@class='product-thumb']")))
        counter += len(browser.find_elements(By.XPATH, ("//div[@class='product-thumb']")))
        if i != pages-1:
            wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), '>') and not(contains(text(),'|'))]")))
            element = browser.find_element(By.XPATH, ("//a[contains(text(), '>') and not(contains(text(),'|'))]"))
            actions.move_to_element(element).click().perform()

    assert counter == items_count


def test_check_tree_nav(open_catalogue, browser):
    """
      Test is designed to check catalogue tree navigation and number of items in the selected section

    """
    wait = WebDriverWait(browser, 5)
    wait.until(EC.visibility_of_all_elements_located((By.XPATH, "//a[@class='list-group-item']")))
    elements =  browser.find_elements(By.XPATH, ("//a[@class='list-group-item' and not(contains(text(), 'Components'))]"))
    random_index = random.randint(0, len(elements) - 1)
    element = elements[random_index]
    print(element.text)
    items_count = int(element.text.split('(')[1].split(')')[0])
    element.click()

    wait.until(EC.visibility_of_all_elements_located((By.XPATH, "//div[@id='content']")))
    counter = len(browser.find_elements(By.XPATH, ("//div[@class='product-thumb']")))
    assert items_count == counter




def test_check_buttons(open_catalogue, browser):
    """
      Test is designed to check the existence of cart, favorite and comparison buttons for each product on the page

    """
    wait = WebDriverWait(browser, 5)
    wait.until(EC.visibility_of_all_elements_located((By.XPATH, "//a[@class='list-group-item']")))
    elements =  browser.find_elements(By.XPATH, ("//a[@class='list-group-item' and not(contains(text(), 'Components'))]"))
    random_index = random.randint(0, len(elements) - 1)
    element = elements[random_index]
    items_count = int(element.text.split('(')[1].split(')')[0])
    element.click()
    wait.until(EC.visibility_of_all_elements_located((By.XPATH, "//div[@id='content']")))
    counter = len(browser.find_elements(By.XPATH, ("//button[@type='submit']")))
    assert counter == items_count*3


def test_check_show_more_products(open_catalogue, browser):
    """
      Test is designed to check the Show switch (number of showed products)

    """
    wait = WebDriverWait(browser, 5)
    wait.until(EC.visibility_of_all_elements_located((By.XPATH, "//a[@class='list-group-item' and not(contains(text(), '-'))]")))
    elements = browser.find_elements(By.XPATH, ("//a[@class='list-group-item']"))

    random_index = random.randint(0, len(elements) - 1)
    element = elements[random_index]
    items_count = int(element.text.split('(')[1].split(')')[0])
    element.click()

    wait.until(EC.visibility_of_all_elements_located((By.XPATH, "//div[@id='content']")))

    try:
        selectors = browser.find_elements(By.XPATH, ("//select[@id='input-limit']/option"))
        random_index = random.randint(0, len(selectors) - 1)
        selector = selectors[random_index]
        selected_number = int(selector.text)
        selector.click()
        wait.until(EC.visibility_of_all_elements_located((By.XPATH, "//div[@class='product-thumb']")))
        counter = len(browser.find_elements(By.XPATH, ("//div[@class='product-thumb']")))
        assert counter == selected_number or counter == items_count
    except Exception:
        counter = len(browser.find_elements(By.XPATH, ("//div[@class='product-thumb']")))
        assert counter == 0


