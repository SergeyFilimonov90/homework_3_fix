import time
import datetime
from datetime import date
import calendar
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




def test_about_link(set_up):
     options = Options()
     options.add_experimental_option('excludeSwitches',['enable-logging'])
     driver = webdriver.Chrome(executable_path='C:\\Users\\Elgyn\\PycharmProjects\\resource\\chromedriver.exe',chrome_options=options)
     login = Login_page(driver)
     main_page_test = Main_page(driver)


     login.authorization()
     main_page_test.go_to_about_link()


     time.sleep(10)


