import collections
from base_demo import Iterable
import copy 

class Iterable:
   def __init__(self, data, multiple=True):
       self.data = data
       self.multiple = multiple
       self.ix = 0

   def __iter__(self):
       print('iter:', end='')
       if self.multiple: 
           print('reset index:', end='')
           self.ix = 0
           return copy.copy(self)
       return self

   def __next__(self):
       print('next:', end='')
       if  len(self.data) <= self.ix:
           raise StopIteration('finished iteration')
       result  = self.data[self.ix]
       self.ix += 1
       return result




if __name__ == "__main__":
    iterable_object = Iterable([1, 2, 3, 4, 6, 5])
    iterable_object2 = Iterable([1, 2, 3, 4, 6, 5])
    print('\n', '{LIST} constructor iteration context', list(iterable_object), '\n', '-' * 60, '\n') # NOTE: builtin type constructor
    print('\n', '{TUPLE} constructor iteration context', tuple(iterable_object), '\n', '-' * 60, '\n')
    print('\n', '{SET} constructor iteration context', set(iterable_object), '\n', '-' * 60, '\n')
    print('\n', '{DICT} constructor iteration context', dict(zip(iterable_object, iterable_object2)), '\n', '-' * 60, '\n')
    map_result = map(lambda o:o*2, iterable_object) # NOTE: function return iterator
    print('\n', '{MAP} function iteration context:', map_result, isinstance(map_result, collections.Iterator),   f'\n{"-"*50}\n')
    filter_result = filter(lambda o:o%2==0, iterable_object)
    print('\n', '{FILTER} function iteration context:', filter_result, isinstance(filter_result, collections.Iterator),   f'\n{"-"*50}\n')
    zip_result = zip(iterable_object, iterable_object2)
    print('\n', '{ZIP} function iteration context:', zip_result, isinstance(zip_result, collections.Iterator),   f'\n{"-"*50}\n')
    sorted_result = sorted(iterable_object) # NOTE: function return non-iterator
    print('\n', '{SORTED} function iteration context:', sorted_result, type(sorted_result), f'\n{"-"*50}\n' )
    sum_result = sum(iterable_object)
    print('\n', '{SUM} function iteration context:', sum_result, type(sum_result), f'\n{"-"*50}\n' )
    max_result = max(iterable_object)
    print('\n', '{MAX} function iteration context:', max_result, type(max_result), f'\n{"-"*50}\n' )
    min_result = min(iterable_object)
    print('\n', '{MIN} function iteration context:', min_result, type(min_result), f'\n{"-"*50}\n' )
    all_result = all(iterable_object)
    print('\n', '{ALL} function iteration context:', all_result, type(all_result), f'\n{"-"*50}\n' )
    any_result = any(iterable_object)
    print('\n', '{ANY} function iteration context:', any_result, type(any_result), f'\n{"-"*50}\n' )
    print('\n', '{FUNCTION parameter} iteration context', *iterable_object, f'\n{"-"*50}\n')
    print('\n', '{IN test} iteration context', 10 in iterable_object, f'\n{"-"*50}\n')
