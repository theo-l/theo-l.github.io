from base_demo import Iterable

if __name__ == "__main__":
    iterable_object = Iterable([1,2,3,4,5,7,6])

    in_result = 10 in iterable_object
    print('\n', '<IN> iteration context:', in_result, f'\n{"-"*50}\n')


    print('\n', '<FOR> iteration context:', end='')
    for i in iterable_object:
        print(i)
    print(f'\n{"-"*50}\n')


    print('\n', '<LIST comprehension> iteration context:', [i for i in iterable_object], f'\n{"-"*50}\n')
    print('\n', '<SET comprehension> iteration context:', {i for i in iterable_object}, f'\n{"-"*50}\n')
    print('\n', '<DICT comprehension> iteration context:', {i:i for i in iterable_object}, f'\n{"-"*50}\n')

    # NOTE: Generator object
    print('\n', '<TUPLE comprehension> iteration context:', (i for i in iterable_object), f'\n{"-"*50}\n')
    
