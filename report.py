def get_description():
    """Return random weather, just like the pros"""
    from random import choice
    possibilities = ['rain', 'snow', 'sleet', 'fog', 'sun', 'no else']
    return choice(possibilities)

def get_description():
    import random
    possibilities = ['rain', 'snow', 'sleet', 'fog', 'sun', 'no else']
    return random.choice(possibilities)

import random
def get_description():
    possibilities = ['rain', 'snow', 'sleet', 'fog', 'sun', 'no else']
    return random.choice(possibilities)
get_description()
#如果匯入的程式在很多地方會用到,則在函式外匯入

