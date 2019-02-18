from heisenberg.core import Heisenberg
import time


PLAYER_USERNAME = "[username]"
PLAYER_POSTING_KEY = "[private_posting_key]"
INVEST_AMOUNT = 420


def main():
    h = Heisenberg(PLAYER_USERNAME, PLAYER_POSTING_KEY)
    while True:
        tx_id, block_num = h.heist(INVEST_AMOUNT)
        print(f"Invested {INVEST_AMOUNT} DRUGS. \n"
              f"Transaction ID: {tx_id}, Block num: {block_num}")
        time.sleep(300)


if __name__ == '__main__':
    main()