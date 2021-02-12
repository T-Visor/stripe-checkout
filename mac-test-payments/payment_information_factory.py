from visa_success import VisaSuccess
from visa_decline import VisaDecline




class PaymentInformationFactory:
    """
        This class generates encapsulated payment information
        objects to be used for the Stripe Checkout webpage.
    """




    def get_payment_information(self, transaction_type):
        """
            Args:
                transaction_type (string): the type of payment information
                                           object desired
            Returns:
                the appropriate payment information object
        """
        if transaction_type == 'success':
            return VisaSuccess()
        elif transaction_type == 'decline':
            return VisaDecline()
    
