EMPLOYEE_COUNT = 0
def build_truckpader(name, position): # employee factory method
    global EMPLOYEE_COUNT
    EMPLOYEE_COUNT += 1
    return {'name':name, 'position':position}

def work(truckpader):
    position  = truckpader.get('position')
    if position == 'android':
        print(f'{truckpader["name"]} is doing some KJ')
    elif position == 'frontend':
        print(f'{truckpader["name"]} is doing some HCJ')
    elif position == 'backend':
        print(f'{truckpader["name"]} is doing some PR')
    # elif position == 'po':
    #     print(f'{truckpader["name"]} is doing plaining')
    # elif position == 'infra':
    #     print(f'{truckpader["name"]} is doing maintenance')
    # elif position == 'bi':
    #     print(f'{truckpader["name"]} is doing statistics')
    else:
        print(f'Unknown truckpader position')


def do_task(*truckpaders):
    for truckpader in truckpaders:
        work(truckpader)


if __name__ == '__main__':
    liang = build_truckpader('liang', 'backend')
    parazinho = build_truckpader('parazinho', 'android')
    paulinha = build_truckpader('paulinha', 'frontend')
    # ale = build_truckpader('ale','po')
    # victor = build_truckpader('victor','infra')
    # gabriel = build_truckpader('gabriel','bi')
    print(f'build: {EMPLOYEE_COUNT} truckpaders!')

    work(liang) #>>> 'liang is doing some PR'
    work(parazinho) #>>> 'parazinho is doing some KJ'
    work(paulinha) #>>> 'paulinha is doing some HCJ'
    # work(ale)
    # work(victor)
    # work(gabriel)

    do_task(*[liang, parazinho, paulinha]) 
    # do_task(*[liang, parazinho, paulinha, ale, victor, gabriel]) 

