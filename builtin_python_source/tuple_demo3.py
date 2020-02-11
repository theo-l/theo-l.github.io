def tuple_demo():
    demo_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2)
    print(demo_tuple[:], demo_tuple[::2], demo_tuple[::-2])

    print(demo_tuple.count(1))
    print(demo_tuple.index(8))

    a, *b, c = demo_tuple
    print(a, b, c)

def namedtuple_demo():
    person 



if __name__ == "__main__":
    tuple_demo()
