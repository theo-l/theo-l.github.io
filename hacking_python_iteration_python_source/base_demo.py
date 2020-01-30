import collections, copy
import functools, operator
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


def main():
    list_iter = Iterable([1, 2, 3, 4, 6, 5])
    list_iter2 = Iterable([1, 2, 3, 4, 6, 5])

    print('Iteration context in LIST builtin:', list(list_iter))
    print('Iteration context in TUPLE builtin:', tuple(list_iter))
    print('Iteration context in SET builtin:', set(list_iter))
    print('Iteration context in DICT builtin:', dict(zip(list_iter, list_iter2)))


    print('Iteration context in LIST COMPREHENSIONS:', [i for i in list_iter])
    print('Iteration context in TUPLE COMPREHENSIONS:', (i for i in list_iter)) # generate a generator
    print('Iteration context in SET COMPREHENSIONS:', {i for i in list_iter})
    print('Iteration context in DICT COMPREHENSIONS:', {i:j for i,j  in zip(list_iter, list_iter2)})


    print('Iteration context in ARGUMENT ITERATION:', *list_iter)

    for i in list_iter:
        print(i, end='')
    print()

    # print('Range iterator:', isinstance(range(10), ))
    print('Iteration context in MAP function: ', isinstance(map(lambda i: i*2, list_iter), collections.Iterator))
    print('Iteration context in FILTER function: ', isinstance(filter(lambda i: i%2==0, list_iter), collections.Iterator))

    print('Iteration context in SORTED function: ', sorted(list_iter)) # Return a real list object
    
    print('Iteration context in REDUCE function:', functools.reduce(lambda a,b: a+b, list_iter))
    print('Iteration contxt in SUM function:', sum(list_iter))
    print('Iteration contxt in MAX function:', max(list_iter))
    print('Iteration contxt in MIN function:', min(list_iter))
    print('Iteration contxt in ALL function:', all(list_iter))
    print('Iteration contxt in ANY function:', any(list_iter))

    str_list = Iterable(['a', 'b', 'c', 'd', 'e','f'])
    print(','.join(str_list))

    print('Iteration context in MEMBERSHIP test:', 1 in list_iter)

    iter1 = Iterable(['name', 'age','gender'])
    iter2 = Iterable(['liang', '32', 'M'])
    print(isinstance(zip(iter1, iter2), collections.Iterator))
    print('Iteration context in ZIP function:', dict(zip(iter1, iter2)))
    print('Iteration contxt in ZIP function:', list(zip(iter1, iter2)))

    a_dict = {'name':'liang'}
    print(isinstance(a_dict.keys(), collections.KeysView))
    print(isinstance(a_dict.values(), collections.ValuesView))
    print(isinstance(a_dict.items(), collections.ItemsView))
    

    # Muiltple vs Single iterator object 
    single_iter = Iterable([1,2,3,4,5,6], False)
    i1 = iter(single_iter)
    i2 = iter(single_iter)
    print(next(i1))
    print(next(i1))
    print(next(i2))
    print(next(i2))

    multiple_iter = Iterable([1,2,3,4,5,6])
    i1 = iter(multiple_iter)
    i2 = iter(multiple_iter)
    print(next(i1))
    print(next(i1))
    print(next(i2))
    print(next(i2))


if __name__ == "__main__":
    main()
