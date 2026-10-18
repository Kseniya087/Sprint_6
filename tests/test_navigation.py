import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import MainPage

class TestNavigation:
    allure.title("Проверка возврата на главную по логотипу Самоката")
    def test_samokat_logo_returns_to_main(self, driver):
        main_page = MainPage(driver)
        main_page.open()

        main_page.click_samokat_logo()

        assert driver.current_url == main_page.URL, "Логотип Самоката не ведет на главную!"


    allure.title("Проверка открытия Дзена по логотипу Яндекса")
    def test_yandex_logo_opens_dzen(self, driver):
        main_page = MainPage(driver)
        main_page.open()

        original_window = driver.current_window_handle

        main_page.click_yandex_logo()

        WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))

        for window_handle in driver.window_handles:
            if window_handle != original_window:
                driver.switch_to.window(window_handle)
                break

        WebDriverWait(driver, 10).until(EC.url_contains("dzen.ru"))
        assert "dzen.ru" in driver.current_url, "Страница Дзена не открылась!"

        driver.close()
        driver.switch_to.window(original_window)
    