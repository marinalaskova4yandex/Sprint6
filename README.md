# Проект автоматизации тестирования сервиса «Самокат» (Спринт 6)

Данный репозиторий содержит UI-автотесты, написанные на **Python** с использованием фреймворка **pytest** и паттерна проектирования **Page Object Model (POM)**. Для генерации детальных отчетов используется **Allure**.

## Архитектура проекта

- `pages/` — базовый класс страницы и классы страниц (MainPage, OrderPage, RentPage).
- `tests/` — тестовые сценарии (заказ самоката, проверка аккордеона FAQ).
- `locators.py` — локаторы элементов веб-интерфейса.
- `conftest.py` — конфигурация pytest и фикстура инициализации веб-драйвера (Firefox).

## Подготовка к запуску

1. **Клонируйте репозиторий:**
   ```bash
   git clone <url_вашего_репозитория>
   cd <имя_папки_проекта>
   ```

2. **Создайте и активируйте виртуальное окружение:**
   - На macOS/Linux:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
   - На Windows:
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```

3. **Установите необходимые зависимости:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Убедитесь, что у вас установлен браузер Firefox и Geckodriver.**

## Запуск тестов

*   **Обычный запуск тестов заказа самоката с очисткой кэша:**
    ```bash
    pytest tests/test_order.py -v -s --cache-clear
    ```

*   **Запуск всех тестов сбором данных для Allure-отчета:**
    ```bash
    pytest --alluredir=allure-results
    ```

*   **Генерация и просмотр Allure-отчета в браузере:**
    ```bash
    allure serve allure-results
    ```
