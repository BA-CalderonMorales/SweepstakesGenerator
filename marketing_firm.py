from sweepstakes import Sweepstakes
from user_interface import UserInterface


class MarketingFirm:
    "A class that will allow any marketing company to be able to create a sweepstake, \
    change the marketing firm name if they choose to, select a sweepstakes from a \
    list of sweepstakes, and terminate the program if they are finished using it."
    def __init__(self, the_name, storage):
        "The constructor containing the name of the firm and the list of sweepstakes"
        self.firm_name = the_name
        self.sweepstakes_storage = storage

    def create_sweepstakes(self):
        "The method that allows the current marketing firm to create a sweepstakes and \
        add it to the current sweepstake storage."
        new_sweepstake_name = UserInterface.get_user_input_string("\n\tEnter the name of the "
                                                                  "sweepstakes\n "
                                                                  "\tyou'd like to create: ")
        new_sweepstake = Sweepstakes(new_sweepstake_name, list())
        self.sweepstakes_storage.append(new_sweepstake)

    def change_marketing_firm_name(self):
        "The method that allows the current marketing firm to change the name of their \
        firm if they so choose to do so."
        self.firm_name = UserInterface.get_user_input_string("\n\tPlease enter the new name of "
                                                             "your\n "
                                                             "\tmarketing firm: ")

    def select_sweepstakes(self):
        "This method allows the marketing firm to select a sweepstake from the list of \
        sweepstakes that have been created."
        hold_current_option = 0
        hold_current_sweepstake = None
        #  Check that the sweepstakes storage is not empty
        if len(self.sweepstakes_storage) == 0:
            print("\n\tYou need to create some sweepstakes first.")
            return self.menu()
        else:
            print("\n\tHere are all the sweepstakes you can choose from\n")
            #  Display the sweepstakes in the storage
            for index in range(0, len(self.sweepstakes_storage)):
                if self.sweepstakes_storage[index].name is None:
                    self.sweepstakes_storage.pop()

            if len(self.sweepstakes_storage) > 0:
                for the_sweepstakes in self.sweepstakes_storage:
                    UserInterface.display_sweepstakes_info(the_sweepstakes.name)
            else:
                print("\tYou need to create some sweepstakes to choose from first.")
                self.menu()

            #  Then, allow the user to choose a specific sweepstakes, based off of the list of
            #  current sweepstakes.
            selected_sweepstakes = UserInterface.get_user_input_string("\n\tSelect a sweepstakes by\n"
                                                                       "\ttyping in the sweepstakes\n"
                                                                       "\tname here: ")
            for sweepstake_title in self.sweepstakes_storage:
                if sweepstake_title.name.lower().strip() == selected_sweepstakes.lower().strip():
                    hold_current_sweepstake = sweepstake_title
            hold_current_option = hold_current_sweepstake.menu()
            the_magic = [hold_current_option, hold_current_sweepstake]
            return the_magic

    def menu(self):
        "This method acts as the facade to the three previous methods. It will allow the user to: \
        1) create a sweepstake; 2) change the name of their firm; 3) select a sweepstake from \
        the current list of sweepstakes; and, 4) terminate the Sweepstake program."
        choice = UserInterface.display_marketing_firm_menu_options(self.firm_name)
        if choice == 1:
            self.create_sweepstakes()
            self.menu()
        elif choice == 2:
            self.change_marketing_firm_name()
            self.menu()
        elif choice == 3:
            previous_menu_option_chosen = self.select_sweepstakes()
            if previous_menu_option_chosen[0] == -1:
                self.menu()
            else:
                hold_current_sweepstake = previous_menu_option_chosen[1]
                hold_new_option = hold_current_sweepstake.menu()
                the_updated_magic = [hold_new_option, hold_current_sweepstake]
                self.previous_menu_loop(the_updated_magic)
        elif choice == 4:
            choice = UserInterface.get_user_input_string("\n\tAre you sure you want to terminate\n"
                                                         "\tthe program? Enter 'y' for yes, 'n' for no: ")
            if choice.lower().strip() == 'y':
                print("Thank you for checking out my Marketing Firm Sweepstakes Generator!")
            elif choice.lower().strip() == 'n':
                self.menu()

    def previous_menu_loop(self, the_list_containing_option_and_current_sweepstake):
        "This method is acting as a helper method for the self.menu() method."
        the_option = the_list_containing_option_and_current_sweepstake[0]
        the_sweepstake = the_list_containing_option_and_current_sweepstake[1]
        if the_option == -1:
            self.menu()
        else:
            the_updated_option = the_sweepstake.menu()
            the_new_list_containing_updated_option_and_current_sweepstake = [the_updated_option, the_sweepstake]
            self.previous_menu_loop(the_new_list_containing_updated_option_and_current_sweepstake)
