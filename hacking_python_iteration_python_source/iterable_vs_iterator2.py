import collections
# iterable objects
list_iterable = [1, 2, 3, 4, 5]
tuple_iterable = (1, 2, 3, 4, 5)
set_iterable = {1, 2, 3, 4, 5}
dict_iterable = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}

for iterable_object in (list_iterable, tuple_iterable, set_iterable, dict_iterable):
    # print(iterable_object)

    # NOTE convert iterable object to iterator object
    iterator_object = iter(iterable_object)
    while True:
        try:
            # NOTE only iterator object can be used in next context
            print(next(iterator_object))
            # print(next(iterable_object))
        except StopIteration:
            print('\n\n')
            break

# iterator object in python
list_iter = iter(list_iterable)
tuple_iter = iter(tuple_iterable)
set_iter = iter(set_iterable)
dict_iter = iter(dict_iterable)
map_iter = map(lambda o: o * 2, [1, 2, 3, 4, 5])
filter_iter = filter(lambda o: o % 2 == 0, [1, 2, 3, 4, 5, 6, 7])
zip_iter = zip([1, 2, 3, 4, 5], [6, 7, 8, 9, 10])


for it in (list_iter, tuple_iter, set_iter, dict_iter, map_iter, filter_iter, zip_iter):
    print(type(it), isinstance(it, collections.Iterator))
