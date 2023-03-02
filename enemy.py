from compatants import Compatants

class Enemy(Compatants):
    def __init__(self, attack_damage) -> None:
        super().__init__('Enemy', 10, attack_damage)