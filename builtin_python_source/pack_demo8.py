def pack_and_unpack_demo():
    #unpack
    for sequence in ['hello world', list(range(10)), tuple(range(10, 20))]:

        a, b, *c = sequence
        print(a, b, c)
        print(sequence[0], sequence[1], list(sequence[2:]))
        print()
        *a, b, c = sequence
        print(a, b, c)
        print(list(sequence[:-2]), sequence[-2], sequence[-1])

        print()
        a, *b, c = sequence
        print(a, b, c)
        print(sequence[0], list(sequence[1:-1]), sequence[-1])
        print()

    set_data = set(range(30, 40))
    a, b, *c = set_data
    print(a, b, c)
    *a, b, c = set_data
    print(a, b, c)
    a, *b, c = set_data
    print(a, b, c)

    #pack 
    print([*[1, 2, 3, 4], *(15, 16, 17, 18), *{21, 22, 23}])
    print({**{'name':'liang'}, **{'gender':'m'}})


if __name__ == "__main__":
    pack_and_unpack_demo()
