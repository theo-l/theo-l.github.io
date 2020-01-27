:data-transition-duration: 1000
:js-body: plugins/substep.js
:css: plugins/substep.css
:skip-help: true

.. title:  Hacking python OOP & class

----

.. class:: center

Hacking python OOP & Class
===========================


    Author: *Liang Guisheng*

    Email: *theol.liang@gmail.com*

----


1. Intro to OOP & Class
==========================

1.1 What is OOP?
----------------

    OOP offers a different and often more effective way of looking at programming, in which we factor code to minimize redundancy and write new programs by customizing exist code instead of change it in-place

1.2 What is a Python class?
-------------------------------

.. class:: substep

    1. Class is python's OOP tool

    2. **Class is just a package of functions that use and process built-in object types**

    3. Class is designed to create and manage new objects which also support inheritance (a mechanism of code customization and reuse anything of exist class object)**

    *NOTE: in Python OOP(Class) is entirely optional, so we don't really need to use class to start*

1.3 Why class?
----------------

    1. Inheritance

        The common properties data structure need to be implemented only once for
        the general case and be reused by all types of instances we
        may build in the future

    2. Composition

        Enable us to build some complex object which need many other component work together, like in **GUI** programming

    3.  Features only in class

        1. Multiple instances: Essentially factories for generating one or more objects
        2. Customization via inheritance: Extend a class in the outside of the class itself
        3. Operator overloading: By providing special protocol builtin methods, class can work like python built-in types(slice, index)

1.4 Look into python class
--------------------------

    1. A name to identify a class
    2. **A collection of attributes to define the status/state of a class**
    3. **A collection of user-define methods to define the actions of a class**
    4. **A collection of special protocol built-in methods to overload the built-in behaviors of a class**

----

1.5 A simple python class
============================

.. code:: python

    class Employee:

        # declared class attributes
        employee_count = 0
        employee_position_count = {}

        # A fake private attribute by python convention
        _some_private_value='some private value'

        # declared some real private attribute, which can not access by instance/class directly
        __private_value = 'private'

        __slots__ = ['name', 'age', 'position', '_value'] # A python limited attribute access protocol

        def __new__(cls, *args, **kwargs): # Where create the instance object(self)
            return object.__new__(cls)

        def __init__(self, name: str = None, age: int = 0, position: str = None):

            # Instance's attributes
            self.name = name
            self.age = age
            self.position = position

            # Access class's attribute
            Employee.employee_position_count.setdefault(position, 0)
            Employee.employee_position_count[position] += 1
            Employee.employee_count += 1
            self._value = 'test'

        @property
        def value(self): # a kind of attribute based on **descriptor** protocol
            return self._value

        @value.setter
        def value(self, value):
            self._value = value

        def work(self): # instance method
            print(f'{self.name} is working now!')

        @classmethod
        def get_employee_count(cls): # class method
            print(f'Total employee: {cls.employee_count}')

        @staticmethod
        def get_employee_position_count(position: str = None): # static method
            if not position:
                print(f'Employee in {position}: {Employee.employee_position_count[position]}')
            print(f'Employee in {position}: {Employee.employee_position_count.get(position, 0)}')

        def __str__(self): # Instance & built-in method
            return f'({self.name} : {self.age} : {self.position})'

----


2. Class attributes
===========================

2.1 Attribute categories
------------------------

#. public attribute
#. private attribute
#. class attribute
#. descriptor managed attribute
#. instance attribute

2.2 Attribute search
--------------------------

* Attribute access in python

    When we use the following code in python, will invoke python's attribute search

    .. code:: python

        object.attribute

* Attribute search in general

    *it searches a tree of linked objects, looking for the first appearance of attribute that it can find*

* Attribute search in Class

    *Find the first occurrence of attribute by looking in object , then in all classes above it, from bottom to top and left to right.*

2.3 Special protocol method in Class for attribute access
---------------------------------------------------------

