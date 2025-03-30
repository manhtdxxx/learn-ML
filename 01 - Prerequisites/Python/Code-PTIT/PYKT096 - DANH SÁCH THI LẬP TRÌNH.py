class Team:
    def __init__(self, maTeam, tenTeam, tenTruong):
        self.maTeam = 'Team{:02d}'.format(maTeam)
        self.tenTeam = tenTeam
        self.tenTruong = tenTruong


class Candidate:
    def __init__(self, maTS, tenTS, maTeam2):
        self.maTS = 'C{:03d}'.format(maTS)
        self.tenTS = tenTS
        self.maTeam2 = maTeam2  # maTeam2 là object của class Team

    def getIn4(self):
        return '{} {} {} {}'.format(self.maTS, self.tenTS, self.maTeam2.tenTeam, self.maTeam2.tenTruong)

teams = {}
for i in range(int(input())):
    tenTeam = input()
    tenTruong = input()

    team_object = Team(i+1, tenTeam, tenTruong)
    teams[team_object.maTeam] = team_object


candidates = []
for i in range(int(input())):
    tenTS = input()
    maTeam2 = input()

    candidates.append(Candidate(i+1, tenTS, teams[maTeam2]))


candidates.sort(key=lambda x: x.tenTS)
for i in candidates:
    print(i.getIn4())
