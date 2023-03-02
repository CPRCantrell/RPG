class Compatants:
    def __init__(self, name, health, attack_damgae) -> None:
        self.name = name
        self.health = health
        self.max_health = health
        self.attack_damage = attack_damgae
        pass

    def attack(self, opponent):
        pass

    def __str__(self) -> str:
        return self.name