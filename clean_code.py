from typing import List, Optional, Union
"""Clean code rules:
- correct function names that describes what the function does
- documentation
- type annotation: type hinting
Union = a or b or c
Optional = a or None
- single responsibility of functions and classes 
    (should do only one thing with as few arguments (1-3) as possible!)

"""

def get_active_account(user_id:str = None) -> List:
    acct = []
    if user_id == None:
        return acct #return list of all active accts
    acct.append(user_id)
    return acct #just return 1 user active acct
print(get_active_account(5))