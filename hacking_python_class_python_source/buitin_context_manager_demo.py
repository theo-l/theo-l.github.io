class ContextManager:

    def __enter__(self):
        print(f'{"-"*40}\n<Enter with>:    ', end='')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if not exc_type:
            print(f' <exit ok!>\n{"-"*40}\n')
        else:
            print(f' <exit error: {exc_type}!>\n{"-"*40}\n' )
            return False# NOTE 3: True will not raise any more False will continue to raise error

    def work(self):
        print(':<working>:    ', end='')


if __name__ == '__main__':

    # NOTE 1: use context without error
    with ContextManager() as cm:
        cm.work()
        # NOTE 2: use context with raised error
        raise ValueError('context error')