* __getattribute__(self, item): Any kind of attribute access
* __getattr__(self, item): Access non-exist(declared) attribute
* __setattr__(self, key, value): Set instance attribute
* descriptor access: __get__/__set__/__del__ descriptor managed attribute

----

Work with Class attribute
============================

.. code:: python

    class NameDescriptor:
        def __init__(self, value):
            print(f'Before init descriptor attribute value: {value}')
            self._value = value
            print(f'After init descriptor attribute value: {value}\n')

        def __get__(self, instance, klass):
            print(f'Before getting attribute in descriptor: <{self.__class__.__name__}>.__get__')
            result = self._value
            print(f'After getting attribute in descriptor: <{self.__class__.__name__}>.__get__\n')
            return result

        def __set__(self, instance, value):
            print(f'Before setting attribute in descriptor: <{self.__class__.__name__}>.__set__')
            self._value = value
            print(f'After setting attribute in descriptor: <{self.__class__.__name__}>.__set__\n')

    class EmployeeAttributeDemo:
        public_value = 'public'
        _fake_private_value = 'fake private value'  # python convention private attribute
        __real_private_value = 'not really a private value'  # real private attribute(which is not really private)
        name = NameDescriptor('alice')

        def __init__(self, instance_value):
            self.instance_value = instance_value

        def __setattr__(self, key, value):
            print(f'Before setting value of <{key}> => <{value}> in __setattr__')
            super(EmployeeAttributeDemo, self).__setattr__(key, value)
            print(f'After setting value of <{key}> => <{value}> in __setattr__ \n')

        def __getattr__(self, item):
            if item == '__len__': # avoid default invocation
                return super(EmployeeAttributeDemo, self).__getattr__(item)
            print(f'Before getting value of <{item}> in __getattr__')
            if item == 'age': return 25
            result = super(EmployeeAttributeDemo, self).__getattr__(item)
            print(f'After getting value of <{item}> in __getattr__ \n')
            return result

        def __getattribute__(self, item):
            if not item.startswith('__'):
                print(f'Before getting value of <{item}> in __getattribute__')
            result = super(EmployeeAttributeDemo, self).__getattribute__(item)
            if not item.startswith('__'):
                print(f'After getting value of <{item}> in __getattribute__\n')
            return result

    if __name__ == '__main__':
        # em = EmployeeAttributeDemo('original instance value')

        def check_attribute_access(obj, attribute, new_value=None):
            print(getattr(obj, attribute))
            setattr(obj, attribute, new_value)
            print(getattr(obj, attribute))

        # check_attribute_access(obj, 'public_value', 'another public value')
        # check_attribute_access(obj, '_fake_private_value', 'another fake private value')
        # check_attribute_access(obj, 'name', 'new descriptor attribute value')
        # check_attribute_access(obj, 'instance_value', 'new instance value')
        # check_attribute_access(obj, 'age', 20)
        # print(em.__real_private_value)  # cause error
        # print(em._EmployeeAttributeDemo__real_private_value)  # cause error

----

3. Class methods
========================

3.1 What is a Python class method ?
----------------------------------------

A class method is a function declared inside the declaration of class object. :)

3.2 What is the difference between method & function ?
--------------------------------------------------------

* A function is declared outside of a class(which does not rely on class)
* A method is declared inside a class (which is relies on class)
* How to bind a plain function to a class manually?
* Python callable objects *Function*, *Method*, *Class* and *Instance*


3.3 Class method categories
----------------------------------------------

#. Class methods: (**@classmethod**)
#. Static methods: (**@staticmethod**)
#. Instance methods: method(self, \*args, \*\*kwargs)
#. built-in methods: (__new__ / __init__, ... )

----

4. Python callable objects comparison
======================================

