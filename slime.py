from enemy import Enemy
import random as r

class Slime(Enemy):
    def __init__(self) -> None:
        self.turn_options = ['pounce', 'regenerate']
        super().__init__(2)

    def attack(self, opponent):
        action = r.choice(self.turn_options)
        if action == 'pounce':
            opponent.health -= self.attack_damage*2
        elif action == 'regenerate':
            self.health += 5

        print(f'{self} : {action} : {opponent} health = {opponent.health} : {self} health = {self.health}')