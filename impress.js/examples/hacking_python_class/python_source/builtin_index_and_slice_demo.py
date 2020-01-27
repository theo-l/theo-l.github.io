class Indexer:
    def __init__(self, value=None):
        self.value = value or []

    def __index__(self):
        print(f'******** Access __index__ method')
        return 127

    def __getitem__(self, item):
        print(f'******** Access __getitem__: {item}')
        return self.value[item]

    def __setitem__(self, key, value):
        print(f'******** Access __setitem__:  <{key}> = <{value}>!')
        self.value[key] = value

    def __str__(self):
        return str(self.value)


if __name__ == '__main__':
    indexer = Indexer([1, 2, 3, 3, 4, 5])

    # print(indexer[0], end='\n\n')
    # indexer[0] = 100
    # print(indexer, end='\n\n')

    # print(indexer[0:2], end='\n\n')
    # indexer[0:2] = 50, 200, 300
    # print(indexer, end='\n\n')

    print(hex(indexer), end='\n\n')
    print(oct(indexer), end='\n\n')
    print(bin(indexer), end='\n\n')
