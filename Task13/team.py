import json
class Team:
    def __init__(self, name, players):
        self.id = id(self)
        self.name = name
        self.players = players
class Player:
    def __init__(self, name, team):
        self.id = id(self)
        self.name = name
        self.team = team
class Match:
    def __init__(self, date, location, result, team1, team2):
        self.id = id(self)
        self.date = date
        self.location = location
        self.result = result
        self.team1 = team1.name
        self.team2 = team2.name
        self.players = [team1.players, team2.players]
def team_writer(team):
    my_team = {'id': team.id, 'name': team.name}
    with open('teams.txt', 'a') as f:
        f.write(json.dumps(my_team) + '\n')
        f.close()
def players_writer(player):
    my_player = {'id': player.id, 'name': player.name, 'team': player.team}
    with open('players.txt', 'a') as f:
        f.write(json.dumps(my_player) + '\n')
        f.close()
def match_writer(match):
    my_match = {'id': match.id, 'date': match.date, 'location': match.location, 'result': match.result, 'team1': match.team1, 'team2': match.team2, 'players': match.players}
    with open('match.txt', 'a') as f:
        f.write(json.dumps(my_match) + '\n')
        f.close()
def match_find(date):
    with open('match.txt', 'r') as f:
        line = f.readline()
        while line:
            line = json.loads(line)
            if line['date'] == date:
                print('During ' + date + ', the ' + line['team1'] + ' played against ' + line['team2'] + ' with the score: ' + match1.result)
            line = f.readline()
        f.close()
player1 = Player('Ronaldo', 'Dinamo')
players_writer(player1)
player2 = Player('Messi', 'Dinamo')
players_writer(player2)
player3 = Player('Zidan', 'Manch')
players_writer(player3)
player4 = Player('Pele', 'Barselona')
players_writer(player4)

team1 = Team('Manch', player3)
team2 = Team('Dinamo', [player1, player2])
team3 = Team('Barselona', player4)
team_writer(team1)
team_writer(team2)
team_writer(team3)

match1 = Match('20.02.2019', 'Minsk', '3:2', team1, team2)
match_writer(match1)
match2 = Match('21.02.2019', 'Gomel', '1:4', team2.name, team3.name)
match_writer(match2)
match3 = Match('22.02.2019', 'Brest', '2:1', team1.name, team3.name)
match_writer(match3)

match_find('21.02.2019')
