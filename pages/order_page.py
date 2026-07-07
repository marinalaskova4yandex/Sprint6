import allure
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators import OrderLocators

class OrderPage(BasePage):
    @allure.step("Заполнить первую форму заказа: Имя={name}, Фамилия={surname}, Адрес={address}, Метро={station}, Телефон={phone}")
    def fill_personal_data_form(self, name, surname, address, station, phone):
        self.send_keys_to_field(OrderLocators.NAME_FIELD, name)
        self.send_keys_to_field(OrderLocators.SURNAME_FIELD, surname)
        self.send_keys_to_field(OrderLocators.ADDRESS_FIELD, address)
        self.select_metro_station(station)
        self.send_keys_to_field(OrderLocators.PHONE_FIELD, phone)
        self.click_element(OrderLocators.NEXT_BUTTON)

    def select_metro_station(self, station):
        station_input = self.wait_for_element_presence(OrderLocators.STATION__FIELD)
        self.click_element(OrderLocators.STATION__FIELD)
        station_input.send_keys(station)
        
        dropdown = self.wait_for_element_presence(OrderLocators.STATION_DROPDOWN_LIST)
        self.wait.until(EC.element_to_be_clickable(dropdown))
        
        station_input.send_keys(Keys.DOWN)
        station_input.send_keys(Keys.ENTER)