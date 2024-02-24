import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FFOptions


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--headless", action="store_true")
    parser.addoption("--base_opencart_url", default="http://localhost/oc/")


@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    base_opencart_url = request.config.getoption("--base_opencart_url")

    driver = None

    if browser_name == "chrome":
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
        service = ChromeService()
        driver = webdriver.Chrome(service=service,options=options)
    elif browser_name == "ff":
        options = FFOptions()
        if headless:
            options.add_argument("-headless")
        driver = webdriver.Firefox(options=options)
    elif browser_name == "ya":
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
        binary_yandex_driver_file = '../drivers/yandexdriver.exe'
        driver = webdriver.Chrome(binary_yandex_driver_file, options=options)
    driver.maximize_window()
    driver.base_opencart_url = base_opencart_url
    yield driver
    driver.close()
