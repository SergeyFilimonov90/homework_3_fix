from selenium.webdriver.common.by import By

class MainPageLocators:
    PRICE2 = (By.XPATH,'//*[@id="inventory_container"]/div/div[2]/div[2]/div[2]/div')

class FinishPageLocators:
    PRICE_2_CART = (By.XPATH, "//*[@id='cart_contents_container']/div/div[1]/div[3]/div[2]/div[2]/div")