import allure
import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage

test_data = [
    # Набор 1 (для верхней кнопки)
    ("Анна", "Иванова", "ул. Льва Толстого, д. 12", "Черкизовская", "89999999999", "11.11.2026", "сутки", "black", "Домофон 123, позвонить за час"),
    # Набор 2 (для нижней кнопки)
    ("Иван", "Петров", "ул. Пушкина, д. 5", "Арбатская", "88888888888", "15.11.2026", "двое суток", "grey", "Оставить у подъезда")
]


class TestOrder:

    @allure.title("Оформление заказа через {button_name}")
    @pytest.mark.parametrize("order_button, button_name, client_data", [
        pytest.param(MainPage.TOP_ORDER_BUTTON, "верхнюю кнопку", test_data[0], id="top_button"),
        pytest.param(MainPage.BOTTOM_ORDER_BUTTON, "нижнюю кнопку", test_data[1], id="bottom_button")
    ])
    def test_order_flow(self, driver, order_button, button_name, client_data):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        
        with allure.step(f"Нажать на {button_name}"):
            main_page.open()
            main_page.accept_cookies()
            main_page.click_order_button(order_button)

        
        name, surname, address, metro, phone, date, period, color, comment = client_data

        
        order_page.fill_first_step(name, surname, address, metro, phone)
        order_page.fill_second_step(date, period, color, comment)
        order_page.click_finish_order_button()

        assert order_page.is_order_success(), "Ошибка: Окно с сообщением об успешном заказе не появилось"

