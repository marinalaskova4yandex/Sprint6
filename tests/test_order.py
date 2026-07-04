import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from pages.rent_page import RentPage
from locators import OrderLocators, MainPageLocators, RentPageLocators
from constants import TestConstants

@allure.suite("Спринт 6: Позитивные UI-сценарии и переходы")
class TestOrderScooterFlow:

    @allure.title("Заказ самоката через точку входа: {entry_point}")
    @allure.description("Проверяем полное оформление заказа. Маркер успеха ожидается внутри ассерта.")
    @pytest.mark.parametrize(
        "entry_point, button_order, name, surname, address, station, duration, phone, date, comment",
        [
            ("HEADER", MainPageLocators.HEADER_ORDER_BUTTON, "Иван", "Иванов", "ул. Ленина, 5", "Черкизовская", RentPageLocators.DURATION_TWO_DAYS, "79991112233", "12.12.2026", "Скорее"),
            ("FOOTER", MainPageLocators.FOOTER_ORDER_BUTTON, "Анна", "Петрова", "ул. Мира, 10", "Сокольники", RentPageLocators.DURATION_ONE_DAY, "79110005566", "15.12.2026", "Жду")
        ]
    )
    def test_order_scooter_success_flow(self, driver, entry_point, button_order, name, surname, address, station, duration, phone, date, comment):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        rent_page = RentPage(driver)
        
        main_page.open()
        main_page.accept_cookies()
        
        # Исправлено: Физические клики мыши через ActionChains для обеих точек входа
        from selenium.webdriver.common.action_chains import ActionChains
        
        if entry_point == "HEADER":
            order_btn = main_page.wait_for_element(button_order)
            actions = ActionChains(driver)
            actions.move_to_element(order_btn).click().perform()
        else:
            main_page.scroll_to_element(button_order)
            order_btn = main_page.wait_for_element(button_order)
            actions = ActionChains(driver)
            actions.move_to_element(order_btn).click().perform()
            
        order_page.send_keys_to_field(OrderLocators.NAME_FIELD, name)
        order_page.send_keys_to_field(OrderLocators.SURNAME_FIELD, surname)
        order_page.send_keys_to_field(OrderLocators.ADDRESS_FIELD, address)
        order_page.send_keys_to_station_field(station)
        order_page.send_keys_to_field(OrderLocators.PHONE_FIELD, phone)
        order_page.click_next()
        
        rent_page.fill_rent_data(date, duration, comment)
        rent_page.confirm_order()
        
        # Однозначный ассерт. Взаимодействие с маркером успеха происходит прямо внутри проверки
        actual_popup_text = rent_page.get_order_confirmation_text()
        assert TestConstants.ORDER_CONFIRMED_MARKER in actual_popup_text, (
            f"Ошибка! Текст '{TestConstants.ORDER_CONFIRMED_MARKER}' не найден в попапе. Получено: '{actual_popup_text}'"
        )

    @allure.title("Тест логотипа Самоката: Возврат на главную страницу")
    @allure.description("Атомарный тест: клик по логотипу 'Самокат' из формы заказа должен возвращать на корневой URL")
    def test_click_scooter_logo_returns_to_home_page(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.accept_cookies()
        main_page.click_element(MainPageLocators.HEADER_ORDER_BUTTON)
        
        main_page.click_element(MainPageLocators.SCOOTER_LOGO)
        
        main_page.wait_until_url_contains(TestConstants.BASE_URL)
        assert main_page.get_current_url() == TestConstants.BASE_URL, "Логотип не вернул пользователя на главную страницу!"

    @allure.title("Тест логотипа Яндекса: Перенаправление на Дзен")
    @allure.description("Атомарный тест: проверка перехода на Дзен в новой вкладке при клике на логотип Яндекса")
    def test_click_yandex_logo_opens_dzen(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.accept_cookies()
        
        from selenium.webdriver.common.action_chains import ActionChains
        
        # Используем локатор картинки из класса MainPageLocators
        ya_logo_img = main_page.wait_for_element(MainPageLocators.YANDEX_LOGO_IMAGE)
        
        # Физический клик мыши через ActionChains
        actions = ActionChains(driver)
        actions.move_to_element(ya_logo_img).click().perform()
        
        main_page.switch_to_next_tab()
        main_page.wait_until_url_contains(TestConstants.DZEN_URL)
            
        current_url = main_page.get_current_url()
        assert TestConstants.DZEN_URL in current_url, f"Логика перехода нарушена! Ожидали: {TestConstants.DZEN_URL}, получили: {current_url}"