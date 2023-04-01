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
from pages.main_page import Main_page


class Cart_final_page(Main_page,Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators

    checkout_overview_paragraph = "//span[@class='title']"
    product_1_text = "//div[@class='inventory_item_name']"
    product_1_price = "//div[@class='inventory_item_price']"
    subtotal_price = "//div[@class='summary_subtotal_label']"
    finish_final_button = "//button[@id='finish']"

    #Constants

    PRODUCT_1_TEXT = 'Sauce Labs Backpack'
    PRODUCT_1_PRICE = '$29.99'
    PRODUCT_2_TEXT = 'Sauce Labs Bike Light'
    PRODUCT_2_PRICE = '$9.99'
    PRODUCT_3_TEXT = 'Sauce Labs Bolt T-Shirt'
    PRODUCT_3_PRICE = '$15.99'
    PRODUCT_4_TEXT = 'Sauce Labs Fleece Jacket'
    PRODUCT_4_PRICE = '$49.99'
    PRODUCT_5_TEXT = 'Sauce Labs Onesie'
    PRODUCT_5_PRICE = '$7.99'
    PRODUCT_6_TEXT = "Test.allTheThings() T-Shirt (Red)"
    PRODUCT_6_PRICE = "$15.99"

    product_name = ''

    product_price = ''

    product_subtotal_price = ''

    #Getters


    def get_checkout_overview_paragraph_text(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkout_overview_paragraph)))


    def get_product_text(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_1_text)))

    def get_product_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_1_price)))

    def get_subtotal_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.subtotal_price)))

    def get_finish_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.finish_final_button)))


    def get_products_name_cart(self):
        global product_name
        product1 = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_1_text)))
        product_name = product1.text
        print(f'Product name: {product_name}')
        return product_name


    def get_products_price_cart(self):
        global product_price
        product1 = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_1_price)))
        product_price = product1.text
        print(f'Price: {product_price}')
        return product_price

    def get_products_pricesubtotal_cart(self):
        global product_subtotal_price
        product1 = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.subtotal_price)))
        product_subtotal_price = product1.text[12:]
        print(f'Subtotal: {product_subtotal_price}')
        return product_subtotal_price

    #Actions

    def click_final_finish_button(self):
        self.get_finish_button().click()
        print('Click finish button')

    #Methods

    def cart_step_two_test_product_1(self):
        self.get_current_url()
        self.assert_url('https://www.saucedemo.com/checkout-step-two.html')
        self.check_name_or_price(self.get_checkout_overview_paragraph_text(), 'Checkout: Overview')
        self.get_products_name_cart()
        self.get_products_price_cart()
        self.get_products_pricesubtotal_cart()

        self.assert_text(Main_page.get_products_1_text_s(self), product_name)
        self.assert_text(Main_page.get_products_1_price_s(self), product_price)
        self.assert_text(Main_page.get_products_1_price_s(self),product_subtotal_price)
        #self.assert_final_cart_price_subtotal(Main_page.product_1_price_global, self.product_subtotal_price)
        self.click_final_finish_button()

    def cart_step_two_test_product_2(self):
        self.get_current_url()
        self.assert_url('https://www.saucedemo.com/checkout-step-two.html')
        self.check_name_or_price(self.get_checkout_overview_paragraph_text(), 'Checkout: Overview')

        self.get_products_name_cart()
        self.get_products_price_cart()
        self.get_products_pricesubtotal_cart()
        self.assert_text(Main_page.get_products_2_text_s(self), product_name)
        self.assert_text(Main_page.get_products_2_price_s(self), product_price)
        self.assert_text(Main_page.get_products_2_price_s(self), product_subtotal_price)
        self.click_final_finish_button()

    def cart_step_two_test_product_3(self):
        self.get_current_url()
        self.assert_url('https://www.saucedemo.com/checkout-step-two.html')
        self.check_name_or_price(self.get_checkout_overview_paragraph_text(), 'Checkout: Overview')
        self.get_products_name_cart()
        self.get_products_price_cart()
        self.get_products_pricesubtotal_cart()
        self.assert_text(Main_page.get_products_3_text_s(self), product_name)
        self.assert_text(Main_page.get_products_3_price_s(self), product_price)
        self.assert_text(Main_page.get_products_3_price_s(self), product_subtotal_price)
        self.click_final_finish_button()

    def cart_step_two_test_product_4(self):
        self.get_current_url()
        self.assert_url('https://www.saucedemo.com/checkout-step-two.html')
        self.check_name_or_price(self.get_checkout_overview_paragraph_text(), 'Checkout: Overview')
        self.get_products_name_cart()
        self.get_products_price_cart()
        self.get_products_pricesubtotal_cart()
        self.assert_text(Main_page.get_products_4_text_s(self), product_name)
        self.assert_text(Main_page.get_products_4_price_s(self), product_price)
        self.assert_text(Main_page.get_products_4_price_s(self), product_subtotal_price)
        self.click_final_finish_button()

    def cart_step_two_test_product_5(self):
        self.get_current_url()
        self.assert_url('https://www.saucedemo.com/checkout-step-two.html')
        self.check_name_or_price(self.get_checkout_overview_paragraph_text(), 'Checkout: Overview')
        self.get_products_name_cart()
        self.get_products_price_cart()
        self.get_products_pricesubtotal_cart()
        self.assert_text(Main_page.get_products_5_text_s(self), product_name)
        self.assert_text(Main_page.get_products_5_price_s(self), product_price)
        self.assert_text(Main_page.get_products_5_price_s(self), product_subtotal_price)
        self.click_final_finish_button()

    def cart_step_two_test_product_6(self):
        self.get_current_url()
        self.assert_url('https://www.saucedemo.com/checkout-step-two.html')
        self.check_name_or_price(self.get_checkout_overview_paragraph_text(), 'Checkout: Overview')
        self.get_products_name_cart()
        self.get_products_price_cart()
        self.get_products_pricesubtotal_cart()
        self.assert_text(Main_page.get_products_6_text_s(self), product_name)
        self.assert_text(Main_page.get_products_6_price_s(self), product_price)
        self.assert_text(Main_page.get_products_6_price_s(self), product_subtotal_price)
        self.click_final_finish_button()









