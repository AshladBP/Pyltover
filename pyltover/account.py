from __future__ import annotations
import json
from .enums import Loading

class Account():
    def __init__(self, pyltover_instance, raw_data : dict):
        self.pyltover_instance = pyltover_instance
        self.raw_data = raw_data
        self._is_loaded = False
        
    def __str__(self):
        return json.dumps(self.raw_data, indent=4)
        
    def __getattribute__(self, name):
        data_fetched = object.__getattribute__(self, '_is_loaded')

        if not data_fetched and name != ['_fetch_data_from_puuid', '_fetch_data_from_riot_id'] and name != '_is_loaded':
            if 'puuid' in object.__getattribute__(self, 'raw_data'):
                self._fetch_data_from_puuid()
            else:
                self._fetch_data_from_riot_id()

        return object.__getattribute__(self, name)
    
    def _fetch_data_from_puuid(self):
        self.raw_data = self.pyltover_instance.make_request(f'riot/account/v1/accounts/{self.raw_data["puuid"]}')
        self._is_loaded = True
        
    def _fetch_data_from_riot_id(self):
        self.raw_data = self.pyltover_instance.make_request(f'riot/account/v1/accounts/{self.raw_data["gameName"]}/{self.raw_data["tagLine"]}')
        self._is_loaded = True
    
    @staticmethod
    def from_puuid(pyltover_instance, puuid : str):
        account = Account(pyltover_instance, {'puuid': puuid})
        if pyltover_instance.loading_style == Loading.EAGER:
            account._fetch_data_from_puuid()
        return account
    
    @staticmethod
    def from_riot_id(pyltover_instance, game_name : str, tag_line : str):
        account = Account(pyltover_instance, {'gameName': game_name, 'tagLine': tag_line})
        if pyltover_instance.loading_style == Loading.EAGER:
            account._fetch_data_from_riot_id()
        return account
    
    @property
    def puuid(self):
        return self.raw_data['puuid']
    
    @property
    def game_name(self):
        return self.raw_data['gameName']
    
    @property
    def tag_line(self):
        return self.raw_data['tagLine']
        