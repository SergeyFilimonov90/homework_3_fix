import time
import datetime
from datetime import date
import calendar

import pytest
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver import ActionChains,Keys
from selenium.webdriver.support.wait import WebDriverWait
from pages.login_page import Login_page
from pages.main_page import Main_page
from pages.cart_page import Cart_page
from pages.client_information_page import Clien_information_page
from pages.payment_page import Payment_page
from pages.finish_page import Finish_page


#might need: pip3 install pytest-ordering

#@@pytest.mark.run(order=1) #we specify in what order we want the tests to be executed
def buy_product_1(set_up,set_group):
     options = Options()
     options.add_experimental_option('excludeSwitches',['enable-logging'])#to clear the terminal from all gibberish messages
     driver = webdriver.Chrome(executable_path='C:\\Users\\Elgyn\\PycharmProjects\\resource\\chromedriver.exe',chrome_options = options)
     print('Start test 1')
     print('Приветствую Вас в нашем интернет магазине.')
     print(
          'Выберите один из товаров и введите его номер:\n1:Sauce Labs Backpack\n2:Sauce Labs Bike Light\n3:Sauce Labs Bolt T-Shirt\n4:Sauce Labs Fleece Jacket\n5:Sauce Labs Onesie\n6:Test.allTheThings() T-Shirt (Red)')
     valid_input = [1, 2, 3, 4, 5, 6]

     while True:
          try:
               userInput = int(input("Enter something: "))
          except ValueError:
               print("Not an integer!")
               continue
          if userInput not in valid_input:
               print('Need a valid input')
               continue
          elif userInput == 1:
               print('At last you got it!')
               print('Begin test')

               print('testing completed')
               break

     login = Login_page(driver)
     main_page_test = Main_page(driver)
     cart_page_test = Cart_page(driver)
     client_info_page = Clien_information_page(driver)
     pay = Payment_page(driver)
     finish_page = Finish_page(driver)

     login.authorization()
     main_page_test.select_product_1()
     cart_page_test.cart_test()
     client_info_page.client_page_test()
     pay.payment()
     finish_page.finish()
     print('Finish test 1')




#@pytest.mark.run(order=1)
def test_buy_product_2(set_up,set_group):
     options = Options()
     options.add_experimental_option('excludeSwitches', ['enable-logging'])
     driver = webdriver.Chrome(executable_path='C:\\Users\\Elgyn\\PycharmProjects\\resource\\chromedriver.exe', chrome_options=options)
     print('Start test 2')

     login = Login_page(driver)
     main_page_test = Main_page(driver)
     cart_page_test = Cart_page(driver)


     login.authorization()
     main_page_test.select_product_2()
     cart_page_test.cart_test()
     print('Finish test 2')

     #time.sleep(10)

#@pytest.mark.run(order=2)
def test_buy_product_3(set_up,set_group):
     options = Options()
     options.add_experimental_option('excludeSwitches', ['enable-logging'])
     driver = webdriver.Chrome(executable_path='C:\\Users\\Elgyn\\PycharmProjects\\resource\\chromedriver.exe', chrome_options = options)
     print('Start test 3')

     login = Login_page(driver)
     main_page_test = Main_page(driver)
     cart_page_test = Cart_page(driver)


     login.authorization()
     main_page_test.select_product_3()
     cart_page_test.cart_test()

     print('Finish test 3')

     time.sleep(10)




