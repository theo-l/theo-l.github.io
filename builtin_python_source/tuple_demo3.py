def tuple_demo():
    demo_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2)
    print(demo_tuple[:], demo_tuple[::2], demo_tuple[::-2])

    print(demo_tuple.count(1))
    print(demo_tuple.index(8))

    a, *b, c = demo_tuple # unpack 
    print(a, b, c)

    sc = (*(1,2,3), *(3,4,5)) # pack 
    print(sc)

def namedtuple_demo():
    from collections import namedtuple

    Truckpader = namedtuple('Truckpader', 'name, gender')
    liang = Truckpader('liang', 'm')
    # liang = Truckpader('liang', 'm', 'python') # NOTE: error
    print(liang.name, liang.gender)
    print(liang[0], liang[1])

    Truckpader2 = namedtuple('Truckpader2', ['name', 'gender'])
    liang = Truckpader2('liang', 'm')
    print(liang, liang.name, liang.gender)

    liang = Truckpader2(name='Liang', gender='M')
    print(liang, liang.name, liang.gender)

    name, gender = liang 
    print(f'Name={name}, Gender={gender}')


if __name__ == "__main__":
    # tuple_demo()
    namedtuple_demo()
