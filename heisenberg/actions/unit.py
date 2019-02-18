from . import BaseAction

class Unit(BaseAction):
    """The class representing the "dw-unit" action in the game."""

    CUSTOM_JSON_ID = "dw-unit"
    PROPERTIES = ["username", "unit", "unit_amount"]

    def __init__(self, account, unit, amount):
        self.account = account
        self.unit = unit
        self.amount = amount

    def _generate_json(self):
        return {
            "username": self.account,
            "unit": self.unit,
            "unit_amount": f"{self.amount}",
        }

    def __str__(self):
        return f"<{self.CUSTOM_JSON_ID}: " \
               f"{self.account} {self.unit} {self.amount}>"
