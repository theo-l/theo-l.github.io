def function_generator():
    print('calling function generator')
    while True:
        initial_value = (yield)
        if isinstance(initial_value, str):
            print('----received string value')
            yield 'string'
        elif isinstance(initial_value, int):
            print('----received integer value')
            yield 'int'
        else:
            yield 'unknown'

if __name__ == "__main__":

    gen = function_generator()
    next(gen)  # to start a generator
    v = gen.send('liang')
    print(v)

    next(gen)
    v = gen.send(123)
    print(v)

    next(gen)
    v = gen.send([1, 2, 3])
    print(v)

    express_generator = (i for i in range(3))
    print(next(express_generator))
    print(next(express_generator))
    print(next(express_generator))
    print(next(express_generator))
