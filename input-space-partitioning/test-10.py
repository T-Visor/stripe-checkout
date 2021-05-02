#!/usr/bin/env python3
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select




# payment details
EMAIL = 'akira@persona.com'
CARD_NUMBER = '4242424242424242'
CARD_EXPIRY_DATE = '1230'
CARD_VERIFICATION_CODE = '223'
CARDHOLDER_NAME = 'Akira'
COUNTRY = 'United States'
ZIP_CODE = '21252'

SCREENSHOT_FILE_NAME = 'results/test-10-result.png'




def main():
    """
        Run the test procedure.
    """
    # Open locally hosted webpage.
    driver = webdriver.Firefox()
    driver.get('localhost:4242')

    # Proceed to checkout page.
    driver.find_element_by_id('button').click()
    driver.implicitly_wait(10) # seconds

    # Populate the web form.
    populate_payment_details_form(driver)

    # Submit the information. 
    driver.find_element_by_class_name('SubmitButton').click()

    # Take a screenshot.
    time.sleep(10)
    driver.save_screenshot(SCREENSHOT_FILE_NAME)

    # Close the session.
    driver.close()




def populate_payment_details_form(driver):
    """
        Enter values for all fields in the web form.

    Args:
        driver: the web driver running the automated test
    """
    enter_information_into_field(driver, 'email', EMAIL)
    enter_information_into_field(driver, 'cardNumber', CARD_NUMBER)
    enter_information_into_field(driver, 'cardExpiry', CARD_EXPIRY_DATE)
    enter_information_into_field(driver, 'cardCvc', CARD_VERIFICATION_CODE)
    enter_information_into_field(driver, 'billingName', CARDHOLDER_NAME)
    enter_information_into_field(driver, 'billingPostalCode', ZIP_CODE)

    drop_down_menu = Select(driver.find_element_by_id('billingCountry'))
    drop_down_menu.select_by_visible_text(COUNTRY)

    driver.implicitly_wait(5) # seconds




def enter_information_into_field(driver, element_name, information):
    """
        Auto-fill a specific field.

    Args:
        driver: the web driver running the automated test
        element_name (string): the string name of the webpage element
        information (string): the string to write into the field
    """
    element = driver.find_element_by_name(element_name)
    element.clear()
    element.send_keys(information)




main()
