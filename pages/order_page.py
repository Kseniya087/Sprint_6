from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class OrderPage:
    ORDER_URL = "https://qa-scooter.praktikum-services.ru/order"
    STATUS_URL = "https://qa-scooter.praktikum-services.ru/track?t={order_numnber}"

    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")
    PHONE_INPUT = (By.XPATH,"//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_DROPDOWN = (By.XPATH, "//div[contains(@class, 'Dropdown-control')]")
    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    FINISH_ORDER_BUTTON = (By.XPATH, "//button[contains(@class,'Button_Middle') and text()='Заказать']")
    
    CONFIRM_YES_BUTTON = (By.XPATH, "//button[text()='Да']")
    SUCCESS_HEADER= (By.XPATH, "//div[contains(text(),'Заказ оформлен')]")
    ORDER_NUMBER_TEXT = (By.XPATH, "//div[contains(text(),'Номер заказа')]")
    VIEW_STATUS_BUTTON = (By.XPATH,"//button[text()='Посмотреть статус']")


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def fill_first_step(self, name, surname,address,metro, phone):
        self.driver.find_element(*self.NAME_INPUT).send_keys(name)
        self.driver.find_element(*self.SURNAME_INPUT).send_keys(surname)
        self.driver.find_element(*self.ADDRESS_INPUT).send_keys(address)
        self.select_metro(metro)
        self.driver.find_element(*self.PHONE_INPUT).send_keys(phone)
        self.driver.find_element(*self.NEXT_BUTTON).click()

    def select_metro(self, station_name):
        metro_input = self.driver.find_element(*self.METRO_INPUT)
        metro_input.send_keys(station_name)

        locator = (By.XPATH, f"//button[contains(@class, 'select-search__option') and contains(., '{station_name}')]")
        self.wait.until(EC.element_to_be_clickable(locator)).click()



    def fill_second_step(self, date, period, color, comment):
        date_field = self.driver.find_element(*self.DATE_INPUT)
        date_field.clear()
        date_field.send_keys(date)

        date_field.send_keys(Keys.ENTER)
        
        self.select_rental_period(period)
        self.select_color(color)
        self.driver.find_element(*self.COMMENT_INPUT).send_keys(comment)

    def select_rental_period(self, period_text):
            self.driver.find_element(*self.RENTAL_DROPDOWN).click()

            locator = (By.XPATH, f"//div[contains(@class, 'Dropdown-option') and text()= '{period_text}']")
            self.wait.until(EC.element_to_be_clickable(locator)).click()

    def select_color(self, color_id):
        locator = (By.ID, color_id)
        self.driver.find_element(*locator).click()

    def click_finish_order_button(self):
        self.driver.find_element(*self.FINISH_ORDER_BUTTON).click()

        self.wait.until(EC.element_to_be_clickable(self.CONFIRM_YES_BUTTON)).click()


    def is_order_success(self):
        return self.wait.until(EC.visibility_of_element_located(self.SUCCESS_HEADER)).is_displayed()

    def get_order_number(self):
        return self.driver.find_element(*self.ORDER_NUMBER_TEXT).text

    def click_view_status(self):
        self.driver.find_element(*self.VIEW_STATUS_BUTTON).click()


        


    



