#!/usr/bin/env python
import argparse
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from payment_information_factory import PaymentInformationFactory
from visa_success import VisaSuccess
from visa_decline import VisaDecline




def main():
    """
        Run a test procedure for Stripe Checkout.
    """
    # Get payment information and print details to the console
    payment_information = get_payment_information()
    print(payment_information)
        
    # Open the locally hosted Node web application.
    driver = webdriver.Firefox()
    driver.get('localhost:4242')

    # Click the button on the landing page to initiate a Stripe Checkout
    # session.
    driver.find_element_by_id('button').click()
    time.sleep(3)

    # Fill out the form and submit the information
    populate_payment_details_form(driver, payment_information)
    driver.find_element_by_class_name('SubmitButton').click()
    time.sleep(15)

    # End the test session.
    driver.close()




def get_payment_information():
    """
    Returns:
        An object containing payment details necessary for the 
        Stripe Checkout transaction.
    """
    argument = parse_commandline_argument()
    factory = PaymentInformationFactory()
    return factory.get_payment_information(argument.transaction[0])




def parse_commandline_argument():
    """ 
		Parse the arguments from the command-line.

        If no arguments are passed, the help screen will
        be shown and the program will be terminated.

    Returns:
        the parser with the command-line argument
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--transaction', nargs=1, required=True, 
                        help='Transaction type (Example: "success" or "decline")')
    
    # if no arguments were passed, show the help screen
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit()

    return parser.parse_args()




def populate_payment_details_form(web_driver, payment_information):
    """
        Enter values for all fields in the web form.

    Args:
        web_driver: the web driver running the automated test
        payment_information: the object containing the necessary  
                             information for filling out the web form
    """
    
    enter_information_into_field(web_driver, 'email',
                                 payment_information.email_address)

    enter_information_into_field(web_driver, 'cardNumber',
                                 payment_information._card_number)

    enter_information_into_field(web_driver, 'cardExpiry',
                                 payment_information._card_expiration)

    enter_information_into_field(web_driver, 'cardCvc',
                                 payment_information._card_cvc)

    enter_information_into_field(web_driver, 'billingName',
                                 payment_information.billing_name)

    enter_information_into_field(web_driver, 'billingPostalCode',
                                payment_information.zip_code)
    time.sleep(3)




def enter_information_into_field(web_driver, element_name, information):
    """
        Auto-fill a specific field.

    Args:
        web_driver: the web driver running the automated test
        element_name (string): the string name of the webpage element
        information (string): the string to write into the field
    """
    element = web_driver.find_element_by_name(element_name)
    element.clear()
    element.send_keys(information)




main()
