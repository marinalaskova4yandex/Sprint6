import random
import time
import allure
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators import RentPageLocators, PopupLocators

class RentPage(BasePage):

    @allure.step("Заполнить вторую часть формы: Дата={date}, Срок аренды={duration_locator}, Комментарий={comment}")
    def fill_rent_data(self, date, duration_locator, comment):
        # Находим поле даты, заполняем и закрываем календарь
        date_field = self.send_keys_to_field(RentPageLocators.DATE_FIELD, date)
        date_field.send_keys(Keys.ENTER)

        # Вызываем метод выбора срока аренды, передавая туда локатор-кортеж из теста
        self.choose_rental_period(duration_locator)

        # Собираем список цветов из точных имен локаторов в locators.py
        scooter_colors = [
            RentPageLocators.BLACK_SCOOTER_CHECKBOX,
            RentPageLocators.GREY_SCOOTER_CHECKBOX
        ]
        # Выбираем случайный цвет самоката
        random_color = random.choice(scooter_colors)
        self.click_element(random_color)

        self.send_keys_to_field(RentPageLocators.COMMENT_FIELD, comment)

    @allure.step('Заполнить поле Срок аренды')
    def choose_rental_period(self, duration):
        # 1. Скроллим к полю "Срок аренды", чтобы оно было по центру экрана
        self.scroll_to_element(RentPageLocators.DURATION_FIELD)
        
        # 2. Находим элемент управления Dropdown-control
        duration_dropdown = self.wait_for_element(RentPageLocators.DURATION_FIELD)
        
        # 3. Двойная защита клика для Firefox: пробуем обычный клик, если перекрыт — жмем через JS
        try:
            duration_dropdown.click()
        except:
            self.driver.execute_script("arguments[0].click();", duration_dropdown)

        # 4. Ждем, когда в DOM появится раскрытое меню Dropdown-menu ( aria-expanded="true" )
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support import expected_conditions as EC
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "Dropdown-menu")))
        time.sleep(0.5)  # Небольшая пауза, чтобы элементы окончательно отрисовались

        # 5. Находим нужную опцию суток внутри меню по новому точному локатору
        option_element = self.wait.until(EC.presence_of_element_located(duration))
        
        # 6. Кликаем по суткам принудительно через JavaScript
        self.driver.execute_script("arguments[0].click();", option_element)
        time.sleep(0.5)

    @allure.step("Подтвердить заказ в попапах")
    def confirm_order(self):
        self.click_element(RentPageLocators.ORDER_BUTTON)
        self.click_element(PopupLocators.YES_BUTTON)

    @allure.step("Проверить появление окна об успешном создании заказа")
    def is_order_created_successfully(self):
        return self.is_element_displayed(PopupLocators.ORDER_CONFIRMED_POPUP)