.. code:: python

    def unbindable_hello(): # function callable
        print('Hello, unbindable function')

    def plain_hello(name: str = None):  #function callable function: when bound to class, name is going to be treated as self
        print(f'Hello, {name or "World"}')

    def bindable_hello(mock_self, name: str = None): # function/method callable
        print(f'Hello, {mock_self.name or name}')

    class Hello:
        def __init__(self, name): # class callable protocol
            self.name = name or 'World'

        def __call__(self, *args, **kwargs): # instance callable protocol
            return f'Instance : {self.name}'

    if __name__ == '__main__':
        name = 'function vs method'

        unbindable_hello() # OK, NOTE: function call
        plain_hello(name) # OK

        Hello.hello = bindable_hello
        obj = Hello(name) # NOTE: class call
        obj.hello() # OK, NOTE: method call

        Hello.hello = plain_hello
        obj = Hello(name)
        obj.hello() # OK

        Hello.hello = unbindable_hello
        obj = Hello(name)
        obj.hello() # Fail

        print(obj()) # instance call

----

5. Work with Class&instance user-defined methods
================================================

.. code:: python

    class Hello:
        instance_count = 0

        def __init__(self, name: str = None):
            self.name = name
            Hello.instance_count += 1

        @classmethod
        def children(cls):
            return cls.instance_count

        @staticmethod
        def greeting(name: str = None):
            return f'Hello, static: {name or "World"}!'

        def hello(self, name: str = None):
            return f'Hello, instance: {name or self.name}!'

        def __str__(self):
            return f'Hello, {self.name}!'


    if __name__ == '__main__':
        obj1 = Hello('obj1')
        obj2 = Hello('obj2')

        # Class method invocation
        print(Hello.children()) # 2

        # Static method invocation with both class & instance
        print(Hello.greeting('Class greeting')) # Hello, static: Class greeting!
        print(obj1.greeting('Instance greeting')) # Hello, static: Instance greeting!

        # Instance method invocation with both class & instance
        print(Hello.hello(obj1)) # Hello, instance: obj1!
        print(obj1.hello()) # Hello, instance: obj1!

        # Class builtin method invocation with instance implicitly
        print(obj1) # Hello, obj1!
        print(obj2) # Hello, obj2!

----


6. Work with Python class built-in methods
===========================================

.. code:: python

    class BuiltinDemo:

        def __init__(self, value: list = None, bool_value: bool = False, iter_value=None, context_obj=None, slice_obj=None):
            self.value, self.bool_value, self.iter_value, self.context_obj, self.slice_obj = value, bool_value, iter_value, context_obj,slice_obj

        def __getitem__(self, item):
            print(f'invoking __getitem__ method with: {item}')
            return self.slice_obj[item]

        def __setitem__(self, key, value):
            print(f'invoking __setitem__ method with: {key} = {value}')
            self.slice_obj[key] = value

        def __bool__(self):
            print(f'Invoking __bool__ method!')
            return self.bool_value

        def __len__(self):
            print(f'Invoking __len__ method!')
            return len(self.value)

        def __next__(self):
            print('invoking __next__ method!')
            value = self.iter_value
            if self.iter_value == 0:
                print('finished iteration!')
                raise StopIteration('Finished iteration')
            self.iter_value -= 1
            return value

        def __iter__(self):
            print('invoking __iter__ method!')
            return self

        def __enter__(self):
            print(f'invoking __enter__ method in with context')
            return self.context_obj

        def __exit__(self, exc_type, exc_val, exc_tb):
            if exc_type is not None:
                print(f'invoking __exit__ method with error: {exc_val}!')
                return True  # no propagate exception. False will propagate error
            print(f'invoking __exit__ method in with context normally')

        def __add__(self, other):
            return self.value + other.value

    if __name__ == '__main__':
        obj = BuiltinDemo('demo', False, 10, 'context_value')
        print('true' if obj else 'false') # boolean context
        print([i for i in obj]) # iteration context
        with obj as o: # with context
            print(f'Context returned object:{o}')
            # raise ValueError('context error!') # with error
        print(obj1 + obj2)  # hello world!
        obj1[1] = 11
        print(obj1[1])

----


7. Python Class designs
=============================

