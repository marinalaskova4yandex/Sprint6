import allure
from pages.base_page import BasePage
from locators import MainPageLocators

class MainPage(BasePage):
    @allure.step("Проскроллить страницу к блоку FAQ")
    def scroll_to_faq_block(self):
        self.scroll_to_element(MainPageLocators.FAQ_BLOCK)

    @allure.step("Раскрыть вопрос аккордеона с индексом {index}")
    def expand_faq_question(self, index):
        self.click_element(MainPageLocators.QUESTIONS[index])

    @allure.step("Получить текст ответа аккордеона с индексом {index}")
    def get_faq_answer_text(self, index):
        return self.get_element_text(MainPageLocators.ANSWERS[index])

    @allure.step("Нажать на верхнюю кнопку заказа в шапке (через ActionChains без скролла)")
    def click_header_order_button_via_actions(self):
        self.click_via_action_chains_without_scroll(MainPageLocators.HEADER_ORDER_BUTTON)

    @allure.step("Нажать на нижнюю кнопку заказа в футере (через ActionChains со скроллом)")
    def click_footer_order_button_via_actions(self):
        self.scroll_to_element(MainPageLocators.FOOTER_ORDER_BUTTON)
        self.click_via_action_chains(MainPageLocators.FOOTER_ORDER_BUTTON)

    @allure.step("Нажать на верхнюю кнопку заказа стандартным методом")
    def click_header_order_button(self):
        self.click_element(MainPageLocators.HEADER_ORDER_BUTTON)

    @allure.step("Нажать на логотип Яндекса")
    def click_yandex_logo(self):
        self.click_via_action_chains(MainPageLocators.YANDEX_LOGO_IMAGE)

    @allure.step("Нажать на логотип Самоката")
    def click_scooter_logo(self):
        self.click_element(MainPageLocators.SCOOTER_LOGO)

    @allure.step("Дождаться перенаправления и получить итоговый URL Дзена в ассерт")
    def wait_and_get_dzen_url(self, expected_url):
        self.wait_until_url_contains("dzen")
        return self.get_current_url()

    @allure.step("Дождаться возврата и получить итоговый корневой URL в ассерт")
    def wait_and_get_home_url(self, expected_url):
        self.wait_until_url_contains(expected_url)
        return self.get_current_url()