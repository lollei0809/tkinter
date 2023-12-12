import random

RULES = {'rps': {'rock': ['scissors'],
                 'paper': ['rock'],
                 'scissors': ['paper']
                 },

         'rpsls': {'rock': ['scissors', 'lizard'],
                   'paper': ['rock', 'spock'],
                   'scissors': ['paper', 'lizard'],
                   'lizard': ['paper', 'spock'],
                   'spock': ['scissors', 'paper']
                   },
         }


class PlayerObject:

    def __init__(self, name=None, rules=None):
        if rules is None:
            rules = RULES['rps']
        self.rules = rules
        if name is None:
            name = self.random_object()
        name = name.lower()
        if name not in rules:
            raise ValueError("name must be valid object")
        else:
            self.name = name

    def random_object(self):
        random.choice("rock","paper","scissors")

    def __repr__(self):
        return f'PlayerObject({self.name})'

    def __gt__(self, other):  # gt sets greater than: return true if in the list of objects it can beat
        return other.name in self.rules[self.name]

    def __eq__(self, other):
        return self.name == other.name


class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.current_object = None

    def reset_object(self):
        self.current_object = None

    def win_round(self):
        self.score += 1

    def __repr__(self):
        return f'name: {self.name}\nscore: {self.score}\ncurrent object: {self.current_object}'


class Human(Player):
    def choose_object(self, choice):
        self.current_object = PlayerObject(choice)


class Computer(Player):
    def __init__(self):
        super().__init__("Computer")

    def choose_object(self):
        self.current_object = PlayerObject.random_object()


class Game:

    def __init__(self):
        self.current_round = 0
        self.round_result = None
        self.round_winner = None
        self.players = []
        self.max_rounds = 0

    def add_human_player(self,name):
        self.players.append(Human(name))


    def add_computer_player(self):
        self.players.append(Computer())

    def set_max_rounds(self,num):
        if isinstance(num,int):
            self.max_rounds = num
        else:
            raise ValueError("max rounds must be an integer")

    def find_winner(self):
        if PlayerObject.__gt__(self.players[0],self.players[1]):
            self.round_result = "WON"
            self.round_winner = self.players[0]
            self.players[0].score+=1
        elif PlayerObject.__gt__(self.players[1],self.players[0]):
            self.round_result = "WON"
            self.round_winner = self.players[1]
            self.players[1].score += 1
        else:
            self.round_result ="DRAW"
        self.max_rounds-=1

    def next_round(self):
        self.current_round+=1
        self.round_result = None
        self.round_winner = None
        for player in self.players:
            player.reset_object()


    def is_finished(self):
        if self.current_round>=self.max_rounds:
            return True

    def reset(self):
        self.current_round =0
        for player in self.players:
            player.score = 0

    def report_round(self):
        return f'{self.players[0].name} chose {self.players[0].current_object}\n{self.players[1].name} chose {self.players[1].current_object}'
        if self.round_result =='WON':
            return f'round won by {self.round_winner}'
        else:
            return 'round is a draw'

    def report_score(self):
        return f'{self.players[0].name}: {self.players[0].score}\n{self.players[1].name}: {self.players[1].score}'

    def report_winner(self):
        if self.players[0].score>self.players[1].score:
            return f'{self.players[0].name} won overall'
        elif self.players[1].score>self.players[0].score:
            return f'{self.players[1].name} won overall'
        else:
            return 'draw overall'















