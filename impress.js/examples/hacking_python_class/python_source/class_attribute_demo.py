class Meta(type):
    def __getattribute__(self, item):
        print(f'>>>>>>>>Access class attribute: {item} in Meta.__getattribute__!\n')
        return super(Meta, self).__getattribute__(item)

    def __getattr__(self, item): # mock 'age' as non initiated class attribute 
        print(f'>>>>>>>>Access class attribute: {item} in Meta.__getattr__!\n')
        return 25 if item == 'age' else super(Meta, self).__getattr__(item)
        
    def __setattr__(self, key, value):
        print(f'>>>>>>>>Set class attribute: <{key}> = <{value}> in Meta.__setattr__!\n')
        super(Meta, self).__setattr__(key, value)

class Employee(metaclass = Meta):
    count = 0

    def __init__(self, name):
        self.name = name
        Employee.count+=1

if __name__ == '__main__':
    alice = Employee('alice')  
    # print(Employee.count) # access defined class attribute

    # print('instance access class attribute:', end='')
    print(alice.count) # actually access class attpibute

    # Change class's attribute value, show instance's acess
    # Employee.count+=1
    # print('instance access class attribute:', end='')
    # print(alice.count)

    # Change instance's attribute value, show different
    # alice.count += 2
    # print(Employee.count)
    # print('instance access class attribute:', end='')
    # print(alice.count)

    print(Employee.age) # access non-defined class attribute 

