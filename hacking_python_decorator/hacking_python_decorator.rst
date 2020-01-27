:data-transition-duration: 1000
:skip-help: true
:data-autoplay: 2

.. title:  Hacking python oop & class

----

Hacking python decorators
===========================

.. class:: center

Author: *Liang Guisheng*

Email: *theol.liang@gmail.com*

----

1. What is decorator and python decorator?
===============================================



1.1 What is decorator (literally & simulation)?
---------------------------------------------------------


1.2 What is a python decorator ?
----------------------------------

    Decorator is a tool to specify management code for function and class object, which inserted after the definition of function and class


1.3 A glance of python decorator
----------------------------------

Python decorator is just a simple protocol: a callable object receive a callable object and return a callable object

.. code:: python

    def public_decorator(callable):
        callable.public = True
        return callable

    def any_callable():
        pass

    @public_decorator
    def public_decorated_callable():
        pass


    if __name__ == '__main__':
        print('true' if getattr(any_callable, 'public', False) else 'false')
        public_marked_callable = public_decorator(any_callable)
        print('true' if getattr(public_marked_callable, 'public', False) else 'false')
        print('true' if getattr(public_decorated_callable, 'public', False) else 'false')

----

2. Why use decorator in python?
=========================================

* Decorators have a very explicit syntax which makes them easier to spot than helper function calls(in some where else)
* Decorators are applied once when the subject function or class is defined, no need to add extra code
* Because of both of the above points, decorators make users recognise the augment logic more directly

----


3. Decorator's categories
=========================================

3.1 Category by the type of decorator implementation
------------------------------------------------------

#. decorator function

    decorator implemented by function object

#. decorator class

    decorator implemented by class object, **which is always return a wrapped object**

3.2 Category by the return value of decorator
-------------------------------------------------------

#. marker decorator

    the returned decorated object is the same as the origin object

#. wrapper decorator

    the returned decorated object is different from the origin object

    **decorator class always return the instance of the decorator class, which is not the original object**

3.3 Category by the object type where decorator applied to
--------------------------------------------------------------
#. function decorator

    The decorated object is a plain python function object

#. class decorator

    The decorated object is a python class object

#. method decorator

    The decorated object is a python class method

3.4 Category by the complexity of implementation
------------------------------------------------------

#. A simple decorator(which do some action and return the origin object)
#. A simple nested decorator(decorator factory)
#. A wrapped decorator(which will wrap the origin object's action)

----

3.1 Decorator implementation type demo
========================================================

.. code:: python

    # Create a decorator with function definition
    def public_decorator_function(callable):
        callable.is_public = True
        return callable


    # Create a decorator with class definition
    class public_decorator_class:

        def __init__(self, callable):
            self.is_public = True
            self.callable = callable

        def __call__(self, *args, **kwargs):
            return self.callable(*args, **kwargs)


    def non_public_function():  # method without marker decorator
        print('non public function')


    @public_decorator_function
    def function_public_marked_function():  # method marked by decorator function
        print('function public marked function')


    @public_decorator_class
    def class_public_marked_function():  # method marked by decorator class
        print('class public marked function')


    # helper to mock 'is_public' mark check
    def request(callable):
        if not getattr(callable, 'is_public', False):
            print('Non public callable object is not allowed!')
            return
        callable()


    if __name__ == '__main__':
        request(function_public_marked_function)
        request(class_public_marked_function)
        request(non_public_function)

----

3.2 Decorator return value type demo
=========================================================

.. code:: python

    # decorator which return the original object
    def simple_marker_decorator(callable):
        callable.mark = 'simple'
        return callable


    # decorator wrapped the original object and return the wrapper
    def wrapped_marker_decorator(callable):
        def wrapper(*args, **kwargs):
            print(f'origin callable:{callable}')
            return callable(*args, **kwargs)

        wrapper.mark = 'wrapped'

        return wrapper


    def func1():
        print('Calling fun1')


    def func2():
        print('Calling fun2')


    if __name__ == '__main__':
        print(func1)
        # here is the same as
        # @simple_marker_decorator
        # def func1():
        #    ...
        func1 = simple_marker_decorator(func1)
        print(func1)

        print(func2)
        # here is the same as
        # @wrapped_marker_decorator
        # def func2():
        #    ...
        func2 = wrapped_marker_decorator(func2)
        print(func2)

