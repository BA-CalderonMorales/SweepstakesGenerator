import user_interface

# region Class Instantiations (will move soon)
class Contestant:
    def __init__(self, first, last, email, registration_number):
        self.first_name = first
        self.last_name = last
        self.contestant_email = email
        self.registration_id = registration_number


class Sweepstakes:
    def __init__(self, the_name, all_contestants):
        self.name = the_name
        self.contestants = all_contestants
#  endregion


#  region UserInterface method checking

#  region Display_Message(Message)
user_interface.display_message("Hello World\n")
#  endregion

#  region Get_User_Input_String(Prompt)
the_word = user_interface.get_user_input_string("Enter a word: ")
#  endregion

#  region Get_User_Input_Number(Prompt)
the_number = user_interface.get_user_input_number("\nEnter a number: ")
#  endregion

#  region These print statements use get_user_input_string/number from above
print(f"{the_word}")
print(f"{the_number}")
#  endregion

#  region Display_Contestant_Info(Contestant)
contestant_one = Contestant("Brandon", "Calderon", "bcm@gmail.com", 131213)
user_interface.display_contestant_info(contestant_one)
#  endregion

#  region Display_Sweepstakes_Info
contestant_two = Contestant("Jim", "Jones", "jj@gmail.com", 145555)
contestant_three = Contestant("Carl", "Weezer", "cw@gmail.com", 154333)
contestant_four = Contestant("Bob", "Marley", "bobm@gmail.com", 181716)

the_contestants = {
    "one": contestant_one,
    "two": contestant_two,
    "three": contestant_three,
    "four": contestant_four
}

sweepstake_one = Sweepstakes("Luxury Cruise in LA", the_contestants)
user_interface.display_sweepstakes_info(sweepstake_one)
#  endregion

#  region Display_Sweepstakes_Selection_Menu
sweepstake_two = Sweepstakes("Flying over Canada", the_contestants)
sweepstake_three = Sweepstakes("Dune buggy in the Sahara", the_contestants)

the_list_of_sweepstakes = [sweepstake_one, sweepstake_two, sweepstake_three]
user_interface.display_sweepstakes_selection_menu(the_list_of_sweepstakes)

#  endregion

#  region Display_Marketing_Firm_Menu_Options
firm_name = "JWT"
user_interface.display_marketing_firm_menu_options(firm_name)
#  endregion

#  region Display_Sweepstakes_Menu_Options(Sweepstakes_name)
sweepstakes_name = "Luxury Cruise in LA"
user_interface.display_sweepstakes_menu_options(sweepstakes_name)
#  endregion

#  endregion