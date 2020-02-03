import collections
from base_demo import Iterable

if __name__ == "__main__":
    iterable_object = Iterable([1, 2, 3, 4, 6, 5])
    iterable_object2 = Iterable([1, 2, 3, 4, 6, 5])

    map_result = map(lambda o:o*2, iterable_object)
    print('\n', '<MAP> function iteration context:', map_result, isinstance(map_result, collections.Iterator),   f'\n{"-"*50}\n')

    filter_result = filter(lambda o:o%2==0, iterable_object)
    print('\n', '<FILTER> function iteration context:', filter_result, isinstance(filter_result, collections.Iterator),   f'\n{"-"*50}\n')

    zip_result = zip(iterable_object, iterable_object2)
    print('\n', '<ZIP> function iteration context:', zip_result, isinstance(zip_result, collections.Iterator),   f'\n{"-"*50}\n')

