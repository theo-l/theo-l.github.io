class Decorator:

    def __init__(self, callback):
        self.callback  = callback 

    def __call__(self, *args, **kwargs):
        print('calling instance callable protocol')
        return self.callback(*args, **kwargs)

    def __get__(self, instance, kwargs):
        print('calling descriptor protocol')
        def method_wrapper(*args, **kwargs):
            return self.callback(instance, *args, **kwargs)
        return method_wrapper
# 
@Decorator
def hello_function(): print('calling hello function!')

class Hello:
    @Decorator
    def hello_method(self): print('calling hello method!')
        

if __name__ == "__main__":
    hello_function()
    h = Hello()
    h.hello_method()
