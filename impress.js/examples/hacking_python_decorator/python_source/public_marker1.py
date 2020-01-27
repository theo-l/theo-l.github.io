def public_function():pass  # a function object 
class PublicClass:pass # a class object 
public_instance = PublicClass() # an instance object 
public_instance.__name__ = 'public_instance' # just for demo later use

def mark_public(obj):
    obj.public = True
    return obj 

def request(obj):
    if getattr(obj, 'public', False):
        print(f'PUBLIC OBJECT:<{obj.__name__}>')
    else:
        print(f'****NOT ALLOWED****:non public object: <{obj.__name__}>')

if __name__ == "__main__":
    request(public_function) 
    request(PublicClass)
    request(public_instance)

    print()
    public_function1 = mark_public(public_function) 
    PublicClass1 = mark_public(PublicClass)

    request(public_function1) 
    request(PublicClass1)
    request(public_instance)

