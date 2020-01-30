def package_bottle(bottle):
    def bag(drink='water'):
        print(f'----Open bag\n--Take bottle')
        bottle(drink)
        print(f'--Back bottle\n----Close bag\n')
    return bag


@package_bottle
def bottle(drink='water'):
    print(f'Open bottle\nPut <{drink}>\nDrink <{drink}>\nClose Bottle\n')


def bottle2(drink='water'):
    print(f'Open bottle\nPut <{drink}>\nDrink <{drink}>\nClose Bottle\n')


def bottle3(drink='water'):
    print(f'Open bottle\nPut <{drink}>\nDrink <{drink}>\nClose Bottle\n')


if __name__ == "__main__":
    # NOTE 1: check effect of a wrapper decorator
    # bottle('Coca Cola')
    # bottle2('Coca Cola')

    # NOTE 2: compare the effect of decorator and helper method call
    decorated_bottle3 = package_bottle(bottle3)
    decorated_bottle3_2 = package_bottle(bottle3)

    decorated_bottle3('Coca Cola')
    # NOTE: helper method call sometimes does not change the original object
    bottle3('Coca Cola') 
    
    # NOTE: So if any other place where we need use the object the decorator feature, we need call the helper method
    # decorated_bottle3_2('Coca Cola') 
