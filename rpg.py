from terminal_munipulation import TerminalMunipulation as TermMunip
from hero import Hero
from slime import Slime

class RPG:
    def __init__(self) -> None:
        self.player = None
        self.enmy = None

    def run_game(self):
        RPG.welcome_display()
        self.hero_setup()
        self.game_loop()
        self.end_game()

    @staticmethod
    def welcome_display():
        TermMunip.clear_screen()
        welcome_message = """
                Welcome to RPG
    You will be a hero that will travel on adventure and fight bad guys! (working title)
        """
        print(welcome_message) #--------------------------> work on welcome message
        RPG.pause()
        TermMunip.clear_screen()

    def hero_setup(self):
        print('Character Creation:')
        self.player = Hero(input('Name: ')) #--------------------------->Verify input later
        RPG.pause()

    def game_loop(self):
        self.cunstruct_encounter()
        self.combat()

    def cunstruct_encounter(self):
        self.enemy = Slime() #---------------------------> Build cunstructor that will generate random encounters later

    def combat(self):
        TermMunip.clear_screen()
        while self.player.health > 0 and self.enemy.health > 0:
            self.player.attack(self.enemy)
            if self.enemy.health < 1:
                break
            self.enemy.attack(self.player)
        RPG.pause()
        TermMunip.clear_screen()

    def end_game(self):
        TermMunip.clear_screen()
        print(f'{self.player} {"lives to tell another tale" if self.player.health > 0 else "Dead in glorious combat"}') #---------------------> Work on end game

    @staticmethod
    def pause():
        input('\n\nPress enter to continue')