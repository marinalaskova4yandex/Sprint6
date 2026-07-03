import allure
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators import OrderLocators

class OrderPage(BasePage):

    @allure.step("Заполнить первую часть формы: Имя={name}, ...")
    def fill_personal_data(self, name, surname, address, station, phone):
        self.send_keys_to_field(OrderLocators.NAME_FIELD, name)
        self.send_keys_to_field(OrderLocators.SURNAME_FIELD, surname)
        self.send_keys_to_field(OrderLocators.ADDRESS_FIELD, address)
        
        # Вызываем метод заполнения станции метро через клавиатуру
        self.send_keys_to_station_field(station)
        
        self.send_keys_to_field(OrderLocators.PHONE_FIELD, phone)

    @allure.step("Заполнить поле Станция метро")
    def send_keys_to_station_field(self, station):
        import time

        # 1. Находим поле ввода и кликаем по нему, чтобы активировать фокус
        station_input = self.wait_for_element(OrderLocators.STATION__FIELD)
        self.click_element(OrderLocators.STATION__FIELD)
        
        # 2. Вводим текст названия станции
        station_input.send_keys(station)
        
        # 3. Ждем появления выпадающего списка
        self.wait_for_element(OrderLocators.STATION_DROPDOWN_LIST)
        time.sleep(0.5)  # Небольшая пауза, чтобы список успел отфильтроваться в Firefox
        
        # 4. Отправляем системную стрелку ВНИЗ напрямую в инпут (выбирает первую строчку)
        station_input.send_keys(Keys.DOWN)
        time.sleep(0.2)
        
        # 5. Отправляем ENTER напрямую в инпут для подтверждения выбора
        station_input.send_keys(Keys.ENTER)
        time.sleep(0.5)  # Время на то, чтобы форма Самоката обновила статус валидации поля

    @allure.step("Нажать кнопку 'Далее'")
    def click_next(self):
        self.click_element(OrderLocators.NEXT_BUTTON)