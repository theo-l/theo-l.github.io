def file_demo():

    print('\n\nRead file by readlines()\n')
    with open(__file__, 'r') as fp:
        lines = fp.readlines()
        print('type of readlines:', type(lines), '\n')
        for line in lines:
            print(line, end='')

    print('\n\nRead file by readline()\n')
    with open(__file__, 'r') as fp:
        line = fp.readline()
        while line:
            print(line, end='')
            line = fp.readline()

    print('\n\nRead file directly by the file object\n')
    with open(__file__, 'r') as fp:
        print('type of fp:', type(fp))
        for line in fp:
            print(line, end='')


if __name__ == "__main__":
    file_demo()
