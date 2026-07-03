import pytest
import allure
from pages.main_page import MainPage
from locators import MainPageLocators

@allure.suite("Спринт 6: Проверка выпадающих списков FAQ")
class TestMainPageFaq:

    @allure.title("Тест FAQ: Вопрос и ответ № {index}")
    @allure.description("Проверяем раскрытие аккордеона и переход на Дзен через логотип Яндекса")
    @pytest.mark.parametrize(
        "index, expected_answer",
        [
            (0, "Сутки — 400 рублей. Оплата курьеру — наличными или картой."),
            (1, "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."),
            (2, "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."),
            (3, "Только начиная с завтрашнего дня. Но скоро станем расторопнее."),
            (4, "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."),
            (5, "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."),
            (6, "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."),
            (7, "Да, обязательно. Всем самокатов! И Москве, и Московской области.")
        ]
    )
    def test_faq_dropdown_items(self, driver, index, expected_answer):
        main_page = MainPage(driver)
        
        # Выполнение сценария FAQ
        main_page.open()
        main_page.accept_cookies()
        main_page.scroll_to_faq_block()
        main_page.expand_faq_question(index)
        actual_answer = main_page.get_faq_answer_text(index)
        
        assert actual_answer == expected_answer, f"Ошибка на индексе {index}!"
        
        # ПРОВЕРКА ЛОГОТИПА ЯНДЕКСА (ДЗЕН) ДЛЯ ТЕСТОВ FAQ
        main_page.click_element(MainPageLocators.YANDEX_LOGO)
        main_page.switch_to_next_tab()
        main_page.wait_url_contains("https://dzen.ru/")
        assert "https://dzen.ru/" in main_page.get_current_url(), "Логотип Яндекса не открыл Дзен!"