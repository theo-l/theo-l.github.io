def bottle_decorator(bottle):
    bottle.decoration = 'string'
    return bottle


@bottle_decorator
def bottle(drink='water'):
    print( f'''{"-"*40}\nOpen bottle\nPut {drink}\nDrink {drink}\nClose bottle\n{"-"*40}''')


def bottle2(drink='water'):
    print( f'''{"-"*40}\nOpen bottle\nPut {drink}\nDrink {drink}\nClose bottle\n{"-"*40}''')


def check_bottle_decoration(bottle):
    print(f'Bottle <{bottle.__name__}> is decorated with {{{getattr(bottle, "decoration")}}}' if getattr(bottle, 'decoration', False) else f'Bottle <{bottle.__name__}> has not been decorated')

if __name__ == "__main__":
    # NOTE 1: check the effect of decorator, has different  
    check_bottle_decoration(bottle)
    check_bottle_decoration(bottle2)

    # NOTE 2: check the function of the decorated object, no different
    bottle('Coca Cola')
    bottle2('Coca Cola')

    # NOTE 3: change directly applied into the original object 
    decorated_bottle2 = bottle_decorator(bottle2)
    check_bottle_decoration(decorated_bottle2) 
    check_bottle_decoration(bottle2)

    
