import unittest

from heisenberg.actions.heist import Heist
from heisenberg.actions.unit import Unit
from heisenberg.actions.char import Char
from heisenberg.actions.upgrade import Upgrade
from heisenberg.actions.attack import Attack


class ActionTests(unittest.TestCase):

    def test_heist(self):
        heist = Heist('emrebeyler', 42)
        tx_data = heist.to_transaction()
        self.assertEqual(heist.amount, 42)
        self.assertEqual(tx_data["json"]["amount"], '42')
        self.assertEqual(tx_data["json"]["username"], 'emrebeyler')

    def test_unit(self):
        unit = Unit('emrebeyler', 'bouncer', 10)
        tx_data = unit.to_transaction()
        self.assertEqual(tx_data["json"]["username"], 'emrebeyler')
        self.assertEqual(tx_data["json"]["unit"], 'bouncer')
        self.assertEqual(tx_data["json"]["unit_amount"], '10')

    def test_char(self):
        unit = Char('emrebeyler', 1, 'ngc')
        tx_data = unit.to_transaction()
        self.assertEqual(tx_data["json"]["username"], 'emrebeyler')
        self.assertEqual(tx_data["json"]["icon"], '1')
        self.assertEqual(tx_data["json"]["referer"], 'ngc')

    def test_upgrade(self):
        upgrade = Upgrade('emrebeyler', 'headquarters')
        tx_data = upgrade.to_transaction()
        self.assertEqual(tx_data["json"]["username"], 'emrebeyler')
        self.assertEqual(tx_data["json"]["building"], 'headquarters')

    def test_attack(self):
        attack = Attack(
            'emrebeyler',
            'ngc',
            [{'unit': 'knifer', 'amount': 3}, {'unit': 'bouncer', 'amount': 2}]
        )
        tx_data = attack.to_transaction()
        self.assertEqual(tx_data["json"]["username"], 'emrebeyler')
        self.assertEqual(tx_data["json"]["defender"], 'ngc')
        self.assertEqual(len(tx_data["json"]["army"]), 2)

    def test_from_transaction(self):
        op_data = {
            'required_auths': [],
            'required_posting_auths': ['emrebeyler'],
            'id': 'dw-heist',
            'json': '{"username": "emrebeyler","amount": "260"}'
        }

        heist = Heist.from_op(op_data)
        self.assertEqual(heist.amount, '260')

    def test_from_transaction_invalid_custom_json_id(self):
        op_data = {
            'required_auths': [],
            'required_posting_auths': ['emrebeyler'],
            'id': 'dw-heist-invalid',
            'json': '{"username": "emrebeyler","amount": "260"}'
        }
        with self.assertRaises(ValueError):
            heist = Heist.from_op(op_data)



