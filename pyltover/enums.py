from enum import Enum

class Loading(Enum):
    LAZY = 0
    EAGER = 1
    
class By(Enum):
    RIOT_ID = 1
    PUUID = 2