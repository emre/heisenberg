class Heist:

    def __init__(self, account, amount):
        self.account = account
        self.amount = amount

    def to_transaction(self):
        return {
                "from": self.account,
                "id": "dw-heist",
                "json": {"username": self.account, "amount": f"{self.amount}"},
                "required_auths": [],
                "required_posting_auths": [self.account],
        }

    @classmethod
    def from_transaction(cls, tx_data):
        pass