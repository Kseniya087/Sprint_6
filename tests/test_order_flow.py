import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage

class TestOrder:

    test_data = [("Анна","Иванова","ул.Мусы Джалиля,д.32", "Шипиловская", "89691234546", "20.10.2026", "сутки", "black", "Домофон 123"), ("Иван", "Петров", "ул.Ленина,д.23", "Бульвар Рокоссовского", "89512583669", "23.10.2026", "трое суток", "grey", "Позвонить за час")]

    allure.title("Позитивный сценарий заказа самоката")

    @pytest.mark.parametrize("entry_point", ["top", "bottom"])
    @pytest.mark.parametrize("name, surname, address, metro, phone, date, period, color, comment", test_data)

    def test_order_flow(self, driver, entry_point, name, surname, address, metro, phone, date, period, color, comment):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.open()
        main_page.accept_cookies()

        if entry_point == "top":
            main_page.click_top_order_button()
        else:
            main_page.click_bottom_order_button()

        order_page.fill_first_step(name, surname, address, metro, phone)
        order_page.fill_second_step(date, period, color, comment)

        order_page.click_finish_order_button()

        assert order_page.is_order_success(), "Окно 'Заказ оформлен' не появилось!"

        order_text = order_page.get_order_number()
        assert "Номер заказа:" in order_text, "Номер заказа не отобразился!"



