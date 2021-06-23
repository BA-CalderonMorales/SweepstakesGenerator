import random

from user_interface import UserInterface


class Sweepstakes:
    def __init__(self, the_name, all_contestants):
        self.name = the_name
        self.contestants = all_contestants

    def register_constestant(self, contestant):
        self.contestants.append(contestant)

    def pick_winner(self):
        random_pick = random.randint(0, len(self.contestants) - 1)
        for index in range(0, len(self.contestants)):
            if index == random_pick:
                self.contestants[index].key['win_or_lose'] = True
        for the_contestants in self.contestants:
            the_contestants.notify(the_contestants)

    def view_contestants(self):
        for contestant in self.contestants:
            UserInterface.display_contestant_info(contestant)

    def menu(self):
        UserInterface.display_sweepstakes_menu_options(self.name)