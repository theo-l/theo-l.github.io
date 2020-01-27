class BooleanDemo:

    def __init__(self, value):
        self.data = value

    # def __bool__(self):
        # print('__bool__:', end='')
        # return True if self.data else False

    def __len__(self):
        print('__len__:', end='')
        return 1 if self.data else 0

    def __gt__(self, other):
        print('__gt__:', end='')
        return self.data > other.data


if __name__ == '__main__':
    zero = BooleanDemo(0)
    one = BooleanDemo(1)
    print('true' if zero else 'false')
    print(one > zero)

