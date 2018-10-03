
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class login():

    def test(self):
        baseUrl = "https://www.facebook.com"
        driver = webdriver.Chrome(executable_path='/Users/QuintonMills/Desktop/SeleniumKitchen/chromedriver')
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(2)
        user = driver.find_element_by_xpath("//input[@id='email']")
        user.send_keys("johnnytest1041@yahoo.com")
        pass1 = driver.find_element_by_xpath("//input[@id='pass']")
        pass1.send_keys("SeleniumTest123")
        login = driver.find_element_by_xpath("//label[@id='loginbutton']")
        login.click()
        driver.implicitly_wait(3)
        post = driver.find_element_by_xpath("//i[@class='_5qto img sp_P0O-6um28H6_2x sx_94ad73']")
        post.click()
        driver.implicitly_wait(3)
        post1 = driver.find_element_by_xpath("//a[@class='_4-h7 _5qtn fbReactComposerAttachmentSelector_STATUS']")
        status = driver.find_element_by_xpath("   rel XPath //div[@class='_1mwp navigationFocus _395 _1mwq _4c_p _5bu_ _3t-3 _34nd _21mu _5yk1']")
        status.click()
        driver.implicitly_wait(3)
        status.send_keys("Aye we in here")

        driver.implicitly_wait(5)
ff = login()
ff.test()