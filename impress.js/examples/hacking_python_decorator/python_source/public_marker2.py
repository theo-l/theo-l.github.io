def mark_public(obj):
    obj.public = True
    return obj 

@mark_public
def public_function():pass

@mark_public
class PublicClass:pass

public_instance = PublicClass()
public_instance.__name__ = 'public_instance' # Just for demo

def request(obj):
    if getattr(obj, 'public', False):
        print(f'PUBLIC METHOD:<{obj.__name__}>')
    else:
        print(f'****NOT ALLOWED****:non public object: <{obj.__name__}>')

if __name__ == "__main__":
    print('-'*50, '\n') 
    request(public_function) 
    request(PublicClass)
    request(public_instance)
    print('-'*50, '\n') 
