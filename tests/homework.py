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
from pages.cart_step_two_page import Cart_final_page


#might need: pip3 install pytest-ordering

#@@pytest.mark.run(order=1) #we specify in what order we want the tests to be executed
def buy_product_1():
     options = Options()
     options.add_experimental_option('excludeSwitches',['enable-logging'])#to clear the terminal from all gibberish messages
     driver = webdriver.Chrome(executable_path='C:\\Users\\Elgyn\\PycharmProjects\\resource\\chromedriver.exe',chrome_options = options)
     login = Login_page(driver)
     main_page_test = Main_page(driver)
     cart_page_test = Cart_page(driver)
     client_info_page = Clien_information_page(driver)
     cart_step_two = Cart_final_page(driver)
     finish_page = Finish_page(driver)
     print('Start test 1')
     print('Приветствую Вас в нашем интернет магазине.')
     print(
          'Выберите один из товаров и введите его номер:\n1:Sauce Labs Backpack\n2:Sauce Labs Bike Light\n3:Sauce Labs Bolt T-Shirt\n4:Sauce Labs Fleece Jacket\n5:Sauce Labs Onesie\n6:Test.allTheThings() T-Shirt (Red)')
     valid_input = [1, 2, 3, 4, 5, 6]

     while True:
          try:
               userInput = int(input("Введите ваш товар(1-6): "))
          except ValueError:
               error_message = 'Вы должны ввести чило от 1 до 6'
               error_message += '\nПопробуйте еще раз'
               print(error_message)
               continue

          if userInput not in valid_input:
               print(f'Пожалуйста выберите товар от 1 до 6. Вы выбрали {userInput}.')
               continue

          elif userInput == 1:
               print('Товар 1 выбран!')
               print('Begin test')
               login.authorization()
               main_page_test.verify_page()
               main_page_test.select_product_1()
               cart_page_test.cart_test_product_1()
               client_info_page.client_page_test()
               cart_step_two.cart_step_two_test_product_1()
               finish_page.finish()
               print('testing completed')
               break

          elif userInput == 2:
               print('Товар 2 выбран!')
               print('Begin test')
               login.authorization()
               main_page_test.verify_page()
               main_page_test.select_product_2()
               cart_page_test.cart_test_product_2()
               client_info_page.client_page_test()
               cart_step_two.cart_step_two_test_product_2()
               finish_page.finish()

               break

          elif userInput == 3:
               print('Товар 3 выбран!')
               print('Begin test')
               login.authorization()
               main_page_test.verify_page()
               main_page_test.select_product_3()
               cart_page_test.cart_test_product_3()
               client_info_page.client_page_test()
               cart_step_two.cart_step_two_test_product_3()
               finish_page.finish()


               print('testing completed')
               break

          elif userInput == 4:

               print('Товар 4 выбран!')
               print('Begin test')
               login.authorization()
               main_page_test.verify_page()
               main_page_test.select_product_4()
               cart_page_test.cart_test_product_4()
               client_info_page.client_page_test()
               cart_step_two.cart_step_two_test_product_4()
               finish_page.finish()


               print('testing completed')
               break

          elif userInput == 5:

               print('Товар 5 выбран!')
               print('Begin test')
               login.authorization()
               main_page_test.verify_page()
               main_page_test.select_product_5()
               cart_page_test.cart_test_product_5()
               client_info_page.client_page_test()
               cart_step_two.cart_step_two_test_product_5()
               finish_page.finish()


               print('testing completed')
               break

          elif userInput == 6:

               print('Товар 6 выбран!')
               print('Begin test')
               login.authorization()
               main_page_test.verify_page()
               main_page_test.select_product_6()
               cart_page_test.cart_test_product_6()
               client_info_page.client_page_test()
               cart_step_two.cart_step_two_test_product_6()
               finish_page.finish()


               print('testing completed')
               break


     # login = Login_page(driver)
     # main_page_test = Main_page(driver)
     # cart_page_test = Cart_page(driver)
     # client_info_page = Clien_information_page(driver)
     # pay = Payment_page(driver)
     # finish_page = Finish_page(driver)
     #
     # login.authorization()
     # main_page_test.select_product_1()
     # cart_page_test.cart_test()
     # client_info_page.client_page_test()
     # pay.payment()
     # finish_page.finish()
     # print('Finish test 1')

buy_product_1()