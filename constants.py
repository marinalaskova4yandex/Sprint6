class TestConstants:
    """Глобальные константы для тестовой среды"""
    BASE_URL = "https://qa-scooter.praktikum-services.ru/"
    DZEN_URL = "https://dzen.ru/"
    
    # Таймауты для WebDriverWait
    TIMEOUT_DEFAULT = 7
    TIMEOUT_SHORT = 3
    
    # Ожидаемые эталоны текстов для проверок
    ORDER_CONFIRMED_MARKER = "Заказ оформлен"