class ExtraBuiltin:

    def __str__(self):
        return 'calling __str__!'

    def __del__(self):
        print('calling __del__!')


if __name__ == '__main__':
    a = ExtraBuiltin()
    print(a)
    del a
