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
        self.name = UserInterface.get_user_input_string("\n\tPlease enter the name of "
                                                        "your\n "
                                                        "\tmarketing firm: ")