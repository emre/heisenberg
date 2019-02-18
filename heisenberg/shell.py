import cmd, sys

from .core import Heisenberg

def parse_arg(arg):
    arg = arg.strip()
    return arg.split()

class HeisenbergShell(cmd.Cmd):
    intro = 'Welcome to the Heisenberg shell. ' \
            'Type help or ? to list commands.\n'
    prompt = '(Heisenberg) '

    def do_set_credentials(self, arg):
        """set_credentials <username> <private_posting_key>"""
        try:
            self.username, self.password = parse_arg(arg)
        except ValueError:
            print("Invalid arguments")
            return

        self.heisenberg = Heisenberg(self.username, self.password)
        print("Credentials are set.")

    def do_heist(self, arg):
        amount = parse_arg(arg)[0]
        trx_id, block_num = self.heisenberg.heist(amount)
        print(
            f"{amount} DRUGs are invested to the daily heist.\n"
            f"(TRX ID: {trx_id}, Block num: {block_num})")

    def do_upgrade(self, arg):
        building = parse_arg(arg)[0]
        trx_id, block_num = self.heisenberg.upgrade(building)
        print(
            f"Broadcasted {building} upgrade.\n"
            f"(TRX ID: {trx_id}, Block num: {block_num})")

    def do_unit(self, arg):
        unit, amount = parse_arg(arg)
        trx_id, block_num = self.heisenberg.unit(unit, amount)
        print(
            f"Broadcasted a unit recruit. ({amount} {unit})\n"
            f"(TRX ID: {trx_id}, Block num: {block_num})")

    def do_exit(self, arg):
        sys.exit()


def run_shell():
    HeisenbergShell().cmdloop()