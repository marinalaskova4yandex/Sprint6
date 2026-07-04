import allure
from pages.base_page import BasePage
from locators import MainPageLocators

class MainPage(BasePage):
    @allure.step("Проскроллить до блока FAQ")
    def scroll_to_faq_block(self):
        self.scroll_to_element(MainPageLocators.FAQ_BLOCK)

    @allure.step("Развернуть вопрос в аккордеоне с индексом {index}")
    def expand_faq_question(self, index):
        target_locator = MainPageLocators.QUESTIONS[index]
        # Используем наш обновленный стабильный клик
        self.click_element(target_locator)

    @allure.step("Получить текст ответа в аккордеоне с индексом {index}")
    def get_faq_answer_text(self, index):
        target_locator = MainPageLocators.ANSWERS[index]
        return self.get_text_from_element(target_locator)

    @allure.step("Нажать верхнюю кнопку 'Заказать' в шапке")
    def click_header_order_button(self):
        self.click_element(MainPageLocators.HEADER_ORDER_BUTTON)

    @allure.step("Нажать нижнюю кнопку 'Заказать' внизу страницы")
    def click_footer_order_button(self):
        self.scroll_to_element(MainPageLocators.FOOTER_ORDER_BUTTON)
        self.click_element(MainPageLocators.FOOTER_ORDER_BUTTON)