from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class MainPage:
    URL = "https://qa-scooter.praktikum-services.ru/"

    TOP_ORDER_BUTTON = (By.XPATH, "//div[contains(@class,'Header_Nav')]//button[text()='Заказать']")
    BOTTOM_ORDER_BUTTON = (By.XPATH, "//div[contains(@class,'Home_FinishButton')]//button[text()='Заказать']")
    SAMOKAT_LOGO = (By.XPATH, "//a[contains(@class, 'Header_LogoScooter')]")
    YANDEX_LOGO = (By.XPATH, "//a[contains(@class, 'Header_LogoYandex')]")

    FAQ_QUESTOIN = (By.XPATH, "//div[contains(@id,'accordion__heading-{index}')]")
    FAQ_ANSWER = (By.XPATH, "//div[contains(@id,'accordion__panel-{index}')]")

    COOKIE_ACCEPT_BUTTON = (By.ID, "rcc-confirm-button")
    


    def __init__(self, driver):
        self.driver = driver

        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(self.URL)
        return self

    def accept_cookies(self):
            try:
                cookie_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "rcc-confirm-button")))
                cookie_button.click()
            except Exception:
                try:
                    self.driver.execute_script("arguments[0].clicl();", cookie_button)
                except Exception:
                    pass

    def click_top_order_button(self):
        self.driver.find_element(*self.TOP_ORDER_BUTTON).click()

    def click_bottom_order_button(self):
        self.driver.find_element(*self.BOTTOM_ORDER_BUTTON).click()

    def click_samokat_logo(self):
        self.driver.find_element(*self.SAMOKAT_LOGO).click()

    def click_yandex_logo(self):
        self.driver.find_element(*self.YANDEX_LOGO).click()

    def click_faq_question(self, index):
        locator = (By.XPATH, f"//div[contains(@id,'accordion__heading-{index}')]")

        question_element = self.driver.find_element(*locator)

        self.driver.execute_script("arguments[0].scrollIntoView();", question_element)

        self.wait.until(EC.element_to_be_clickable(locator)).click()


    def get_faq_answer(self, index):
        locator = (By.XPATH, f"//div[contains(@id,'accordion__panel-{index}')]//p")
        return self.wait.until(EC.visibility_of_element_located(locator)).text

