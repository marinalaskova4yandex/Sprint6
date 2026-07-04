from selenium.webdriver.common.by import By

class MainPageLocators:
    """ГРУППА 1: Локаторы Главной страницы (Шапки и Конструктора)"""
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button") 
    FAQ_BLOCK = (By.CLASS_NAME, "accordion")  
    SCOOTER_LOGO = (By.XPATH, "//a[contains(@class, 'Header_LogoScooter')]")
    YANDEX_LOGO = (By.XPATH, "//a[contains(@class, 'Header_LogoYandex')]")

    HEADER_ORDER_BUTTON = (By.XPATH, "//button[contains(@class, 'Button_Button') and text()='Заказать']")
    FOOTER_ORDER_BUTTON = (By.XPATH, "//div[contains(@class, 'Home_FinishButton') or contains(@class, 'Home_Finish')]//button[text()='Заказать']")

    QUESTIONS = [(By.ID, f"accordion__heading-{i}") for i in range(8)]
    ANSWERS = [(By.ID, f"accordion__panel-{i}") for i in range(8)]

    YANDEX_LOGO_IMAGE = (By.CSS_SELECTOR, "img[alt='Yandex']")


class OrderLocators:
    """ГРУППА 2: Локаторы первой страницы формы ('Для кого самокат')"""
    NAME_FIELD = (By.XPATH, '//input[@placeholder="* Имя"]')
    SURNAME_FIELD = (By.XPATH, '//input[@placeholder="*  Фамилия" or @placeholder="* Фамилия"]')
    ADDRESS_FIELD = (By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]')
    PHONE_FIELD = (By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]')
    NEXT_BUTTON = (By.XPATH, '//button[text()="Далее"]')
    STATION__FIELD = (By.XPATH, '//input[@placeholder="* Станция метро"]')
    STATION_DROPDOWN_LIST = (By.XPATH, ".//div[@class='select-search__select']")


class RentPageLocators:
    """ГРУППА 3: Локаторы второй страницы формы ('Про аренду')"""
    DATE_FIELD = (By.XPATH, '//input[@placeholder="* Когда привезти самокат"]')

    # Нажимаем на саму область управления, которая открывает список
   #DURATION_FIELD = (By.XPATH, "//div[@class='Dropdown-control']")
    DURATION_FIELD = (By.CLASS_NAME, "Dropdown-control")

    # Ищем опции внутри раскрытого меню Dropdown-menu строго с маленькой буквы
    DURATION_ONE_DAY = (By.XPATH, "//div[@class='Dropdown-menu']//div[text()='сутки']")
    DURATION_TWO_DAYS = (By.XPATH, "//div[@class='Dropdown-menu']//div[text()='двое суток']")
    DURATION_THREE_DAYS = (By.XPATH, "//div[@class='Dropdown-menu']//div[text()='трое суток']")

    BLACK_SCOOTER_CHECKBOX = (By.ID, "black")
    GREY_SCOOTER_CHECKBOX = (By.ID, "grey")
    COMMENT_FIELD = (By.XPATH, '//input[@placeholder="Комментарий для курьера"]')
    ORDER_BUTTON = (By.XPATH, '//div[contains(@class, "Order_Buttons")]//button[text()="Заказать"]')


class PopupLocators:
    """ГРУППА 4: Локаторы всплывающих модальных окон подтверждения и статуса"""
    CONFIRM_ORDER_POPUP_TITLE = (By.XPATH, '//div[text()="Хотите оформить заказ?"]')
    YES_BUTTON = (By.XPATH, '//button[text()="Да"]')
    ORDER_CONFIRMED_POPUP = (By.XPATH, '//*[contains(text(), "Заказ оформлен") or contains(text(), "Посмотреть статус")]')