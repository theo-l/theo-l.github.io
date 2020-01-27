def interactive_generator():
    print('Send some thing as you can!')
    while True:
        value = (yield)
        print(f'type of value: {value} is {type(value)}')
        if isinstance(value, int):
            print(f'recieving integer value')
            yield f'integer value: {value}'
        elif isinstance(value, str):
            print(f'recieving string value')
            yield f'string value: {value}'


if __name__ == "__main__":
    it = interactive_generator()
    print(type(it))
    it.__next__()
    print(it.send('liang'))
    next(it)
    print(it.send(123))

