def main():

    a_list = [1, 2, 3, 4, 5, 6]
    a_tuple = (1, 2, 3, 4, 5, 6)
    a_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
    a_str = '123456'
    a_set = {1, 2, 3, 4, 5, 6}

    # python for loop can be used to many object types
    # Which is supported by the iteration protocol of python
    def iterate_object(name, obj):
        print(f'Displaying <{name.upper()}> object:', end='')
        for i in obj:
            print(f'{i}', end=',')
        print()

    iterate_object('list', a_list)
    iterate_object('tuple', a_tuple)
    iterate_object('dict', a_dict)
    iterate_object('string', a_str)
    iterate_object('set', a_set)

    with open('./sample_data.txt') as a_file:
        iterate_object('file', a_file)


if __name__ == "__main__":
    main()
