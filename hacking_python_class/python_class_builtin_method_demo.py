class BuiltinDemo:

    def __init__(self, value: list = None, bool_value: bool = False, iter_value=None, context_obj=None,
                 slice_value=None):
        self.value = value
        self.bool_value = bool_value  # detect boolean context invocation
        self.iter_value = iter_value  # detect for loop/iteration context invocation
        self.context_obj = context_obj  # detect for with context manager invocation
        self.slice_obj = slice_value  # detect slice context

    # TODO:
    def __getitem__(self, item):
        print(f'invoking __getitem__ method with: {item}')
        return self.slice_obj[item]

    def __setitem__(self, key, value):
        print(f'invoking __setitem__ method with: {key} = {value}')
        self.slice_obj[key] = value

    # boolean context
    def __bool__(self):
        print(f'Invoking __bool__ method!')
        return self.bool_value

    def __len__(self):
        print(f'Invoking __len__ method!')
        return len(self.value)

    # iteration context
    def __next__(self):
        print('invoking __next__ method!')
        value = self.iter_value
        if self.iter_value == 0:
            print('finished iteration!')
            raise StopIteration('Finished iteration')
        self.iter_value -= 1
        return value

    def __iter__(self):
        print('invoking __iter__ method!')
        return self

    # with manager context
    def __enter__(self):
        print(f'invoking __enter__ method in with context')
        return self.context_obj

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            print(f'invoking __exit__ method in with context normally')
        else:
            print(f'invoking __exit__ method with error: {exc_val}!')
            return True  # no propagate exception. False will propagate error

    def __add__(self, other):
        return self.value + other.value


if __name__ == '__main__':
    obj1 = BuiltinDemo('hello', False, 10, 'context_value', [1, 2, 3])
    obj2 = BuiltinDemo(' world!', False, 10, 'context_value', [2, 3, 4])

    # boolean context use __bool__ or __len__ to detect the boolean value of an object
    print('true' if obj1 else 'false')

    print([i for i in obj1])  # iteration context **NOTE: There is another talks**

    with obj1 as o:
        print(f'Context returned object:{o}')
        # raise ValueError('context error!')

    print(obj1 + obj2)  # hello world!
    obj1[1] = 11
    print(obj1[1])
