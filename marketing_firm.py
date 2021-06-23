from sweepstakes import Sweepstakes
from user_interface import UserInterface


class MarketingFirm:
    def __init__(self, the_name, storage):
        self.firm_name = the_name
        self.sweepstakes_storage = storage

    def create_sweepstakes(self):
        new_sweepstake_name = UserInterface.get_user_input_string("\n\tEnter the name of the "
                                                                  "sweepstakes\n "
                                                                  "\tyou'd like to create: ")
        new_sweepstake = Sweepstakes(new_sweepstake_name, list())
        self.sweepstakes_storage.append(new_sweepstake)

    def change_marketing_firm_name(self):
        self.firm_name = UserInterface.get_user_input_string("\n\tPlease enter the new name of "
                                                             "your\n "
                                                             "\tmarketing firm: ")

    def select_sweepstakes(self):
        #  Check that the sweepstakes storage is not empty
        if len(self.sweepstakes_storage) == 0:
            print("\n\tYou need to create some sweepstakes first.")
            return self.menu()
        else:
            #  Display the sweepstakes in the storage
            for the_sweepstakes in self.sweepstakes_storage:
                UserInterface.display_sweepstakes_info(the_sweepstakes.name)
            #  Then, allow the user to choose a specific sweepstakes, based off of the list of
            #  current sweepstakes.
            selected_sweepstakes = UserInterface.get_user_input_string("\n\tSelect a sweepstakes by\n"
                                                                       "\ttyping in the sweepstakes\n"
                                                                       "\tname here: ")
            for sweepstake_titles in self.sweepstakes_storage:
                if sweepstake_titles.name.lower().strip() == selected_sweepstakes.lower().strip():
                    option_four_check = UserInterface.display_sweepstakes_menu_options(sweepstake_titles.name)
                    self.return_to_main_menu(option_four_check, sweepstake_titles.name)

    def return_to_main_menu(self, option_four_check, sweepstakes_title):
        if option_four_check == 4:
            self.menu()
        else:
            option_four_recheck = UserInterface.display_sweepstakes_menu_options(sweepstakes_title)
            self.return_to_main_menu(option_four_recheck, sweepstakes_title)

    def menu(self):
        choice = UserInterface.display_marketing_firm_menu_options(self.firm_name)
        come_back_to_main_menu = 0
        if choice == 1:
            self.create_sweepstakes()
            self.menu()
        elif choice == 2:
            self.change_marketing_firm_name()
            self.menu()
        elif choice == 3:
            self.select_sweepstakes()
        elif choice == 4:
            choice = UserInterface.get_user_input_string("\n\tAre you sure you want to terminate\n"
                                                         "\tthe program? Enter 'y' for yes, 'n' for no: ")
            if choice.lower().strip() == 'y':
                print("Thank you for checking out my Marketing Firm Sweepstakes Generator!")
            else:
                self.menu()
