from steem import Steem
from steem.transactionbuilder import TransactionBuilder
from steembase import operations

from .actions.heist import Heist
from .actions.unit import Unit
from .actions.char import Char
from .actions.upgrade import Upgrade
from .actions.attack import Attack
from .datastructures import Transaction


class Heisenberg:
    """
    The core class to interact with the Drugwars game.
    All in-game actions can be created with a Heisenberg instance.

    Example:

        This invests 420 ingame DRUGs to the daily heist.

        ```
        from heisenberg.core import Heisenberg

        h = Heisenberg(
            'username',
            'posting_key'
        )
        h.heist(420)
    """

    def __init__(self, account, private_posting_key, steem_nodes=None):
        self.account = account
        self.private_posting_key = private_posting_key
        self.steem = Steem(
            nodes=steem_nodes or ["https://api.steemit.com"],
            keys=[private_posting_key])

    def heist(self, amount):
        """Create an "invest to heist" action and broadcast it
        to the STEEM network.

        :param amount (str): The amount of drugs to invest
        :return (Transaction): Transaction data
        """
        heist = Heist(self.account, amount)
        return self.broadcast(heist)

    def unit(self, unit, unit_amount):
        """Create an "unit" action and broadcast it
        to the STEEM network. (Recruiting)

        :param unit (str): The unit to recruit
        :param amount (str): The amount of units to recruit
        :return (Transaction): Transaction data
        """
        unit = Unit(self.account, unit, unit_amount)
        return self.broadcast(unit)

    def char(self, icon, referer=None):
        """Create a char in the game. This is required to play the game.

        :param icon: ID of the char
        :param referer: referer username (if available)
        :return (Transaction): Transaction data
        """
        char = Char(self.account, icon, referer or "")
        return self.broadcast(char)

    def upgrade(self, building):
        """Upgrade a building in the game with in-game resources.

        :param building (str): Building name
        :return (Transaction): Transaction data
        """
        upgrade = Upgrade(self.account, building)
        return self.broadcast(upgrade)

    def attack(self, defender, army):
        """Attack to an enemy in the game with your unit build.

        :param defender (str): The player you want to attack
        :param army (list): A list of units with amounts you want to use
        :return (Transaction): Transaction data
        """
        attack = Attack(self.account, defender, army)
        return self.broadcast(attack)

    def broadcast(self, action):
        """ Broadcasts the action to the STEEM network.

        It uses `broadcast_transaction_synchronous` method of steemd which
        actually gives transaction details. (ID, block_num.)

        :param action (Action): Action object
        :return (Transaction): Transaction data
        """
        ops = [
            operations.CustomJson(**action.to_transaction()),
        ]
        tb = TransactionBuilder(steemd_instance=self.steem)
        tb.appendOps(ops)
        tb.appendSigner(self.account, "posting")
        tb.sign()
        response = self.steem.broadcast_transaction_synchronous(tb.json())
        return Transaction(response.get("id"), response.get("block_num"))
