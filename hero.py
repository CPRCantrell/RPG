from compatants import Compatants

class Hero(Compatants):
    def __init__(self, name) -> None:
        self.turn_options = ['swing', 'break arm swing', 'snack']
        super().__init__(name, 30, 5)

    def attack(self, opponent):
        action = self.select_action()
        if action == 'swing':
            opponent.health -= self.attack_damage
        elif action == 'break arm swing':
            opponent.health -= self.attack_damage*2
        elif action == 'snack':
            self.health += 5

        print(f'{self} : {action} : {opponent} health = {opponent.health} : {self} health = {self.health}')

    def select_action(self):
        self.display_actions()
        return input('What action would you like to take: ').lower() #----------------------> validate user input later

    def display_action(self):
        for action in range(len(self.turn_options)):
            print(f'{action+1} - {self.turn_options[action]}')