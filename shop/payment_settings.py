

class PaymentSystem:
    """ Abstract Class """

    def pay(self, total_price, currency):
        raise NotImplementedError('Exception raised, PaymentSystem is supposed to be an Abstract class!')


class PayPal(PaymentSystem):
    
    def pay(self, total_price, currency):
        return "You successfuly paied {total_price} {currency} with PayPal ".format(
            total_price=total_price,
            currency=currency
        )


class Privat24(PaymentSystem):
    
    def pay(self, total_price, currency):
        return "You successfuly paied {total_price} {currency} with Privat24 ".format(
            total_price=total_price,
            currency=currency
        )


class Liqpay(PaymentSystem):
    
    def pay(self, total_price, currency):
        return "You successfuly paied {total_price} {currency} with Liqpay ".format(
            total_price=total_price,
            currency=currency
        )
