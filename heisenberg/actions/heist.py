from . import BaseAction

class Heist(BaseAction):
    """The class representing the "dw-heist" action in the game."""

    CUSTOM_JSON_ID = "dw-heist"
    PROPERTIES = ['username', 'amount']

    def __init__(self, account, amount):
        self.account = account
        self.amount = amount

    def _generate_json(self):
        return {
            "username": self.account,
            "amount": f"{self.amount}"
        }

    def __str__(self):
        return f"<{self.CUSTOM_JSON_ID}: {self.account} {self.amount}>"