#***********************************************************
# Different kind of string type
#***********************************************************
def string_type_demo():
    # single quote is the same as double quote
    single_quote_string = 'spa"m'
    double_quote_string = "spa'm"

    triple_quote_string = '''
        ...
        spam
        ...
    '''
    escape_sequence_string = 'a\tp\na\0m'

    # raw string which don't escape the chars
    # useful when we need in some especial suituation
    raw_string = r'a\tp\na\0m'
    byte_string = b'I am a byte string'
    unicode_string = u'梁桂生'
    encode_unicode_string = unicode_string.encode('utf-8')

    # for obj in [single_quote_string, double_quote_string, triple_quote_string, escape_sequence_string, raw_string, byte_string, unicode_string, encode_unicode_string]:
    for key, value in locals().items():
        print(f'<{key}> := <{value}>\n')  # NOTE: f-string


#***********************************************************
# Different kind of string action
#***********************************************************
def string_action_demo():
    a, b = 'hello', 'world'

    # length of a string
    print(f'length of {a}:', len(a))

    # concatate two strings
    print(a + ',' + b)

    # repeat a string
    print('=' * 20)

    # check char/substring in string
    print('h' in a, 'he' in a, 'He' in a)

    # fetch indexed char of a string
    print(a[0], a[-1], a[-2])

    # change strings
    # NOTE: string is immutable, we can not change the element in-place
    # a[0]='H'

    # fetch a slice sub of string
    print(a[:], a[1:], a[:-1])

    # extended fetch a slice sub of string
    print(a[::2], a[::-1])

    # char code conversion
    print(ord('a'), chr(ord('a')))

    #********************
    # String methods
    #********************

    # change the string value
    changed_a = a[:].replace('h', 'H')
    print(changed_a)

    # find some substring's index
    print('hello'.find('a'), 'hello'.find('o'))

    # parse and split string
    print('aaa bbb ccc'.split())

    # participation
    print('aa:bb:cc'.partition(':'), 'aa:bb:cc'.rpartition(':'))

    # use seperator to join a string list
    print(''.join(list(a)))

    # upper(), lower(), capitalize()
    a = 'HeLlo'
    print(a.upper(), a.upper().lower(), a.capitalize(), a.title())

    # check if string is:
    # number, letter, number or letter
    print('123'.isnumeric(), '123'.isdigit(), '123'.isdecimal(), '123'.isalpha())
    print('UPPER'.isupper(), 'UPPER'.istitle(), 'lower'.islower(), 'lower'.istitle(), 'Title'.istitle())

    # check if string has some pattern
    print('astart'.startswith('a'))
    print('endb'.endswith('b'))


def string_format_demo():
    # %[(name)][flags][width][.precision]typecode
    print('old style format:', 'name=%s, age=%d' % ('dave', 30))
    print('old style format:', 'name=%(name)s, age=%(age)d' % {'name': 'dave', 'age': 30})

    # [[fill]align][sign][#][0][width][.precision][typecode]
    print('format style format:', 'name={}, age={}'.format('dave', 30))
    print('format style format:', 'name={1}, age={0}'.format(30,
                                                             'dave'))  # NOTE: use given index instead of default index
    print('format style format:', 'name={name}, age={age}'.format(name='dave', age=30))  # NOTE: use given name
    print('format style format:', 'name={name}, age={age}'.format(**{'name': 'dave', 'age': 30}))
    print('format style format:', 'name={0[name]}, age={0[age]}'.format({'name': 'dave', 'age': 30}))
    print('format style format:', 'name={data[name]}, age={data[age]}'.format(data={'name': 'dave', 'age': 30}))

    print('f-string style format:', f'name={"dave"}, age={30}')


if __name__ == "__main__":
    # string_type_demo()
    # string_action_demo()
    string_format_demo()
