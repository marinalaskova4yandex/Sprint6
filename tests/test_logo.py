import allure
from pages.main_page import MainPage
from constants import Urls

@allure.suite("Проверка кликов по логотипам в шапке сайта")
class TestHeaderLogosRedirects:

    @allure.title("Тест логотипа Самоката: Переход на главную страницу")
    @allure.description("Проверяем возврат пользователя на стартовую страницу из формы заказа")
    def test_click_scooter_logo_returns_to_home_page(self, driver):
        main_page = MainPage(driver)
        main_page.open_base_url()
        main_page.accept_cookies()
        
        main_page.click_header_order_button()
        main_page.click_scooter_logo()
        
        assert main_page.wait_and_get_home_url(Urls.BASE_URL) == Urls.BASE_URL, (
            "Ошибка! Клик на логотип 'Самокат' не вернул пользователя на главную страницу."
        )

    @allure.title("Тест логотипа Яндекса: Редирект на платформу Дзен")
    @allure.description("Проверяем открытие главной страницы Дзена в новой вкладке")
    def test_click_yandex_logo_opens_dzen(self, driver):
        main_page = MainPage(driver)
        main_page.open_base_url()
        main_page.accept_cookies()
        
        main_page.click_yandex_logo()
        main_page.switch_to_next_tab()
               
        actual_url = main_page.wait_and_get_dzen_url("dzen.ru")
        
        assert "dzen.ru" in actual_url, (
            f"Ошибка! В новой вкладке открылся сторонний ресурс вместо Дзена. Получено: {actual_url}"
        )