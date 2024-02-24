from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_check_header_explicit(browser):
    browser.get("https://konflic.github.io/examples/pages/slowlyloading.html")
    # Какое ожидание победит?
    browser.implicitly_wait(1)
    wait = WebDriverWait(browser, 5)
    wait.until(EC.visibility_of_element_located((By.ID, "header")))

def test_check_header_implicit(browser):
    browser.implicitly_wait(5)
    browser.get("https://konflic.github.io/examples/pages/slowlyloading.html")
    browser.find_element(By.CSS_SELECTOR, "#header")


def test_check_title(browser):
    browser.get("https://konflic.github.io/examples/pages/slowlyloading.html")
    # Можно создать экземляр класса
    wait = WebDriverWait(browser, 10, poll_frequency=1)
    # И потом использовать ожидания от него
    wait.until(EC.title_is("Loaded!"))
    wait.until(EC.visibility_of_element_located((By.ID, "header")), message='')
    el = wait.until(EC.visibility_of_element_located((By.ID, "content")))
    wait.until(EC.text_to_be_present_in_element((By.ID, "content"), "This is else page content."))
    assert el.text == "This is else page content."


def test_check_magic_button(browser):
    browser.get("https://konflic.github.io/examples/pages/ajax.html")
    # Так как этот элемент не асинхронный, то можно не использовать ожиданий он загрузится вместо со страницей
    browser.find_element_by_name("showjsbutton").click()
    # Если метод возвращает элемент который ищет можно взять его ссылку
    js_button = WebDriverWait(browser, 3).until(EC.visibility_of_element_located((By.CLASS_NAME, "target")))
    js_button.click()
    WebDriverWait(browser, 2).until(EC.staleness_of(js_button))