import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage


class OrderPage(BasePage):
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
  


    @allure.step("Заполнить первую форму заказа (Имя: {name}, Фамилия: {surname}, Адрес: {address}, Телефон: {phone})")
    def fill_first_step(self, name, surname, address, metro, phone):
        self.send_keys(self.NAME_INPUT, name)
        self.send_keys(self.SURNAME_INPUT, surname)
        self.send_keys(self.ADDRESS_INPUT, address)
        self.select_metro(metro)
        self.send_keys(self.PHONE_INPUT, phone)
        self.click(self.NEXT_BUTTON)

    @allure.step("Выбрать станцию метро: {station_name}")
    def select_metro(self, station_name):
        metro_input = self.find_element(self.METRO_INPUT)
        metro_input.send_keys(station_name)
        
        locator = (By.XPATH, f"//button[contains(@class, 'select-search__option') and contains(., '{station_name}')]")
        self.click(locator)

    @allure.step("Заполнить вторую форму заказа (Дата: {date}, Период: {period})")
    def fill_second_step(self, date, period, color, comment):
        date_field = self.find_element(self.DATE_INPUT)
        date_field.clear()
        date_field.send_keys(date)
        date_field.send_keys(Keys.ENTER)
        
        self.select_rental_period(period)
        self.select_color(color)
        self.send_keys(self.COMMENT_INPUT, comment)

    @allure.step("Выбрать срок аренды: {period_text}")
    def select_rental_period(self, period_text):
        self.click(self.RENTAL_DROPDOWN)
        
        locator = (By.XPATH, f"//div[contains(@class, 'Dropdown-option') and text()='{period_text}']")
        self.click(locator)

    @allure.step("Выбрать цвет самоката (ID: {color_id})")
    def select_color(self, color_id):
        locator = (By.ID, color_id)
        self.click(locator)

    @allure.step("Нажать 'Заказать' и подтвердить заказ")
    def click_finish_order_button(self):
        self.click(self.FINISH_ORDER_BUTTON)
        self.click(self.CONFIRM_YES_BUTTON)

    @allure.step("Проверить, что заказ успешно оформлен")
    def is_order_success(self):
        return self.is_element_visible(self.SUCCESS_HEADER)
