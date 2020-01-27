class Dev:
    def __init__(self, name):
        self.name = name

    def internal_issue_handle(self, description):
        print(f'DEV:[{self.name}] handling internal issue: <{description}>\n{"-"*60}\n')


class Leader(Dev):
    def external_issue_handle(self, description):
        print(f'LEADER:[{self.name}] handling external issue: <{description}>\n{"-"*60}\n')


class Team:
    def __init__(self, leader, dev):
        self.leader = leader
        self.dev = dev

    def __getattr__(self, item):
        if item.startswith('external'):
            print(f'{"-"*60}\nEXTERNAL issue is reporting to Team')
            return getattr(self.leader, item)
        if item.startswith('internal'):
            print(f'{"-"*60}\nINTERNAL issue is reporting to Team')
            return getattr(self.dev, item)
        return super(Team, self).__getattr__(item)


if __name__ == '__main__':

    # Create a team with a leader and dev
    alice = Leader('alice')
    bob = Dev('bob')
    team = Team(alice, bob)

    # NOTE 1: handle external issue
    team.external_issue_handle('product problem!')

    # NOTE 2: handle internal issue
    team.internal_issue_handle('bug problem!')
