#!/usr/bin/env python

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def main():
    """
        Run a test procedure which simulates a successful
        Stripe Checkout session.
    """
    # Use Firefox to open the locally hosted
    # node web application.
    driver = webdriver.Firefox()
    driver.get('localhost:4242')

    # Click the button on the landing page to initiate a Stripe Checkout
    # session.
    driver.find_element_by_id('button').click()
    time.sleep(5)

    # Submit information.
    populate_form_using_web_driver(driver)
    driver.find_element_by_class_name('SubmitButton').click()
    time.sleep(15)

    # End the test session.
    driver.close()




def populate_form_using_web_driver(web_driver):
    """
        Enter values for all fields in the web form.

    Args:
        web_driver (web driver): the browser controller which will
                                 run the test procedure
    """
    enter_information_into_field(web_driver, 'email', 'tkimbr1@students.towson.edu')
    enter_information_into_field(web_driver, 'cardNumber', '4242424242424242')
    enter_information_into_field(web_driver, 'cardExpiry', '1230')
    enter_information_into_field(web_driver, 'cardCvc', '123')
    enter_information_into_field(web_driver, 'billingName', 'Turhan Kimbrough')
    enter_information_into_field(web_driver, 'billingPostalCode', '12345')
    time.sleep(3)




def enter_information_into_field(web_driver, element_name, information):
    """
        Auto-fill a specific field.

    Args:
        web_driver (web driver): the browser controller which will
                                 run the test procedure
        element_name (string): the string name of the webpage element
        information (string): the string to write into the field
    """
    field = web_driver.find_element_by_name(element_name)
    field.clear()
    field.send_keys(information)




main()
