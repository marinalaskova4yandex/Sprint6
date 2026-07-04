import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants import TestConstants
from locators import MainPageLocators

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, TestConstants.TIMEOUT_DEFAULT)

    @allure.step("Открыть главную страницу")
    def open(self):
        self.driver.get(TestConstants.BASE_URL)

    @allure.step("Принять cookie")
    def accept_cookies(self):
        try:
            cookie_btn = self.wait.until(EC.presence_of_element_located(MainPageLocators.COOKIE_BUTTON))
            self.execute_js_click(cookie_btn)
        except:
            pass

    @allure.step("Ожидать элемент по локатору: {locator}")
    def wait_for_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))    

    @allure.step("Прокрутить к элементу по локатору: {locator}")
    def scroll_to_element(self, locator):
        element = self.wait_for_element(locator)        
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'instant', block: 'center'});", element)
        return element
    
    @allure.step("Нажать на элемент по локатору: {locator}")
    def click_element(self, locator):        
        self.scroll_to_element(locator)
        element = self.wait_for_element(locator)
        self.execute_js_click(element)

    @allure.step("Заполнить поле по локатору: {locator}")
    def send_keys_to_field(self, locator, keys):
        field = self.wait_for_element(locator)
        field.clear()
        field.send_keys(keys)
        return field

    @allure.step("Получить текст по локатору: {locator}")
    def get_text_from_element(self, locator):
        element = self.wait_for_element(locator)
        text = element.text
        if not text:
            text = self.driver.execute_script("return arguments[0].textContent;", element)
        return text.strip() if text else ""

    @allure.step("Выполнить JS-клик на веб-элемент")
    def execute_js_click(self, element):
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Переключиться на самую последнюю открытую вкладку")
    def switch_to_next_tab(self):
        all_tabs = self.driver.window_handles
        self.driver.switch_to.window(all_tabs[-1])

    @allure.step("Ожидать, что URL содержит строку: {url_part}")
    def wait_until_url_contains(self, url_part):
        return self.wait.until(EC.url_contains(url_part))

    @allure.step("Получить текущий URL браузера")
    def get_current_url(self):
        return self.driver.current_url