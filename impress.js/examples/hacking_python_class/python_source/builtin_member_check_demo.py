class MemberShip:

    def __init__(self, value):
        self.data = value

    # def __contains__(self, item):
        # print('contains: ', end='')
        # return item in self.data
# 
    # NOTE 1: fallback to iteration protocol
    # def __iter__(self):
        # print('iter=> ', end='')
        # self.ix = 0
        # return self
   #  
    # def __next__(self):
        # print('next:', end='')
        # if self.ix == len(self.data): raise StopIteration
        # item = self.data[self.ix]
        # self.ix += 1
        # return item

    # NOTE 2: fallback to iteration protocol
    def __getitem__(self, item):
        print(f'get[{item}]:', end='')
        return self.data[item]


if __name__ == '__main__':
    x = MemberShip([1, 2, 3, 4, 5])
    print(3 in x)

    y = MemberShip('hello world')
    print('z' in y)
