class DecoratorClass:
    def __init__(self, obj):
        print('calling decorator class')
        self.decorator = 'class'
        self.obj = obj

    def decorator_method(self, obj):
        print('calling decorator method')
        obj.decorator = 'method'
        return obj

    def __call__(self, obj):
        print('calling decorator instance')
        obj.decorator = 'instance'
        return obj


def decorator_function(obj):
    print('calling decorator function')
    obj.decorator = 'function'
    return obj

@DecoratorClass
def obj1():pass

@obj1.decorator_method
def obj2():pass

@obj1
def obj3():pass

@decorator_function
def obj4():pass

if __name__ == "__main__":
    # pass # show the decorator runtime 
    for ix, obj in enumerate([obj1, obj2, obj3, obj4], 1):
        print(f"obj{ix}'s decorator type is <{getattr(obj, 'decorator', 'unknown').upper()}>")
