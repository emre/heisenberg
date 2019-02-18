import json

class Heist:
    """The class representing the "dw-heist" action in the game.

    Example:

        This will instantiate a Heist instance from the blockchain data.
        (op level)
        ```
        op_data = {
            'required_auths': [],
            'required_posting_auths': ['emrebeyler'],
            'id': 'dw-heist',
            'json': '{"username": "emrebeyler","amount": "260"}'
        }

        print(Heist.from_op(op_data))
        ```
    """

    CUSTOM_JSON_ID = "dw-heist"

    def __init__(self, account, amount):
        self.account = account
        self.amount = amount

    def to_transaction(self):
        """Prepares a valid blockchain operation object from the instance."""
        return {
                "from": self.account,
                "id": self.CUSTOM_JSON_ID,
                "json": {"username": self.account, "amount": f"{self.amount}"},
                "required_auths": [],
                "required_posting_auths": [self.account],
        }

    @classmethod
    def from_op(cls, op_data):
        """A factory method to instantiate a Heist object from a blockchain
        operation data.

        :param op_data (dict): Operation data
        :return (Heist): Heist instance
        """
        if op_data.get("id") != Heist.CUSTOM_JSON_ID:
            raise ValueError("Invalid Custom JSON ID.")

        json_metadata = json.loads(op_data["json"])
        return cls(
            json_metadata.get("username"), json_metadata.get("amount"))

    def __str__(self):
        return f"<{self.CUSTOM_JSON_ID}: {self.account} {self.amount}>"