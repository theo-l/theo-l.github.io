from base_demo import Iterable

if __name__ == "__main__":
    iterable_object = Iterable([1,2,3,4,6,5,3])
    print('\n', '<FUNCTION parameter> iteration context', *iterable_object, f'\n{"-"*50}\n')
