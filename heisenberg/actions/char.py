from . import BaseAction

class Char(BaseAction):
    """The class representing the "dw-char" action in the game."""

    CUSTOM_JSON_ID = "dw-char"
    PROPERTIES = ["username", "icon", "referer"]

    def __init__(self, account,  icon, referer):
        self.account = account
        self.icon = icon
        self.referer = referer

    def _generate_json(self):
        return {
            "username": self.account,
            "icon": f"{self.icon}",
            "referer": self.referer,
        }

    def __str__(self):
        return f"<{self.CUSTOM_JSON_ID}: " \
               f"{self.account} #{self.icon} {self.referer}>"
