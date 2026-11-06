import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class MainPage(BasePage):
    URL = "https://qa-scooter.praktikum-services.ru/"

    TOP_ORDER_BUTTON = (By.XPATH, "//div[contains(@class,'Header_Nav')]//button[text()='Заказать']")
    BOTTOM_ORDER_BUTTON = (By.XPATH, "//div[contains(@class,'Home_FinishButton')]//button[text()='Заказать']")
    SAMOKAT_LOGO = (By.XPATH, "//a[contains(@class, 'Header_LogoScooter')]")
    YANDEX_LOGO = (By.XPATH, "//a[contains(@class, 'Header_LogoYandex')]")

    FAQ_QUESTION = (By.XPATH, "//div[contains(@id,'accordion__heading-{index}')]")
    FAQ_ANSWER = (By.XPATH, "//div[contains(@id,'accordion__panel-{index}')]")

    COOKIE_ACCEPT_BUTTON = (By.ID, "rcc-confirm-button")

    @allure.step("Открыть главную страницу")
    def open(self):
        self.driver.get(self.URL)
        return self

    @allure.step("Принять куки (если появились)")
    def accept_cookies(self):
        try:
            self.click((By.ID, "rcc-confirm-button"))
        except Exception:
            pass

    @allure.step("Нажать на кнопку 'Заказать'")
    def click_order_button(self, button_locator):
        self.click(button_locator)

    @allure.step("Кликнуть на логотип Самоката")
    def click_samokat_logo(self):
        self.click(self.SAMOKAT_LOGO)

    @allure.step("Кликнуть на логотип Яндекса")
    def click_yandex_logo(self):
        self.click(self.YANDEX_LOGO)

    @allure.step("Кликнуть на вопрос в FAQ с индексом {index}")
    def click_faq_question(self, index):
        locator = (self.FAQ_QUESTION[0], self.FAQ_QUESTION[1].format(index=index))
        self.scroll_to_element(locator)
        self.click(locator)

    @allure.step("Получить текст ответа в FAQ с индексом {index}")
    def get_faq_answer(self, index):
        locator = (self.FAQ_ANSWER[0], self.FAQ_ANSWER[1].format(index=index))
        return self.get_text(locator)