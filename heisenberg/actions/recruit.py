import json

class Unit:

    CUSTOM_JSON_ID = "dw-unit"

    def __init__(self, account, unit, amount):
        self.account = account
        self.amount = amount
        self.unit = unit

    def to_transaction(self):
        """Prepares a valid blockchain operation object from the instance."""
        return {
            "from": self.account,
            "id": "dw-unit",
            "json": {
                "username": self.account,
                "unit": self.unit,
                f"unit_amount": "{self.unit_amount}"
            },
            "required_auths": [],
            "required_posting_auths": [self.account],
        }

    @classmethod
    def from_op(cls, op_data):
        """A factory method to instantiate a Unit object from a blockchain
        operation data.

        :param op_data (dict): Operation data
        :return (Unit): Unit instance
        """
        if op_data.get("id") != Unit.CUSTOM_JSON_ID:
            raise ValueError("Invalid Custom JSON ID.")

        json_metadata = json.loads(op_data["json"])
        return cls(
            json_metadata.get("username"),
            json_metadata.get("unit"),
            json_metadata.get("amount")
        )

    def __str__(self):
        return f"<{self.CUSTOM_JSON_ID}: " \
               f"{self.account} {self.unit} {self.amount}>"