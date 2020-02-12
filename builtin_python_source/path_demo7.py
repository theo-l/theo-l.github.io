def path_demo():
    from pathlib import Path

    parent_path = Path('./..')
    print('dirs in parent dir:', '\n'.join([str(x) for x in parent_path.iterdir() if x.is_dir()]))

    print('\n')

    current_path = Path.cwd()
    print('all python files', '\n'.join([str(x) for x in current_path.glob('**/*.py')]))
    demo_py = current_path/'dd.py'
    demo_py.touch()
    print('all python files', '\n'.join([str(x) for x in current_path.glob('**/*.py')]))

    home = Path.home()
    one_path = home / 'projects' / 'github' / 'theo-l.liang.io'

    print('path name:', one_path.name)
    print('path:', one_path)
    print('path root:', one_path.root)
    print('path parent:', one_path.parent)
    print('path parents:', list(one_path.parents))
    print('path components:', one_path.parts)



if __name__ == "__main__":
    path_demo()
