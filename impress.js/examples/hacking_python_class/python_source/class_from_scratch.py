class_parents = (object, ) # specify a collection of parents
class_name = 'Employee' # Specify a name to class

class_attributes = {'name':'truckpader', 'salary':0} # specify a collection of data attributes

def work():
    print('i am working')

def bindable_work(self):
    print(f'{self.name} is working')

def bindable_raise_salary(self, percent):
    print(f'Raising salary:<{percent}> => ', end='')
    self.salary *= (1.0+percent)

def customized_init(self, name, salary=0):
    self.name = name 
    self.salary = salary

def customized_str(self):
    return f'<{class_name}: name={self.name}, salary={self.salary}>'

# Specify a collection of method attributes
class_methods={
    '__init__':customized_init,
    'work':bindable_work, 
    'raise_salary':bindable_raise_salary, 
    '__str__':customized_str,
    'work2': work 
}

# Create a class object from above components
MyClass = type(class_name, class_parents, {**class_attributes, **class_methods})

if __name__ == "__main__":

    # NOTE 1: inspect class attribute
    # print(f'{"-"*60}\nBUILTIN attributes: {[att for att in dir(MyClass) if att.startswith("__")]}\n{"-"*60}')
    # print(f'{"-"*60}\nUSER-DEFINED attributes: {[att for att in dir(MyClass) if not att.startswith("__")]}\n{"-"*60}')
    # print(f'{"-"*60}\nCLASS ALL attributes:'+ "\n".join(sorted([str(name)+":"+str(value) for name, value in MyClass.__dict__.items()]))+f'\n{"-"*60}')

    # NOTE 2; inspect the attribute of the created class object and its instance object 
    bob=MyClass('bob', 2000)
    # print('-'*60)
    # print(bob)
    # bob.raise_salary(0.2)
    # print(bob)
    # print('-'*60)


    bob.work()
    MyClass.work(bob)
    
