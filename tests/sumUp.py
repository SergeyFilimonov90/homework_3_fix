import time
import datetime
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver import ActionChains,Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
driver = webdriver.Chrome(executable_path='C:\\Users\\Elgyn\\PycharmProjects\\SeleniumPython\\chromedriver.exe')

now_date = datetime.datetime.utcnow().strftime('%Y.%m..%d.%H.%M.%S') #initialising the daytime var
name_screenshot = 'screenshot' + str(now_date) + '.png' #setting the proper file name and format

                #Saving to the screenshot to a specified folder
driver.save_screenshot('C:\\Users\\Elgyn\\PycharmProjects\\SeleniumPython\\screenshots\\' + name_screenshot)

                   #Quicky about asserts
error_warning = button = driver.find_element(by=By.XPATH, value="//h3[@data-test='error']")
error_warting_text = error_warning.text
assert error_warting_text == 'Epic sadface: Username and password do not match any user in this service'


                 #how to use keyboard keys
product_sort_container = driver.find_element(by=By.XPATH, value="//select[@class='product_sort_container']")
product_sort_container.send_keys(Keys.ARROW_DOWN)

                  #how to make sure you are on the right page
url = 'https://www.saucedemo.com/inventory.html'
right_url = driver.current_url

assert url == right_url,'Wrong URL!'

                          #how to refresh a page
driver.refresh()


                        #page scroll

driver.execute_script('window.scrollTo(0, 200)')

                        #move on element

action = ActionChains(driver) #we show that we want seleinum to control our driver
#red_tshirt = driver.find_element(by=By.XPATH, value="//button[@id ='add-to-cart-test.allthethings()-t-shirt-(red)']")
icon = driver.find_element(by=By.XPATH, value="//a[@rel='noreferrer']")


#action.move_to_element(red_tshirt).perform()   #navigate on element

action.move_to_element(icon).perform()


now_date = datetime.datetime.utcnow().strftime('%Y.%m..%d.%H.%M.%S')  #setting up data format and save screenshot
name_screenshot = 'screenshot' + str(now_date) + '.png'
driver.save_screenshot('C:\\Users\\Elgyn\\PycharmProjects\\SeleniumPython\\screenshots\\' + name_screenshot)

                       #clear a text area

username = driver.find_element(by=By.XPATH, value="//input[@ID=\"user-name\"]")

username.clear()

                      #move back and forth in browser history
driver.back()

driver.forward()

                     #right and double clicks

action = ActionChains(driver)
double_click_button = driver.find_element(by=By.XPATH, value="//button[@id = 'doubleClickBtn']")
action.double_click(double_click_button).perform()


right_click_button = driver.find_element(by=By.XPATH, value="//button[@id = 'rightClickBtn']")
action.context_click(right_click_button).perform() #right click

                       #alternative way to find an element
'''''//button[text()='Click Me']'''''#this is how we find an element with a dynamic ID

'''//div[contains(@class,'react-datepicker__day--today')]'''#finds an element depending on it's tag contains(class,id,etc)
# we can use a part of a complex tag's name


                      # how to generate today's date in put it in a locator

now_date = datetime.datetime.utcnow().strftime('%d')
day_of_week = datetime.datetime.utcnow().strftime('%A')
month = datetime.datetime.utcnow().strftime('%B')
year = datetime.datetime.utcnow().strftime('%Y')

locator = "//div[@aria-label = 'Choose " + str(day_of_week) + ", " + str(month) + " "+ str(now_date) + "th," + " " + str(year) + "'"+"]"


                      #slider interraction
                      
action = ActionChains(driver)

slider_1 = driver.find_element(by=By.XPATH,value = "//input[@class = 'slider-square']")

action.click_and_hold(slider_1).move_by_offset(100, 0).release().perform()

action.click_and_hold(slider_1).move_by_offset(-100, 0).release().perform()#neagative value moves the slider backwards


                    #driver implicit and explicit wait

driver.implicitly_wait(10) #Need only to write it oce in the beginning of the test and and it will wait for all elements to appear.
from selenium.webdriver.support import expected_conditions as EC #we can curtail the import to save space


                              #here you can wait for a specific element to act in a specific way
visible_button = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='enableAfter']")))
#WebDriverWait(driver, timeout=3).until(some_condition)










