# 2.3 Использовать методы явного ожидания элементов
# Какие именно элементы проверять определить самостоятельно, но не меньше 5 для каждой страницы


from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# def test_check_header_explicit(browser):
#     browser.get("https://konflic.github.io/examples/pages/slowlyloading.html")
#     wait = WebDriverWait(browser, 5)
#     webelementtitle = wait.until(EC.visibility_of_element_located((By.ID, "Title")))


def test_check_title(browser):
    browser.get(browser.base_opencart_url)
    wait = WebDriverWait(browser, 5, poll_frequency=1)
    wait.until(EC.title_is("Your Store"))
    assert EC.title_is("Your Store")


    #assert title  "Your Store")
    # wait.until(EC.visibility_of_element_located((By.ID, "header")), message='')
    # el = wait.until(EC.visibility_of_element_located((By.ID, "content")))
    # wait.until(EC.text_to_be_present_in_element((By.ID, "content"), "This is else page content."))
    # assert el.text == "This is else page content."


# def test_check_magic_button(browser):
#     browser.get("https://konflic.github.io/examples/pages/ajax.html")
#     # Так как этот элемент не асинхронный, то можно не использовать ожиданий он загрузится вместо со страницей
#     browser.find_element_by_name("showjsbutton").click()
#     # Если метод возвращает элемент который ищет можно взять его ссылку
#     js_button = WebDriverWait(browser, 3).until(EC.visibility_of_element_located((By.CLASS_NAME, "target")))
#     js_button.click()
#     WebDriverWait(browser, 2).until(EC.staleness_of(js_button))