import random

from contestant import Contestant
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
        choice = UserInterface.display_sweepstakes_menu_options(self.name)
        marketing_firm_menu = 0
        if choice == 1:
            first_name_new_contestant = UserInterface.get_user_input_string("\n\tEnter the first name "
                                                                            "of the new contestant here: ")
            last_name_new_contestant = UserInterface.get_user_input_string("\n\tEnter the last name "
                                                                           "of the new contestant here: ")
            email_new_contestant = UserInterface.get_user_input_string("\n\tEnter the new contestant's "
                                                                       "email here: ")
            registration_id_new_contestant = UserInterface.get_user_input_number("\n\tEnter a unique, six-digit "
                                                                                 "registration identifier for \n"
                                                                                 "the new contestant.")
            new_contestant = Contestant(first_name_new_contestant, last_name_new_contestant,
                                        email_new_contestant, registration_id_new_contestant)
            self.register_constestant(new_contestant)
            self.menu()
        elif choice == 2:
            print("\n\tHere are the results for the random sweepstakes drawing!")
            self.pick_winner()
            self.menu()
        elif choice == 3:
            self.view_contestants()
            self.menu()
        elif choice == 4:
            marketing_firm_menu = 4
        return marketing_firm_menu
