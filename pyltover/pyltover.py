from __future__ import annotations
import requests
from .enums import Loading, By
from .account import Account

class Pyltover:
    def __init__(self, api_key : str = None, loading_style : Loading = Loading.LAZY, region : str = 'europe'):
        self.api_key = api_key
        self.loading_style = loading_style
        self.region = region
        self.base_url = f'https://{self.region}.api.riotgames.com/'
        self.session = requests.Session()
        
    def make_request(self, endpoint : str, params : dict = None):
        if self.api_key:
            req = self.session.get(self.base_url+endpoint, params=params, headers={'X-Riot-Token': self.api_key})
            return req.json()
        
    def get_account(self, by: By, *args):
        if by == By.RIOT_ID:
            return Account.from_riot_id(self, *args)
        elif by == By.PUUID:
            return Account.from_puuid(self, *args)
        else:
            raise ValueError("Invalid method to get account")