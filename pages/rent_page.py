import random
import allure
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators import RentPageLocators, PopupLocators

class RentPage(BasePage):
    @allure.step("Заполнить вторую форму заказа: Дата={date}, Срок={duration_locator}, Комментарий={comment}")
    def fill_rent_data_form(self, date, duration_locator, comment):
        date_field = self.wait_for_element_presence(RentPageLocators.DATE_FIELD)
        self.send_keys_to_field(RentPageLocators.DATE_FIELD, date)
        date_field.send_keys(Keys.ENTER)
        
        self.choose_rental_period(duration_locator)
        self.select_random_color()
        self.send_keys_to_field(RentPageLocators.COMMENT_FIELD, comment)

    def choose_rental_period(self, duration_locator):
        self.scroll_to_element(RentPageLocators.DURATION_FIELD)
        self.click_via_action_chains(RentPageLocators.DURATION_FIELD)
        self.click_element(duration_locator)

    def select_random_color(self):
        colors = [RentPageLocators.BLACK_SCOOTER_CHECKBOX, RentPageLocators.GREY_SCOOTER_CHECKBOX]
        self.click_element(random.choice(colors))

    @allure.step("Подтвердить оформление заказа в модальном окне")
    def confirm_order(self):
        self.click_element(RentPageLocators.ORDER_BUTTON)
        self.click_element(PopupLocators.YES_BUTTON)

    @allure.step("Дождаться появления попапа успеха и получить его текст для проверки")
    def wait_and_get_order_confirmation_text(self):
        try:
            return self.get_element_text(PopupLocators.ORDER_CONFIRMED_POPUP)
        except:
            return self.get_element_text_content_via_js(PopupLocators.ORDER_CONFIRMED_POPUP)