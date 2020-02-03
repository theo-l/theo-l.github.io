from base_demo import Iterable

if __name__ == "__main__":
    iterable_obj = Iterable([1,2,3,4,6,5])
    iterable_obj2 = Iterable([1,2,3,4,6,5])
    # NOTE 1: use an iterable object in list call will use iterable protocol
    print( '\n', '<LIST> constructor iteration context', list(iterable_obj), '\n', '-'*60, '\n')

    # NOTE 2: use an iterable object in tuple call will use iterable protocol
    print( '\n', '<TUPLE> constructor iteration context', tuple(iterable_obj), '\n', '-'*60, '\n')

    # NOTE 3: use an iterable object in set call will use iterable protocol
    print( '\n', '<SET> constructor iteration context', set(iterable_obj), '\n', '-'*60, '\n')

    # NOTE 4: use an iterable object in dict call will use iterable protocol
    print( '\n', '<DICT> constructor iteration context', dict(zip(iterable_obj, iterable_obj2)), '\n', '-'*60, '\n')








