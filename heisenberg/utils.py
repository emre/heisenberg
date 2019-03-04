import datetime

from dateutil.parser import parse


def calculate_balance(resource_type, account_data):
    """Helper function to calculate the actual resource balances.

    The game client calculates the balance lazily - means that the balance
    in game database only updates once a related action occurs in the
    blockchain. This helper takes the regeneration into account from the
    last update.

    :param resource_type (str): Resource type. (drug | weapon | alcohol)
    :param account_data (dict): Account data
    :return (float): The actual balance
    """
    user_info = account_data["user"]
    building_info = account_data["buildings"]

    last_balance = user_info[f"{resource_type}s_balance"]
    last_update = parse(user_info["last_update"]).replace(tzinfo=None)
    diff = (datetime.datetime.utcnow() - last_update).total_seconds()
    regenerated_balance = user_info[f"{resource_type}_production_rate"] * diff
    operation_center = [b for b in building_info \
                        if b["building"] == "operation_center"]
    if not len(operation_center):
        bonus_balance = 0
    else:
        operation_center = operation_center[0]
        bonus_balance = regenerated_balance * operation_center["lvl"] * 0.005

    return last_balance + regenerated_balance + bonus_balance
