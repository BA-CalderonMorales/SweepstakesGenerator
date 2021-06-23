"User Interface for Sweepstakes program. Only intention for these \
functions is to call on them to print the contents of data that's \
already been processed. No class variables were referenced from \
outside of this user interface. Will modify as each class that uses \
this user interface is created."


class UserInterface:

    @staticmethod
    def display_message(message):
        "Displays a message to the user."
        print(message)

    @staticmethod
    def get_user_input_string(prompt):
        "Takes in a string, uses that string to prompt the user to \
        enter a word or phrase."
        user_input = input(prompt)
        return user_input

    @staticmethod
    def get_user_input_number(prompt):
        "Takes in a string, uses that string to prompt the user to \
        enter a number or group of numbers."
        user_number = int(input(prompt))
        return user_number

    @staticmethod
    def display_contestant_info(contestant):
        "Takes in a Contestant() object, and then outputs the contents \
        of that Contestant via print(f'..')"
        first_name = contestant.key['first_name']
        last_name = contestant.key['last_name']
        email = contestant.key['email']
        registration = contestant.key['id']
        #  Print the contestant's information
        print(f"\n\tFirst Name: {first_name}\n"
              f"\tLast Name: {last_name}\n"
              f"\tEmail: {email}\n"
              f"\tRegistration Number: {registration}")

    @staticmethod
    def display_sweepstakes_info(sweepstakes_key):
        "Takes in a Sweepstakes() object and then outputs the name that's \
        in that current Sweepstakes object."
        the_sweepstakes_name = sweepstakes_key
        print("\n\tHere are the sweepstakes details\n")
        print(f"\t{the_sweepstakes_name}")

    @staticmethod
    def display_sweepstakes_selection_menu(all_sweepstakes):
        "Takes in a list of Sweepstakes() objects and then outputs the names \
        of each sweepstake to the screen."
        print("\tHere is the list of sweepstakes that are ongoing\n")
        print(f"\t{all_sweepstakes[0].name}\n"
              f"\t{all_sweepstakes[1].name}\n"
              f"\t{all_sweepstakes[2].name}")

    @staticmethod
    def display_marketing_firm_menu_options(firm_name):
        "Takes in a string to use for menu options that a specific marketing \
        firm should have if they are planning on making a sweepstake, or if \
        they are planning on modifying one. The program will end if the user \
        selects to 'Terminate the Sweepstakes program'"
        print(f"\n\tHere are {firm_name}'s options as a marketing firm\n")
        print(f"\t1. Create a sweepstakes\n"
              f"\t2. Change the firm name\n"
              f"\t3. Select a sweepstakes\n"
              f"\t4. Terminate the program")
        user_choice = UserInterface.get_user_input_number("\n\tPlease make a selection from the options above: ")
        decision = UserInterface.validate_user_input_menu_options(user_choice)
        if not decision[0]:
            print("That's not a valid selection. Please try again.")
            UserInterface.display_marketing_firm_menu_options(firm_name)
        else:
            return decision[1]

    @staticmethod
    def display_sweepstakes_menu_options(sweepstakes_name):
        "Takes in a sweepstakes name and provides options for a user to select \
        a specific change to the sweepstake that is currently being referenced \
        in sweepstakes_name parameter."
        print(f"\n\tSweepstake - {sweepstakes_name} - Menu options\n")
        print(f"\t1. Register a contestant\n"
              f"\t2. Pick a winner\n"
              f"\t3. View all contestants\n"
              f"\t4. Return to previous menu")  # Marketing Firm Menu
        user_choice = UserInterface.get_user_input_number("\n\tPlease make a selection from the options above: ")
        decision = UserInterface.validate_user_input_menu_options(user_choice)
        if not decision[0]:
            print("That's not a valid selection. Please try again.")
            UserInterface.display_sweepstakes_selection_menu(sweepstakes_name)
        else:
            return decision[1]

    @staticmethod
    def validate_user_input_menu_options(user_choice):
        "Handles data input validation. User can only choose between options 1-4. \
        anything else will return False. All valid inputs will return True, along \
        with the number they chose."
        valid_choice = {
            1: (True, 1),
            2: (True, 2),
            3: (True, 3),
            4: (True, 4)
        }
        return valid_choice.get(user_choice, (False, None))
