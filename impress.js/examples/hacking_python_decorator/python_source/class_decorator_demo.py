class Public:

    def __init__(self, callable):
        self.callable=callable
        self.public = True

    def __call__(self, *args, **kwargs):
        return self.callable(*args, **kwargs)

def detect_name(callable):
    print(f'callable name: {callable.__name__}')
    return callable


@Public
@detect_name
def public_api():
    print('"calling public api"')


if __name__ == "__main__":
    print(type(public_api))
    public_api()
    