----

3.3 Decorator application object type demo
=========================================================

.. code:: python

    def function_mark_decorator(callable):
        callable.mark = 'function'
        return callable

    def class_mark_decorator(klass):
        klass.mark = 'class'
        return klass

    def method_mark_decorator(method):
        method.mark = 'function'
        return method

    class function_only_mark_decorator_class:
        def __init__(self, func):
            self.func = func
            self.func.mark = 'function_only_mark_decorator_class'

        def __call__(self, *args, **kwargs):
            return self.func(*args, **kwargs)

    class compatible_function_and_method_decorator_class(function_only_mark_decorator_class):
        def __get__(self, instance, owner):
            return (lambda *args, **kwargs: self.func(instance, *args, **kwargs))

    @function_mark_decorator
    def function_callable():
        print(f'calling function callable object!')

    @function_only_mark_decorator_class
    def function_callable2():
        print(f'calling function callable with function_callable_with_function_only_mark_decorator_class')

    @compatible_function_and_method_decorator_class
    def function_callable3():
        print(f'calling function callable with compatible_function_and_method_decorator_class!')

    @class_mark_decorator
    class ClassCallable:

        def __init__(self):
            print('calling class callable object!')

        @method_mark_decorator
        def method_callable(self):
            print('calling method callable object!')

        @function_only_mark_decorator_class
        def method_callable2(self):
            print(f'calling method with function_only_mark_decorator_class')

        @compatible_function_and_method_decorator_class
        def method_callable3(self):
            print(f'calling method with compatible_function_and_method_decorator_class')

    if __name__ == '__main__':
        function_callable()
        obj = ClassCallable()
        obj.method_callable()
        function_callable2()
        # obj.method_callable2()  # cause error
        function_callable3()
        obj.method_callable3()

----

3.4 Decorator complexity type demo
==========================================================

.. code:: python

    def red_decorator(callable):
        callable.color = 'red'
        return callable
    def green_decorator(callable):
        callable.color = 'green'
        return callable
    def color_decorator(color):
        def dynamic_color_decorator(callable):
            callable.color = f'<{color.upper()}>'
            return callable
        return dynamic_color_decorator
    def tracer_decorator(callable):
        def wrapper(*args, **kwargs):
            mark = '====>'
            print(f'{mark}Before calling method')
            result = callable(*args, **kwargs)
            print(f'{mark}After calling method')
            return result
        return wrapper
    def labeled_tracer(label):
        def tracer_decorator(callable):
            def wrapper(*args, **kwargs):
                print(f'{label}Before calling method!')
                result = callable(*args, **kwargs)
                print(f'{label}After calling method!\n')
                return result
            return wrapper
        return tracer_decorator

    @red_decorator
    def static_red_callable():
        print('static red callable')
    @green_decorator
    def static_green_callable():
        print('static green callable')
    @color_decorator('red')
    def dynamic_red_callable():
        print('dynamic red callable')
    @color_decorator('green')
    def dynamic_green_callable():
        print('dynamic green callable')

    def check_color(callable):
        print(f'Color of callable is: {getattr(callable, "color", None)}')

    @tracer_decorator
    def tracked_callable():
        print('Tracked callable object')

    @labeled_tracer('####>')
    def label_tracked_callable1():
        print('Label tracked callable object 1')

    @labeled_tracer('@@@@>')
    def label_tracked_callable2():
        print('Label tracked callable object 2')

    if __name__ == '__main__':
        check_color(static_red_callable)
        check_color(static_green_callable)
        check_color(dynamic_red_callable)
        check_color(dynamic_green_callable)
        tracked_callable()
        label_tracked_callable1()
        label_tracked_callable2()

----

4. Pros and Cons
================================

* Pros

    * Explicit syntax
    * Code maintenance
    * Consistency

* Cons

    * Change the type of origin object
    * Introduced extra calls

----

5. Decorator applications Examples
============================================

#. tracking callable's invocation
#. Register api endpoint
#. Parameter data validation
#. Data caching
#. Context provider
#. Singleton pattern
#. Access control
#. ...

----


6. Register api endpoint with call tracking demo
========================================================


----

7. What else?
=========================================================
* Hacking python





