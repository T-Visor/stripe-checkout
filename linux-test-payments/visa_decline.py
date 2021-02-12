from payment_information import PaymentInformation




class VisaDecline(PaymentInformation):
    """ 
        This class encapsulates the payment information necessary
        when filling out the payment details in the Stripe Checkout
        webpage. 

        The payment information should be used for testing Stripe Checkout only,
        and will result in a declined transaction.
    """




    def __init__(self, billing_name=None, email_address=None, zip_code=None):
        """ 
            Create a payment information instance for a declined
            VISA card transaction.

            If no arguments are sent to this constructor, default values will be
            used instead.

        Args:
            billing_name (string): first and last name of cardholder (Ex. Akira Kurusu)
            email_address (string): the cardholder's email address
            zip_code (string): 5 digits representing the zip code (Ex. 55555)
        """
        self.billing_name = billing_name or 'Akira Kurusu'
        self.email_address = email_address or 'akirakurusu@persona.com'
        self.zip_code = zip_code or '55555'
        self._card_number = '4000000000000002'
        self._card_expiration = '1250'
        self._card_cvc = '123'




    def __str__(self):
        """
        Returns:
            A string representation of payment information
        """
        return 'Billing Name: ' + self.billing_name + '\n'          \
               'Email Address: ' + self.email_address + '\n'        \
               'Zip Code: ' + self.zip_code + '\n'                  \
               'Card Number: ' + self._card_number + '\n'           \
               'Card Expiration: ' + self._card_expiration + '\n'   \
               'Card CVC: ' + self._card_cvc + '\n' 
