from pyltover.pyltover import Pyltover
from pyltover.enums import By

pyltover = Pyltover('RGAPI-12345678-1234-1234-1234-123456789012')

print(pyltover.get_account(By.RIOT_ID, 'Babimee', 'EUW'))

