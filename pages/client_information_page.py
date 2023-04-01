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



class Clien_information_page(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators

    first_name = "//input[@id='first-name']"
    last_name = "//input[@id='last-name']"
    postal_code = "//input[@id='postal-code']"
    continue_button = "//input[@id='continue']"
    checkout_text = "//span[@class='title']"


    #Getters

    def get_first_name_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.first_name)))

    def get_last_name_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.last_name)))

    def get_posta_code_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.postal_code)))

    def get_continue_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.continue_button)))

    def get_client_text(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkout_text)))


    #Actions

    def input_first_name(self,first_name):
        self.get_first_name_field().send_keys(first_name)
        print('Input first_name')

    def input_last_name(self,last_name):
        self.get_last_name_field().send_keys(last_name)
        print('Input last_name')

    def input_postal_code(self,postal_code):
        self.get_posta_code_field().send_keys(postal_code)
        print('Input postal code')

    def click_continue(self):
        self.get_continue_button().click()
        print('clicking continue button')

    #Methods

    def client_page_test(self):
        self.check_text(self.get_client_text(),'Checkout: Your Information')
        self.input_first_name('Frank')
        self.input_last_name('Elgyn')
        self.input_postal_code('14546256')
        self.click_continue()





