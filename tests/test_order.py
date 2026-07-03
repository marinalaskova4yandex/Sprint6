import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from pages.rent_page import RentPage
from locators import OrderLocators, MainPageLocators, RentPageLocators, PopupLocators

@allure.suite("Спринт 6: Позитивный сценарий заказа самоката и проверка логотипов хедера")
class TestOrderScooterFlow:
    @allure.title("Заказ самоката через точку входа: {entry_point}")
    @allure.description("Проверяем полное оформление заказа с точным соответствием шагов ТЗ")
    @pytest.mark.parametrize(
        "entry_point, button_order, name, surname, address, station, duration, color_locator, phone, date, comment",
        [
            # Сценарий 1: кнопка в шапке, двое суток, черный самокат
            ("HEADER", MainPageLocators.HEADER_ORDER_BUTTON, "Иван", "Иванов", "ул. Ленина, 5", "Черкизовская", RentPageLocators.DURATION_TWO_DAYS, RentPageLocators.BLACK_SCOOTER_CHECKBOX, "79991112233", "12.12.2026", "Скорее"),
            # Сценарий 2: кнопка внизу, сутки, серый самокат
            ("FOOTER", MainPageLocators.FOOTER_ORDER_BUTTON, "Анна", "Петрова", "ул. Мира, 10", "Сокольники", RentPageLocators.DURATION_ONE_DAY, RentPageLocators.GREY_SCOOTER_CHECKBOX, "79110005566", "15.12.2026", "Жду")
        ]
    )
    def test_order_scooter_success_flow(self, driver, entry_point, button_order, name, surname, address, station, duration, color_locator, phone, date, comment):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        rent_page = RentPage(driver)
        
        # Шаг 1: Открываем сайт Самоката
        main_page.open()
        main_page.accept_cookies()
        
        # Шаг 2: Нажимаем кнопку заказа, переданную в параметрах (push_order_button)
        if entry_point == "HEADER":
            main_page.click_element(button_order)
        else:
            main_page.scroll_to_element(button_order)
            main_page.click_element(button_order)
            
        # Шаг 3: Заполняем первую форму персональными данными и метро
        order_page.send_keys_to_field(OrderLocators.NAME_FIELD, name)
        order_page.send_keys_to_field(OrderLocators.SURNAME_FIELD, surname)
        order_page.send_keys_to_field(OrderLocators.ADDRESS_FIELD, address)
        order_page.send_keys_to_station_field(station)
        order_page.send_keys_to_field(OrderLocators.PHONE_FIELD, phone)
        order_page.click_next()
        
        # Шаг 4: Передаем аргументы строго в соответствии с методом fill_rent_data страницы
        rent_page.fill_rent_data(date, duration, comment)
        rent_page.confirm_order()
        
        # Шаг 5: Обращаемся к PopupLocators 
        popup_text = rent_page.get_text_from_element(PopupLocators.ORDER_CONFIRMED_POPUP)
        assert rent_page.is_order_created_successfully(), f"Ошибка через кнопку '{entry_point}': Попап успеха не отображается!"
        assert "Заказ оформлен" in popup_text or "Статус заказа" in popup_text or "Посмотреть статус" in popup_text, f"Неожиданный текст в попапе: {popup_text}"
        print(f"\n[Успех] Тест пройден! Заказ оформлен через кнопку '{entry_point}'.")
        
        # Шаг 6: Проверяем возврат на главную страницу при клике на логотип «Самоката»
        main_page.click_element(MainPageLocators.SCOOTER_LOGO)
        main_page.wait_url_contains("https://qa-scooter.praktikum-services.ru/")
        assert main_page.get_current_url() == "https://qa-scooter.praktikum-services.ru/", "Логотип не вернул на главную!"

    @allure.title("Тест логотипа: Клик на логотип Яндекса перенаправляет на Дзен")
    @allure.description("Проверяем, что при клике на логотип Яндекса в новом окне открывается главная страница Дзена")
    def test_click_yandex_logo_opens_dzen(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.accept_cookies()
        
        # Кликаем по логотипу Яндекса напрямую через метод клика базового класса и локатор
        main_page.click_element(MainPageLocators.YANDEX_LOGO)
        main_page.switch_to_next_tab()
        
        # Ожидаем загрузку URL Дзена
        main_page.wait_url_contains("https://dzen.ru/") 
        
        current_url = main_page.get_current_url()
        assert "https://dzen.ru/" in current_url, f"Логотип Яндекса не открыл Дзен! Текущий URL: {current_url}"