* OOP & Inheritance: Is-a Relation
* OOP & Composition: Has-a Relation
* OOP & Delegation: Proxy object
    A controller class manage the access of another object which is embedded.
    *In python we often implemented this pattern with __getattr__ method hook*
* Extra class design-related topics
    #. Static & Class methods (**showed before**)
    #. Managed attributes (**Showed before**)
    #. Abstract superclasses
    #. Decorators
    #. Type subclasses & Meta classes

----

7.1 OOP & Inheritance Demo
===========================

.. code:: python

    class Employee:
        def __init__(self, name, salary=0):
            self.name = name
            self.salary = salary

        def work(self):
            return f'{self.name} does stuff'

        def raise_salary(self, percent):
            self.salary *= (1.0 + percent)

        def __repr__(self):
            return f'<Employee: name={self.name}, salaray={self.salary}>'


    class Chef(Employee):
        def __init__(self, name):
            Employee.__init__(self, name, 5000)

        def work(self):
            return f'{self.name} makes food'


    class Server(Employee):
        def __init__(self, name):
            Employee.__init__(self, name, 4000)

        def work(self):
            return f'{self.name} attend customer'


    if __name__ == '__main__':
        bob = Chef('Bob')
        lucy = Server('Lucy')

----


7.2 OOP & Composition Demo
==========================

.. code:: python

    from talks.hacking_python_class.class_inheritance_relation import Server, Chef


    class Customer:
        def __init__(self, name):
            self.name = name

        def order(self, server):
            print(f'Client <{self.name}> orders from {server}')
            server.work()

        def pay(self, server):
            print(f'Client <{self.name}> pays for item to {server}')
            server.work()


    class Oven:
        def bake(self):
            print('oven bakes')


    class PizzaShop:
        def __init__(self):
            self.server = Server('Pat')
            self.chef = Chef('Bob')
            self.oven = Oven()

        def order(self, name):
            customer = Customer(name)
            customer.order(self.server)
            self.chef.work()
            self.oven.bake()
            customer.pay(self.server)


    if __name__ == '__main__':
        tp_pizza = PizzaShop()
        tp_pizza.order('Python')

----

7.3 OOP & Proxy Demo
===========================

.. code:: python

    from talks.hacking_python_class.class_inheritance_relation import Chef


    class TracerWrapper:

        def __init__(self, obj):
            self.wrapped = obj  # this obj object is embedded in a proxy manager class TracerWrapper

        def __getattr__(self, attribute_name):
            if attribute_name == '__len__':
                return super(TracerWrapper, self).__getattr__(attribute_name)
            print(f'====before proxy tracing access of: {attribute_name}')
            result = getattr(self.wrapped, attribute_name)
            print(f'====after proxy tracing access of: {attribute_name}')
            return result


    if __name__ == '__main__':
        chef = TracerWrapper(Chef('bob'))
        # Call a method which is not exist in the proxy class TracerWrapper, will actually
        # call the managed object's method
        chef.work()

----

8. Python class from the scratch demo
======================================

.. code:: python

    class_parents = (object,)
    class_name = 'Employee'

    class_attributes = {'name': None, 'salary': 0}


    def bindable_work(self):
        print(f'{self.name} is working!')


    def customized_init(self, name, salary=0):
        self.name = name
        self.salary = salary


    def customized_raise_salary(self, percent):
        self.salary *= (1.0 + percent)


    def customized_str(self):
        return f'<{class_name}: name={self.name}, salary={self.salary}>'


    class_methods = {
        '__init__': customized_init,
        'work': bindable_work,
        'raise_salary': customized_raise_salary,
        '__str__': customized_str
    }

    Employee = type(class_name, class_parents, {**class_attributes, **class_methods})

    if __name__ == '__main__':
        bob = Employee('Bob', 2000)
        print(bob)
        bob.work()
        bob.raise_salary(0.2)
        print(bob)

----

9. What else ?
========================

1. Hacking python decorators, descriptors and metaclass
2. Hacking python iteration & comprehensions
3. Hacking python built-in data types

----

Thanks
==============
Happy hacking python