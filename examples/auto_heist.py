from heisenberg.core import Heisenberg
from heisenberg.rest_client import RestClient
from heisenberg.utils import calculate_balance

import time


PLAYER_USERNAME = "<player_acc>"
PLAYER_POSTING_KEY = "<posting_key>"


def main():
    heisenberg = Heisenberg(PLAYER_USERNAME, PLAYER_POSTING_KEY)
    client = RestClient()
    while True:
        balance = calculate_balance('drug', client.info(PLAYER_USERNAME))
        print(f"{balance} drugs are available on {PLAYER_USERNAME}")
        tx_id, block_num = heisenberg.heist(int(balance * 0.99))
        print(f"Invested {int(balance * 0.99)} DRUGS. \n"
              f"Transaction ID: {tx_id}, Block num: {block_num}")
        time.sleep(300)


if __name__ == '__main__':
    main()