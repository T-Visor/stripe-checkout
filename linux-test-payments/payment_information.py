from abc import ABC # ABC ==> Abstract Base Class




class PaymentInformation(ABC):
    """ 
        This abstract class represents an encapsulated collection
        of payment information for a Stripe Checkout instance.

        Payment information typically consists of a name, email, zip code,
        and card/bank specific information.

        As part of the factory method design pattern, subclasses will define
        object creation.
    """
    pass
