from abc import ABC, abstractmethod


# basic level inheritance
class PaymentMethod(ABC):
    @property
    @abstractmethod
    def method(self):
        pass

    def pay(self, amount):
        print(f"Paid ₹{amount} using {self.method}.")


class UPI(PaymentMethod):
    @property
    def method(self):
        return "UPI"


class Cash(PaymentMethod):
    @property
    def method(self):
        return "Cash"


class CreditCard(PaymentMethod):
    @property
    def method(self):
        return "CreditCard"
