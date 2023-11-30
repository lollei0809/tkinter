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
    def __init__(self, name, rules=None):
        if rules is None:
            rules = RULES['rps']
        self.name = name.lower()
        self.rules = rules

    def __repr__(self):
        return f'PlayerObject({self.name})'

    def __gt__(self,other): # gt sets greater than
        return other.name in self.rules[self.name]

    def __eq__(self, other):
        return self.name == other.name


