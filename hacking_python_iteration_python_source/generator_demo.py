import time
def function_generator():
    print('calling function generator')

    while True:
        initial_value = (yield)
        if isinstance(initial_value, str):
            time.sleep(2)
            print('received string value')
            yield 'string'
        elif isinstance(initial_value, int):
            time.sleep(2)
            print('received integer value')
            yield 'int'
        else:
            yield 'unknown'





if __name__ == "__main__":
    
    gen = function_generator()
    next(gen)
    gen.send('liang')
    v = next(gen)
    print('after send')

