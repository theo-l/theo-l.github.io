class Iterator:

    def __init__(self, value):
        self.data = value

    # def __iter__(self):
        # print(f'iter=>', end='')
        # self.ix = 0
        # return self
# 
    # def __next__(self):
        # print(f'next:', end='')
        # if self.ix == len(self.data):
            # raise StopIteration('iteration finished')
        # item = self.data[self.ix]
        # self.ix += 1
        # return item
# 
    # NOTE 1: fallback to index protocol 
    # def __getitem__(self, item): 
        # print(f'get[{item}]:', end='')
        # return self.data[item]


if __name__ == '__main__':
    iterator = Iterator(range(1, 5))

    # in for loop
    print([i ** 2 for i in iterator])

    # in builtin method which return one literal value
    print(sum(iterator))
    
    # in builtin method which return some other type value
    print(list(filter(lambda o: o%2==0, iterator)) )
