import time
import datetime
from datetime import date
import calendar
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver import ActionChains,Keys
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base



class Login_page(Base):

    url = 'https://www.saucedemo.com'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators

    user_name = "//input[@ID='user-name']"
    password_field = "//input[@ID='password']"
    login_button = "//input[@value='Login']"
    paragraph_word = "//span[@class='title']"


    #Getters

    def get_user_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_name)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password_field)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))

    def get_paragraph_word_text(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.paragraph_word)))


    #Actions

    def input_user_name(self,user_name):
        self.get_user_name().send_keys(user_name)
        print('Input user_name')

    def input_password(self,password):
        self.get_password().send_keys(password)
        print('Input password')

    def click_login_button(self):
        self.get_login_button().click()
        print('clicking button')

    #Methods

    def authorization(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.input_user_name('standard_user')
        self.input_password('secret_sauce')
        self.click_login_button()
        self.check_text(self.get_paragraph_word_text(),'Products')





