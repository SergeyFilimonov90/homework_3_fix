import time
import datetime
from datetime import date
import calendar

import self
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver import ActionChains,Keys
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base
from pages.locators import MainPageLocators



class Main_page(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    driver = webdriver.Chrome(executable_path='C:\\Users\\Elgyn\\PycharmProjects\\resource\\chromedriver.exe')
    #Locators
    paragraph_text = "//span[@class='title']"
    product_1_text = "//div[text()='Sauce Labs Backpack']"
    product_1_price = "//div[text()='29.99']"
    product_2_text = "//div[text()='Sauce Labs Bike Light']"
    product_2_price = "//div[text()='9.99']"
        #"//*[@id='inventory_container']/div/div[2]/div[2]/div[2]/div"
    product_3_text = "//div[text()='Sauce Labs Bolt T-Shirt']"
    product_3_price = "//div[text()='15.99']"
    product_4_text = "//div[text()='Sauce Labs Fleece Jacket']"
    product_4_price = "//div[text()='49.99']"
    product_5_text = "//div[text()='Sauce Labs Onesie']"
    product_5_price = "//div[text()='7.99']"
    product_6_text = "//div[text()='Test.allTheThings() T-Shirt (Red)']"
    product_6_price = "//div[text()='15.99']"

    add_to_cart_button_product_1 = "//button[@id='add-to-cart-sauce-labs-backpack']"
    add_to_cart_button_product_2 = "//button[@id='add-to-cart-sauce-labs-bike-light']"
    add_to_cart_button_product_3 = "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']"
    add_to_cart_button_product_4 = "//button[@id='add-to-cart-sauce-labs-fleece-jacket']"
    add_to_cart_button_product_5 = "//button[@id='add-to-cart-sauce-labs-onesie']"
    add_to_cart_button_product_6 = "//button[@id='add-to-cart-test.allthethings()-t-shirt-(red)']"

    cart_icon_product = "//div[@id='shopping_cart_container']"
    burger_menu = "//button[@id='react-burger-menu-btn']"
    about_link = "//a[@id='about_sidebar_link']"

   # Constants (Just to know the names and prices)

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

    product_1_price_global = ''
    product_2_price_global = ''
    product_3_price_global = ''
    product_4_price_global = ''
    product_5_price_global = ''
    product_6_price_global = ''

    product_1_text_global = ''
    product_2_text_global = ''
    product_3_text_global = ''
    product_4_text_global = ''
    product_5_text_global = ''
    product_6_text_global = ''

    #Getter for paragraph text(Products)
    def get_products_paragraph_text(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.paragraph_text)))

    #Getters for goods names and prices(get text method))


    def get_products_1_price_s(self):
        global product_1_price_global
        product1 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.product_1_price)))

        product_1_price_global = product1.text
        print(product_1_price_global)
        return product_1_price_global


    def get_products_2_price_s(self):
        global product_2_price_global
        product2 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.product_2_price)))

        product_2_price_global = product2.text
        print(product_2_price_global)
        return product_2_price_global

    def get_products_3_price_s(self):
        global product_3_price_global
        product3 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.product_3_price)))

        product_3_price_global = product3.text
        print(product_3_price_global)
        return product_3_price_global

    def get_products_4_price_s(self):
        global product_4_price_global
        product4 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.product_4_price)))

        product_4_price_global = product4.text
        print(product_4_price_global)
        return product_4_price_global

    def get_products_5_price_s(self):
        global product_5_price_global
        product5 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.product_5_price)))

        product_5_price_global = product5.text
        print(product_5_price_global)
        return product_5_price_global

    def get_products_6_price_s(self):
        global product_6_price_global
        product6 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.product_6_price)))

        product_6_price_global = product6.text
        print(product_6_price_global)
        return product_6_price_global

    def get_products_1_text_s(self):
        global product_1_text_global
        product1 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.product_1_text)))

        product_1_text_global = product1.text
        print(product_1_text_global)
        return product_1_text_global

    def get_products_2_text_s(self):
        global product_2_text_global
        product2 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.product_2_text)))

        product_2_text_global = product2.text
        print(product_2_text_global)
        return product_2_text_global

    def get_products_3_text_s(self):
        global product_3_text_global
        product3 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.product_3_text)))

        product_3_text_global = product3.text
        print(product_3_text_global)
        return product_3_text_global

    def get_products_4_text_s(self):
        global product_4_text_global
        product4 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.product_4_text)))

        product_4_text_global = product4.text
        print(product_4_text_global)
        return product_4_text_global

    def get_products_5_text_s(self):
        global product_5_text_global
        product5 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.product_5_text)))
        # product2 = self.driver.find_element(*MainPageLocators.PRICE2)
        product_5_text_global = product5.text
        print(product_5_text_global)
        return product_5_text_global

    def get_products_6_text_s(self):
        global product_6_text_global
        product6 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.product_6_text)))
        # product2 = self.driver.find_element(*MainPageLocators.PRICE2)
        product_6_text_global = product6.text
        print(product_6_text_global)
        return product_6_text_global



   #Getters2

    def get_product_1_text_main_page(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_1_text)))

    def get_product_1_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_1_price)))

    def get_product_2_text(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_2_text)))

    def get_product_2_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_2_price)))

    def get_product_3_text(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_3_text)))

    def get_product_3_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_3_price)))

    def get_product_4_text(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_4_text)))

    def get_product_4_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_4_price)))

    def get_product_5_text(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_5_text)))

    def get_product_5_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_5_price)))

    def get_product_6_text(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_6_text)))

    def get_product_6_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_6_price)))


    def get_add_to_cart_product_1_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_to_cart_button_product_1)))

    def get_add_to_cart_product_2_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_to_cart_button_product_2)))

    def get_add_to_cart_product_3_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_to_cart_button_product_3)))

    def get_add_to_cart_product_4_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_to_cart_button_product_4)))

    def get_add_to_cart_product_5_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_to_cart_button_product_5)))

    def get_add_to_cart_product_6_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_to_cart_button_product_6)))

    def get_cart_icon(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart_icon_product)))

    def get_burger_menu(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.burger_menu)))

    def get_about_link(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.about_link)))


    #Actions


    def click_add_to_cart_button(self):
        self.get_add_to_cart_product_1_button().click()
        print('Item 1 added to cart')

    def click_add_to_cart_button_2(self):
        self.get_add_to_cart_product_2_button().click()
        print('Item 2 added to cart')

    def click_add_to_cart_button_3(self):
        self.get_add_to_cart_product_3_button().click()
        print('Item 3 added to cart')

    def click_add_to_cart_button_4(self):
        self.get_add_to_cart_product_4_button().click()
        print('Item 3 added to cart')

    def click_add_to_cart_button_5(self):
        self.get_add_to_cart_product_5_button().click()
        print('Item 3 added to cart')

    def click_add_to_cart_button_6(self):
        self.get_add_to_cart_product_6_button().click()
        print('Item 3 added to cart')


    def cart_icon_click(self):
        self.get_cart_icon().click()
        print('Click cart icon')

    def burger_menu_click(self):
        self.get_burger_menu().click()
        print('Click burger menu')

    def about_link_click(self):
        self.get_about_link().click()
        print('Click about link')


    #Methods

    def verify_page(self):
        self.get_current_url()
        self.assert_url('https://www.saucedemo.com/inventory.html')

        self.check_text(self.get_products_paragraph_text(),'Products')

    def select_product_1(self):
        self.get_products_1_text_s()
        self.get_products_1_price_s()
        self.click_add_to_cart_button()
        self.cart_icon_click()

    def select_product_2(self):
        self.get_products_2_text_s()
        self.get_products_2_price_s()
        self.click_add_to_cart_button_2()
        self.cart_icon_click()

    def select_product_3(self):
        self.get_products_3_text_s()
        self.get_products_3_price_s()
        self.click_add_to_cart_button_3()
        self.cart_icon_click()

    def select_product_4(self):
        self.get_products_4_text_s()
        self.get_products_4_price_s()

        self.click_add_to_cart_button_4()
        self.cart_icon_click()

    def select_product_5(self):
        self.get_products_5_text_s()
        self.get_products_5_price_s()

        self.click_add_to_cart_button_5()
        self.cart_icon_click()

    def select_product_6(self):
        self.get_products_6_text_s()
        self.get_products_6_price_s()

        self.click_add_to_cart_button_6()
        self.cart_icon_click()

    def go_to_about_link(self):
        self.get_current_url()
        self.burger_menu_click()
        self.about_link_click()
        self.assert_url('https://saucelabs.com/')
        self.get_current_url()






