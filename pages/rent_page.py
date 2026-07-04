import random
import allure
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators import RentPageLocators, PopupLocators
from selenium.webdriver.common.action_chains import ActionChains


class RentPage(BasePage):
    @allure.step("Заполнить вторую часть формы: Дата={date}, Срок аренды={duration_locator}, Комментарий={comment}")
    def fill_rent_data(self, date, duration_locator, comment):
        date_field = self.send_keys_to_field(RentPageLocators.DATE_FIELD, date)
        date_field.send_keys(Keys.ENTER)
        
        self.choose_rental_period(duration_locator)

        scooter_colors = [
            RentPageLocators.BLACK_SCOOTER_CHECKBOX,
            RentPageLocators.GREY_SCOOTER_CHECKBOX
        ]
        random_color = random.choice(scooter_colors)
        self.click_element(random_color)
        self.send_keys_to_field(RentPageLocators.COMMENT_FIELD, comment)

    @allure.step('Заполнить поле Срок аренды')
    def choose_rental_period(self, duration):        
        self.scroll_to_element(RentPageLocators.DURATION_FIELD)       
        
        field_element = self.wait.until(EC.visibility_of_element_located(RentPageLocators.DURATION_FIELD))
        
        actions = ActionChains(self.driver)
        actions.move_to_element(field_element).click().perform()
        
        # 4. Ожидаем появления кастомного элемента списка, переданного из теста
        target_option = self.wait.until(EC.presence_of_element_located(duration))
        self.wait.until(EC.element_to_be_clickable(duration))
        
        # 5. Кликаем по выбранному сроку (здесь JS-клик сработает отлично, так как пункт уже в DOM)
        self.execute_js_click(target_option)

    @allure.step("Подтвердить заказ в попапах")
    def confirm_order(self):
        self.click_element(RentPageLocators.ORDER_BUTTON)
        self.click_element(PopupLocators.YES_BUTTON)

    @allure.step("Получить текст подтверждения успешного заказа")
    def get_order_confirmation_text(self):        
        
        try:
            element = self.wait.until(EC.visibility_of_element_located(PopupLocators.ORDER_CONFIRMED_POPUP))
            text = element.text
            if not text:
                text = self.driver.execute_script("return arguments.textContent;", element)
            return text.strip()
        except:           
            
            backup_element = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "Order_ModalHeader__3FDaJ")))
            return backup_element.text.strip()