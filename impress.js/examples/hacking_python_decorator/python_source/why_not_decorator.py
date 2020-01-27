def tracer(callable):

    def wrapper(*args, **kwargs):
        print(f'Before calling: <{callable.__name__}>')
        result = callable(*args, **kwargs)
        print(f'After calling: <{callable.__name__}>')
        return result 

    return wrapper

def tracked_api():
    print(f'calling <tracked_api>')


if __name__ == "__main__":
    print(tracked_api) # Before decorated
    tracked_api = tracer(tracked_api)
    print(tracked_api) # After decorated
