from abc import ABC, abstractmethod

# OCP(Open Closed Principle) - A class should be open for extension and closed for modification.
# Meaning you should be able to add a new functionality without changing the existing code


"""

Code violating OCP

"""


class Notifier:
    def notify(self, method, message):
        if method == "SMS":
            print("Sent SMS", message)
        elif method == "EMAIL":
            print("Sent Email", message)


# adding a new method to send message

class Notifier:
    def notify(self, method, message):
        if method == "SMS":
            print("Sent SMS", message)
        elif method == "EMAIL":
            print("Sent Email", message)
        elif method == "SLACK":
            print("Sent Slack Message", message)


"""

SRP Compliant code

"""


class Notifier(ABC):

    @abstractmethod
    def notify(self, message):
        pass


class SMSNotifier(Notifier):
    def notify(self, message):
        print("Sent SMS", message)


class EmailNotifier(Notifier):
    def notify(self, message):
        print("Sent Email", message)


class SlackNotifier(Notifier):
    def notify(self, message):
        print("Sent Slack Message", message)
