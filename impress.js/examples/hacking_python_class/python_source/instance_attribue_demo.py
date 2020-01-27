class Employee:
    def __init__(self, name):
        self.name = name # initiate instance's attribute

    def __getattribute__(self, item):
        print(f'--------Access instance attribute: <{item}> in Employee.__getattribute__!\n')
        return super(Employee, self).__getattribute__(item)

    def __getattr__(self, item): # mock 'age' as non initiated instance attribute
        print(f'--------Access instance attribute: {item} in Employee.__getattr__!\n')
        return 25 if item == 'age' else super(Employee, self).__getattr__(item)

    def __setattr__(self, key, value):
        print(f'--------Set instance attribute: <{key}>=<{value}> in Employee.__setattr__!\n')
        super(Employee, self).__setattr__(key, value)

if __name__ == '__main__':
    alice = Employee('alice') 
    print(alice.name) # access defined attribute
    print(alice.age) # access non-exist attribute
