if __name__ == "__main__":
    string = 'hello, python list comprehensions'

    print([ord(c.upper()) for c in string])
    print({ord(c.upper()) for c in string})
    print({c.upper():ord(c.upper()) for c in string})
    print((ord(c.upper()) for c in string)) # Generator

    print('\n', '-'*60, '\n')

    # Normal for loop
    list_ords = []
    for c in string:
        list_ords.append(ord(c.upper()))
    print(list_ords)


    set_ords = set()
    for c in string:
        set_ords.add(ord(c.upper()))
    print(set_ords)

    dict_ords = {}
    for c in string:
        dict_ords.update({c.upper():ord(c.upper())})
    print(dict_ords)
