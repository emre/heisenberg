import requests

BASE_API_URL = "https://api.drugwars.io"


class RestClient:
    """
    Base wrapper for the REST api of drugwars.
    """

    def __init__(self, base_url=None):
        self.base_url = base_url or BASE_API_URL
        self.session = requests.session()

    def get_absolute_url(self, path):
        """Joins the base API url with the path"""
        return f"{self.base_url}/{path}"

    def dynamic_global_properties(self):
        """Returns the globals used in the game.

        Example result:
            ```
            {
                'daily_percent': 3,
                'heist_percent': 3,
                'last_prod_update': '2019-03-04T12:55:44.001Z',
                 'drug_production_rate': 3671.530999999977,
                 'heist_pool': 82403306,
                 'balance': '66403.257 STEEM',
                 'steemprice': 0.3730699512
            }
            ```

        :return (dict): Game data
        """
        return self.session.get(
            self.base_url
        ).json()

    def fights(self, player):
        """Recent fights of the player.

        :param player: Player
        :return (list): A list of dictionaries including fight history.
        """
        return self.session.get(
            self.get_absolute_url(f'fights/{player}')
        ).json()

    def info(self, player):
        """User's game data. Buildings, resources, unit, etc...

        :param player: Player
        :return:  A list of dictionaries including fight history.
        """
        return self.session.get(
            self.get_absolute_url(f'user/{player}')
        ).json()

    def users(self, max_production_rate=420):
        """Get a list of players by maximum production rate.

        It's possible for the do pagination by using that parameter.

        :param max_production_rate: Maximum production rate.
        :return (list): A list of dictionaries including user data.
        """
        return self.session.get(
            self.get_absolute_url(f'users/{max_production_rate}')
        ).json()
