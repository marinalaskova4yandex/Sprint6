import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from pages.rent_page import RentPage
from locators import RentPageLocators
from constants import ExpectedTexts, Urls

@allure.suite("Позитивные UI-сценарии оформления заказов")
class TestOrderScooterFlow:

    @allure.title("Заказ самоката через верхнюю точку входа (Шапка сайта)")
    @allure.description("Проверяем успешный сквозной заказ при клике на кнопку в хедере страницы")
    def test_order_scooter_via_header_button(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        rent_page = RentPage(driver)
        
        main_page.open_base_url()
        main_page.accept_cookies()
        main_page.click_header_order_button_via_actions()
        
        order_page.fill_personal_data_form("Иван", "Иванов", "ул. Ленина, 5", "Черкизовская", "79991112233")
        rent_page.fill_rent_data_form("12.12.2026", RentPageLocators.DURATION_TWO_DAYS, "Скорее")
        rent_page.confirm_order()
        
        assert ExpectedTexts.ORDER_CONFIRMED_MARKER in rent_page.wait_and_get_order_confirmation_text(), (
            f"Ошибка! Маркер '{ExpectedTexts.ORDER_CONFIRMED_MARKER}' отсутствует в финальном попапе подтверждения."
        )

    @allure.title("Заказ самоката через нижнюю точку входа (Футер сайта)")
    @allure.description("Проверяем успешный сквозной заказ при клике на кнопку внизу страницы")
    def test_order_scooter_via_footer_button(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        rent_page = RentPage(driver)
        
        main_page.open_base_url()
        main_page.accept_cookies()
        main_page.click_footer_order_button_via_actions()
        
        order_page.fill_personal_data_form("Анна", "Петрова", "ул. Мира, 10", "Сокольники", "79110005566")
        rent_page.fill_rent_data_form("15.12.2026", RentPageLocators.DURATION_ONE_DAY, "Жду")
        rent_page.confirm_order()
        
        assert ExpectedTexts.ORDER_CONFIRMED_MARKER in rent_page.wait_and_get_order_confirmation_text(), (
            f"Ошибка! Маркер '{ExpectedTexts.ORDER_CONFIRMED_MARKER}' отсутствует в финальном попапе подтверждения."
        )