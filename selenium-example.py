#!/usr/bin/env python

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get('localhost:4242')

# click the button to proceed with a new stripe checkout session
driver.find_element_by_id('button').click()

# default to waiting 5 seconds... need to change this later
time.sleep(5)

# Enter information for email
email_field = driver.find_element_by_name('email')
email_field.clear()
email_field.send_keys('tkimbr1@students.towson.edu')

# Enter information for card number
card_number_field = driver.find_element_by_name('cardNumber')
card_number_field.clear()
card_number_field.send_keys('4242424242424242')

# Enter information for card expiration
card_expiration_field = driver.find_element_by_name('cardExpiry')
card_expiration_field.clear()
card_expiration_field.send_keys('1230')

# Enter information for card CVC
card_cvc_field = driver.find_element_by_name('cardCvc')
card_cvc_field.clear()
card_cvc_field.send_keys('123')

# Enter information for name on card
cardholder_name_field = driver.find_element_by_name('billingName')
cardholder_name_field.clear()
cardholder_name_field.send_keys('Turhan Kimbrough')

# Enter information for zip code 
zip_code_field = driver.find_element_by_name('billingPostalCode')
zip_code_field.clear()
zip_code_field.send_keys('12345')

time.sleep(3)

driver.find_element_by_class_name('SubmitButton').click()

# wait for 5 seconds again...
time.sleep(15)

# end the test session
driver.close()
