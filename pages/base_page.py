import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from constants import Timeouts, Urls
from locators import MainPageLocators

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, Timeouts.DEFAULT)

    @allure.step("Открыть главную страницу сайта")
    def open_base_url(self):
        self.driver.get(Urls.BASE_URL)

    @allure.step("Принять cookie-файлы")
    def accept_cookies(self):
        try:
            cookie_btn = self.wait.until(EC.presence_of_element_located(MainPageLocators.COOKIE_BUTTON))
            self.execute_js_click(cookie_btn)
        except:
            pass

    @allure.step("Ожидать присутствия элемента в DOM")
    def wait_for_element_presence(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    @allure.step("Ожидать видимости элемента на экране")
    def wait_for_element_visibility(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Прокрутить страницу к элементу")
    def scroll_to_element(self, locator):
        element = self.wait_for_element_presence(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'instant', block: 'center'});", element)
        return element

    @allure.step("Выполнить клик по элементу")
    def click_element(self, locator):
        self.scroll_to_element(locator)
        element = self.wait_for_element_presence(locator)
        self.execute_js_click(element)

    @allure.step("Выполнить физический клик мыши через ActionChains")
    def click_via_action_chains(self, locator):
        element = self.wait_for_element_visibility(locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()

    @allure.step("Выполнить физический клик мыши без предварительного скролла")
    def click_via_action_chains_without_scroll(self, locator):
        element = self.wait_for_element_visibility(locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()

    @allure.step("Заполнить текстовое поле ввода")
    def send_keys_to_field(self, locator, keys):
        field = self.wait_for_element_presence(locator)
        field.clear()
        field.send_keys(keys)

    @allure.step("Получить text контент элемента")
    def get_element_text(self, locator):
        element = self.wait_for_element_visibility(locator)
        return element.text.strip()

    @allure.step("Получить textContent элемента через скрипт")
    def get_element_text_content_via_js(self, locator):
        element = self.wait_for_element_visibility(locator)
        text = self.driver.execute_script("return arguments[0].textContent;", element)
        return text.strip() if text else ""

    @allure.step("Выполнить JavaScript-клик")
    def execute_js_click(self, element):
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Переключиться на последнюю открытую вкладку")
    def switch_to_next_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    @allure.step("Дождаться изменения URL")
    def wait_until_url_contains(self, url_part):
        return self.wait.until(EC.url_contains(url_part))

    @allure.step("Получить текущий адрес URL из браузера")
    def get_current_url(self):
        return self.driver.current_url