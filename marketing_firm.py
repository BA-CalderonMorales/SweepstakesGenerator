from sweepstakes import Sweepstakes
from user_interface import UserInterface


class MarketingFirm:
    def __init__(self, the_name, storage):
        self.name = the_name
        self.sweepstakes_storage = storage

    def create_sweepstakes(self):
        new_sweepstake_name = UserInterface.get_user_input_string("\n\tEnter the name of the "
                                                                  "sweepstakes\n "
                                                                  "\tyou'd like to create: ")
        new_sweepstake = Sweepstakes(new_sweepstake_name, list())
        self.sweepstakes_storage.append(new_sweepstake)

    def change_marketing_firm_name(self):
        self.name = UserInterface.get_user_input_string("\n\tPlease enter the new name of "
                                                        "your\n "
                                                        "\tmarketing firm: ")

    def select_sweepstakes(self):
        selected_sweepstakes = UserInterface.get_user_input_string("\n\tSelect a sweepstakes by\n"
                                                                   "\ttyping in the sweepstakes\n"
                                                                   "\tname here: ")
        for index in self.sweepstakes_storage:
            if index.name.lower().strip() == selected_sweepstakes.lower().strip():
                print(index.name)

    def menu(self):
        UserInterface.display_marketing_firm_menu_options(self.name)