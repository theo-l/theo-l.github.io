def meta_function(name:str, parents:tuple=None, attributes:dict=None):
    print('calling meta function to create class!')
    parents = parents or (object, )
    class_obj = type(name, parents, attributes)
    class_obj.name = 'function'
    return class_obj

class MetaDemo(type):
    def __new__(meta, name, parents, attributes):

        print('calling meta class to create class!')

        def meta_init(self):
            print('calling meta init')

        attributes = attributes or {} 
        attributes.update({
            '__init__': meta_init
        })

        cls_obj = super().__new__(meta, name, parents, attributes)
        cls_obj.name = 'class'
        return cls_obj 


class Demo(metaclass=meta_function):
    pass

class Demo3(metaclass=MetaDemo):
    def __init__(self):
        print('calling Demo3 init')


def append_attribute(cls):
    print('calling class decorator')
    cls.name = 'decorator'

    def my_init(self):
        print('calling my init')
    cls.__init__ = my_init

    return cls

@append_attribute
class Demo2:
    pass


Demo3()
