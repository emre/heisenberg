from . import BaseAction

class Upgrade(BaseAction):
    """The class representing the "dw-upgrade" action in the game."""

    CUSTOM_JSON_ID = "dw-upgrade"
    PROPERTIES = ["username", "building"]

    def __init__(self, account,  building):
        self.account = account
        self.building = building

    def _generate_json(self):
        return {
            "username": self.account,
            "building": self.building
        }

    def __str__(self):
        return f"<{self.CUSTOM_JSON_ID}: " \
               f"{self.account} {self.building}>"
