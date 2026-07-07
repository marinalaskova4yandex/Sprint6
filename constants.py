class Urls:
    """Адреса тестируемых окружений и внешних ресурсов"""
    BASE_URL = "https://qa-scooter.praktikum-services.ru/"
    DZEN_URL = "https://dzen.ru/"


class Timeouts:
    """Таймауты для явных ожиданий WebDriverWait"""
    DEFAULT = 7
    SHORT = 3


class ExpectedTexts:
    """Эталонные строки для валидации результатов в ассертах"""
    ORDER_CONFIRMED_MARKER = "Заказ оформлен"