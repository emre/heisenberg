from . import BaseAction

class Attack(BaseAction):
    """The class representing the "dw-attack" action in the game."""

    CUSTOM_JSON_ID = "dw-attack"
    PROPERTIES = ["username", "defender", "army"]

    def __init__(self, account, defender, army):
        self.account = account
        self.defender = defender
        self.army = army

    def _generate_json(self):
        return {
            "username": self.account,
            "defender": self.defender,
            "army": self.army
        }

    def __str__(self):
        return f"<{self.CUSTOM_JSON_ID}: " \
               f"{self.account} {self.defender} {self.army}>"
