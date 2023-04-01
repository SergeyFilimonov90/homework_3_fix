from lib2to3.pgen2 import driver
from telnetlib import EC
import datetime

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Base():

    def __init__(self,driver):

        self.driver = driver

    '''Method get current url'''

    def get_current_url(self):
        get_url = self.driver.current_url
        print('Current url ' + get_url)

    '''Method check paragraph text'''

    def check_text(self, word, value):
        value_word = word.text
        try:
            assert value_word == value
            print('Word value test passed')
        except AssertionError:
            print(f'Error! Value:  {value_word} didn\'t match the value:{value}')

    def assert_text(self, word, result):
        try:
            assert word == result
            print('Word value pass')
        except AssertionError:
            print(F'Word value fail word: {word} result: {result}')
        print(f'passed word:{word}, result: {result}')

    def check_name_or_price(self, word, value):
        value_word = word.text
        assert value_word == value
        print(f'Word value {value} test passed')

    '''Method make screenshot'''

    def screenshot(self):
        now_date = datetime.datetime.utcnow().strftime('%Y.%m..%d.%H.%M.%S')
        name_screenshot = 'screenshot' + str(now_date) + '.png'  # setting the proper file name and format
        self.driver.save_screenshot('C:\\Users\\Elgyn\\PycharmProjects\\main_project\\screen\\' + name_screenshot)

    def assert_url(self,result):
        current_url =  self.driver.current_url
        assert current_url == result, 'Wrong url!'
        print('Url test passed')

    def assert_final_cart_price(self,price):
        price = price.text[1:]  # using slice to get rid of $ simbol
        print('$ sliced off',price)

        price_total = self.driver.find_element(by=By.XPATH, value="//*[@id='checkout_summary_container']/div/div[2]/div[6]")
        test_price_total = price_total.text
        print('Checking out total price')
        print(price_total.text)
        assert price_total.text == 'Item total: ' + '$' + str(price), 'Wrong total price'


    def assert_final_cart_price_subtotal(self,price,subtotal):

        subtotal = subtotal[12:]
        print('Pass')
        print(f'Subtotal:{subtotal}')

        assert price == subtotal



