#!/usr/local/bin/python3
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys




def main():
    """
        Run a test procedure which simulates a successful
        Stripe Checkout session.
    """
    # Opens the locally hosted Node web application.
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('http://127.0.0.1:4242')

    # Clicks the button on the landing page to initiate a Stripe Checkout
    # session.
    driver.find_element_by_id('button').click()
    time.sleep(8)

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
    email_address = 'tkimbr1@students.towson.edu'
    card_number = '4242424242424242'                # card number used to test VISA transactions
    card_expiration = '1250'                        # December 2050 expiration date
    card_cvc = '123'
    billing_name = 'Turhan Kimbrough'
    zip_code = '12345'

    enter_information_into_field(web_driver, 'email', email_address)
    enter_information_into_field(web_driver, 'cardNumber', card_number)
    enter_information_into_field(web_driver, 'cardExpiry', card_expiration)
    enter_information_into_field(web_driver, 'cardCvc', card_cvc)
    enter_information_into_field(web_driver, 'billingName', billing_name)
    enter_information_into_field(web_driver, 'billingPostalCode', zip_code)
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
