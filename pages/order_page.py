import allure
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators import OrderLocators

class OrderPage(BasePage):
    @allure.step("Заполнить поле Станция метро через клавиатуру")
    def send_keys_to_station_field(self, station):
        station_input = self.wait_for_element(OrderLocators.STATION__FIELD)
        self.click_element(OrderLocators.STATION__FIELD)
        station_input.send_keys(station)
        
        # Замена слипа: ждем, пока элемент выпадающего списка станет видимым/активным
        dropdown = self.wait_for_element(OrderLocators.STATION_DROPDOWN_LIST)
        self.wait.until(EC.element_to_be_clickable(dropdown))
        
        station_input.send_keys(Keys.DOWN)
        station_input.send_keys(Keys.ENTER)

    @allure.step("Нажать кнопку 'Далее'")
    def click_next(self):
        self.click_element(OrderLocators.NEXT_BUTTON)