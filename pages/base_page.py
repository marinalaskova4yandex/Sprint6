import time
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        # Инициализируем явное ожидание на 7 секунд для медленной анимации в Firefox
        self.wait = WebDriverWait(driver, 7)
        self.URL = "https://qa-scooter.praktikum-services.ru/"

    @allure.step("Открыть страницу")
    def open(self):
        self.driver.get(self.URL)
    
    @allure.step('Принять cookie')
    def accept_cookies(self):
        try:
            from locators import MainPageLocators
            cookie_btn = self.wait.until(EC.presence_of_element_located(MainPageLocators.COOKIE_BUTTON))
            self.driver.execute_script("arguments[0].click();", cookie_btn)
            time.sleep(0.5)
        except:
            pass

    @allure.step("Проверить отображение элемента {locator}")
    def is_element_displayed(self, locator):
        try:
            return self.wait.until(EC.presence_of_element_located(locator)).is_displayed()
        except:
            return False

    @allure.step('Ожидать элемент по локатору: {locator}')
    def wait_for_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))
    
    @allure.step('Нажать на элемент по локатору: {locator}')
    def click_element(self, locator):
        # Самое стабильное решение: ждем присутствия и кликаем через JS
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step('Прокрутить элемент по локатору: {locator}')
    def scroll_to_element(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)
        time.sleep(0.8)  # Пауза на анимацию скролла
        return element
    
    @allure.step('Заполнить поле по локатору: {locator}')
    def send_keys_to_field(self, locator, keys):
        field = self.wait.until(EC.presence_of_element_located(locator))
        field.clear()  # Предварительно очищаем поле
        field.send_keys(keys)
        return field

    @allure.step('Получить текст по локатору: {locator}')
    def get_text_from_element(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        time.sleep(0.3)
        text = element.text
        if not text:
            text = self.driver.execute_script("return arguments[0].textContent;", element)
        return text.strip()
    
    @allure.step('Получить текущий URL')
    def get_current_url(self):
        return self.driver.current_url

    # ================= ДОПИСАННЫЕ МЕТОДЫ, КОТОРЫХ НЕ ХВАТАЛО =================

    @allure.step('Ожидать появления части url')
    def wait_url_contains(self, url_part):
        """Ожидает, пока текущий URL-адрес браузера будет содержать указанную строку."""
        return self.wait.until(EC.url_contains(url_part))

    @allure.step('Переключиться на новую вкладку')
    def switch_to_next_tab(self):
        """Переключает фокус Selenium на самую последнюю открытую вкладку браузера."""
        all_tabs = self.driver.window_handles
        self.driver.switch_to.window(all_tabs[-1])