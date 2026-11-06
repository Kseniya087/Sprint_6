import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import MainPage

class TestNavigation:
    @allure.title("Проверка возврата на главную по логотипу Самоката")
    def test_samokat_logo_returns_to_main(self, driver):
        main_page = MainPage(driver)
        main_page.open()

        main_page.click_samokat_logo()

        assert main_page.get_current_url() == main_page.URL, "Логотип Самоката не ведет на главную!"


    @allure.title("Проверка открытия Дзена по логотипу Яндекса")
    def test_yandex_logo_opens_dzen(self, driver):
        main_page = MainPage(driver)
        main_page.open()
    
        main_page.click_yandex_logo()

        WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))  
        new_window = driver.window_handles[-1]
        driver.switch_to.window(new_window)
    
        WebDriverWait(driver, 10).until(EC.url_contains("dzen.ru"))
        assert "dzen.ru" in main_page.get_current_url(), "По клику на логотип Яндекса не открылся Дзен"