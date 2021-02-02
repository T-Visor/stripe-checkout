#!/usr/bin/env python

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def main():
    
    # Use Firefox to open the locally hosted
    # node web application.
    driver = webdriver.Firefox()
    driver.get('localhost:4242')

    # Click the button on the landing page to initiate a stripe checkout
    # session.
    driver.find_element_by_id('button').click()
    time.sleep(5)

    # Enter all information in the checkout page.
    enter_information_into_field(driver, 'email', 'tkimbr1@students.towson.edu')
    enter_information_into_field(driver, 'cardNumber', '4242424242424242')
    enter_information_into_field(driver, 'cardExpiry', '1230')
    enter_information_into_field(driver, 'cardCvc', '123')
    enter_information_into_field(driver, 'billingName', 'Turhan Kimbrough')
    enter_information_into_field(driver, 'billingPostalCode', '12345')
    time.sleep(3)

    # Submit the information.
    driver.find_element_by_class_name('SubmitButton').click()
    time.sleep(15)

    # End the test session.
    driver.close()




def enter_information_into_field(web_driver, element_name, information):
    field = web_driver.find_element_by_name(element_name)
    field.clear()
    field.send_keys(information)




main()
