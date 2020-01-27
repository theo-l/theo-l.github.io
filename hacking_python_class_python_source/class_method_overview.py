class Employee:
    count = 0

    def __new__(cls, name):
        print(f'----Before init {cls.__name__} instance')
        return super().__new__(cls)

    def __init__(self, name):
        print(f'----Start init {self.__class__.__name__} instance')
        self.name = name
        Employee.count += 1

    @classmethod
    def get_count(cls):
        return f'Created: {cls.count} {cls.__name__}'

    @staticmethod
    def get_count2():
        return Employee.get_count()

    def work(self):
        print(f'{self.name} is working!\n')

    def __str__(self):
        return f'<Truckpad Employee: {self.name}>'

    def __call__(self, *args, **kwargs):
        return self.work()


if __name__ == '__main__':
    alice = Employee('alice')
    bob = Employee('bob')

    print(Employee.get_count())  # call CLASS method with class object, pass class object to method
    print(alice.get_count())  # call CLASS method with instance object, python will path the class object to method

    print(Employee.get_count2())  # call STATIC method
    print(alice.get_count2())  # call STATIC method

    # Employee.work() # call USER DEFINED method
    alice.work()  # call USER DEFINED method

    print(alice)  # call BUILTIN method

    alice()  # call INSTANCE directly
