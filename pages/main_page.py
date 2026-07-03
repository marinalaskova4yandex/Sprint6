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
        self.scroll_to_element(target_locator)
        self.click_element(target_locator)

    @allure.step("Получить текст ответа в аккордеоне с индексом {index}")
    def get_faq_answer_text(self, index):
        target_locator = MainPageLocators.ANSWERS[index]
        return self.get_text_from_element(target_locator)
    
    @allure.step("Нажать верхнюю кнопку 'Заказать' в шапке")
    def click_header_order_button(self):
        btn = self.wait_for_element(MainPageLocators.HEADER_ORDER_BUTTON)
        self.driver.execute_script("arguments[0].click();", btn)

    @allure.step("Нажать нижнюю кнопку 'Заказать' внизу страницы")
    def click_footer_order_button(self):
        # Плавно скроллим к нижней кнопке заказа
        self.scroll_to_element(MainPageLocators.FOOTER_ORDER_BUTTON)
        btn = self.wait_for_element(MainPageLocators.FOOTER_ORDER_BUTTON)
        self.driver.execute_script("arguments[0].click();", btn)
    @allure.step("Кликнуть по логотипу 'Самокат'")
    def click_scooter_logo(self):
        self.click_element(MainPageLocators.SCOOTER_LOGO)