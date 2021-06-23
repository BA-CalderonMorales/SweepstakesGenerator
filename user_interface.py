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
        return f"\nThis is what the user entered: {user_input}"

    @staticmethod
    def get_user_input_number(prompt):
        "Takes in a string, uses that string to prompt the user to \
        enter a number or group of numbers."
        user_number = int(input(prompt))
        return f"\nThis is what the user entered: {user_number}"

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
        "Takes in a Sweepstakes() object and then outputs the contestants \
        in that current Sweepstakes dictionary."
        the_sweepstakes_name = sweepstakes_key.name
        print("\n\tHere are the sweepstakes details\n")
        print(f"\t{the_sweepstakes_name}")
        print(f"\t{UserInterface.display_contestant_info(sweepstakes_key.contestants['one'])}\n"
              f"\t{UserInterface.display_contestant_info(sweepstakes_key.contestants['two'])}\n"
              f"\t{UserInterface.display_contestant_info(sweepstakes_key.contestants['three'])}\n"
              f"\t{UserInterface.display_contestant_info(sweepstakes_key.contestants['four'])}\n")

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
        print(f"\tCreate a sweepstakes\n"
              f"\tChange the {firm_name}'s firm name\n"
              f"\tSelect a sweepstakes\n"
              f"\tTerminate the Sweepstakes program")

    @staticmethod
    def display_sweepstakes_menu_options(sweepstakes_name):
        "Takes in a sweepstakes name and provides options for a user to select \
        a specific change to the sweepstake that is currently being referenced \
        in sweepstakes_name parameter."
        print(f"\n\tHere are the menu options for: {sweepstakes_name}")
        print(f"\tRegister a contestant\n"
              f"\tPick a winner\n"
              f"\tView all contestants\n"
              f"\tReturn to previous menu")  # Marketing Firm Menu
