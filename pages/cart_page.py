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
from pages.locators import MainPageLocators
from pages.locators import FinishPageLocators






class Cart_page(Main_page,Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators


    product_text = "//div[@class='inventory_item_name']"
    product_price = "//div[@class='inventory_item_price']"


    add_to_cart_paragraph_text = "//span[@class='title']"
    checkout_button = "//button[@id='checkout']"

    #Constants

    PRODUCT_1_TEXT = 'Sauce Labs Backpack'
    PRODUCT_1_PRICE = '$29.99'

    product1_price_cart = ''
    product1_text_cart = ''

    #Getters

    def get_product_text(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_text)))

    def get_product_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_price)))


    def get_paragraph_text(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_to_cart_paragraph_text)))

    def get_checkout_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkout_button)))



    def get_products_price_1_cart(self):
        global product1_price_cart
        #product2 = self.driver.find_element(*FinishPageLocators.PRICE_2_CART)
        product1 = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_price)))
        product1_price_cart = product1.text
        print(f'cart page price: {product1_price_cart}')
        return product1_price_cart

    def get_products_text_1_cart(self):
        global product1_text_cart
        # product2 = self.driver.find_element(*FinishPageLocators.PRICE_2_CART)
        product1 = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_text)))
        product1_text_cart = product1.text
        print(f'cart page text: {product1_text_cart}')
        return product1_text_cart

    #Actions

    def click_checkout_button(self):
        self.get_checkout_button().click()
        print('Item added to cart')

    #Methods

    #def cart_test_product_1(self):
       # self.get_current_url()
       # self.assert_url('https://www.saucedemo.com/cart.html')
       # self.check_text(self.get_paragraph_text(), 'Your Cart')
       #print(f'text from the main page {self.get_products_5_text_s()}')

       #print(f'text from the main page {self.get_products_1_text_s()}')

       #print(self.get_products_1_price_s())
       #rint(f'price from the main page{Main_page.}')





    #print(f'text from the main page {self.get_products_2_text_s_cart(self.get_products_2_text_s())}')

    def cart_test_product_1(self):

        self.get_current_url()
        self.assert_url('https://www.saucedemo.com/cart.html')
        self.get_products_text_1_cart()
        self.get_products_price_1_cart()
        self.assert_text(Main_page.get_products_1_text_s(self), product1_text_cart)
        self.assert_text(Main_page.get_products_1_price_s(self), product1_price_cart)
        self.click_checkout_button()


    def cart_test_product_2(self):

        self.get_current_url()
        self.assert_url('https://www.saucedemo.com/cart.html')
        self.get_products_text_1_cart()
        self.get_products_price_1_cart()

        self.assert_text(Main_page.get_products_2_text_s(self), product1_text_cart)
        self.assert_text(Main_page.get_products_2_price_s(self), product1_price_cart)
        self.click_checkout_button()


    def cart_test_product_3(self):
        self.get_current_url()
        self.get_products_text_1_cart()
        self.get_products_price_1_cart()
        self.assert_url('https://www.saucedemo.com/cart.html')
        self.assert_text(Main_page.get_products_3_text_s(self), product1_text_cart)
        self.assert_text(Main_page.get_products_3_price_s(self), product1_price_cart)
        self.click_checkout_button()


    def cart_test_product_4(self):
        self.get_current_url()
        self.get_products_text_1_cart()
        self.get_products_price_1_cart()
        self.assert_url('https://www.saucedemo.com/cart.html')
        print(f'@@@@{Main_page.product_4_text_global}')
        self.assert_text(Main_page.get_products_4_text_s(self), product1_text_cart)
        self.assert_text(Main_page.get_products_4_price_s(self), product1_price_cart)
        self.click_checkout_button()

    def cart_test_product_5(self):
        self.get_current_url()
        self.get_products_text_1_cart()
        self.get_products_price_1_cart()
        self.assert_url('https://www.saucedemo.com/cart.html')
        self.assert_text(Main_page.get_products_5_text_s(self), product1_text_cart)
        self.assert_text(Main_page.get_products_5_price_s(self), product1_price_cart)
        self.click_checkout_button()

    def cart_test_product_6(self):
        self.get_current_url()
        self.get_products_text_1_cart()
        self.get_products_price_1_cart()
        self.assert_url('https://www.saucedemo.com/cart.html')
        self.assert_text(Main_page.get_products_6_text_s(self), product1_text_cart)
        self.assert_text(Main_page.get_products_6_price_s(self), product1_price_cart)
        self.click_checkout_button()






