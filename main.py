# region Class Instantiations (will move soon)
from marketing_firm import MarketingFirm
from sweepstakes import Sweepstakes
from user_interface import UserInterface
from contestant import Contestant

#  endregion

#  region UserInterface method checking

"""
#  Uncomment this area to view how I was handling checking each method in the user_interface.py file.
#  region Display_Message(Message)
UserInterface.display_message("Hello World\n")
#  endregion

#  region Get_User_Input_String(Prompt)
the_word = UserInterface.get_user_input_string("Enter a word: ")
#  endregion

#  region Get_User_Input_Number(Prompt)
the_number = UserInterface.get_user_input_number("\nEnter a number: ")
#  endregion

#  region These print statements use get_user_input_string/number from above
print(f"{the_word}")
print(f"{the_number}")
#  endregion

#  region Display_Contestant_Info(Contestant)
contestant_one = Contestant("Brandon", "Calderon", "bcm@gmail.com", 131213)
UserInterface.display_contestant_info(contestant_one)
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
UserInterface.display_sweepstakes_info(sweepstake_one)
#  endregion

#  region Display_Sweepstakes_Selection_Menu
sweepstake_two = Sweepstakes("Flying over Canada", the_contestants)
sweepstake_three = Sweepstakes("Dune buggy in the Sahara", the_contestants)

the_list_of_sweepstakes = [sweepstake_one, sweepstake_two, sweepstake_three]
UserInterface.display_sweepstakes_selection_menu(the_list_of_sweepstakes)

#  endregion

#  region Display_Marketing_Firm_Menu_Options
firm_name = "JWT"
UserInterface.display_marketing_firm_menu_options(firm_name)
#  endregion

#  region Display_Sweepstakes_Menu_Options(Sweepstakes_name)
sweepstakes_name = "Luxury Cruise in LA"
UserInterface.display_sweepstakes_menu_options(sweepstakes_name)
#  endregion

"""

#  endregion - User_Interface check

#  region Contestant method checking
contestant_one = Contestant("Brandon", "Calderon", "bacm@gmail.com", 121314)
contestant_two = Contestant("Jim", "Jones", "jj@gmail.com", 101205)
contestant_three = Contestant("Billy", "Joe-Bob", "bjb@gmail.com", 234567)
#  Works as expected
contestant_one.key['win_or_lose'] = True
contestant_one.notify(contestant_one)
#  endregion

#  region Sweepstakes method checking

contestant_one.key['win_or_lose'] = False
sweepstakes_one = Sweepstakes("Life in LA", list())
print(sweepstakes_one.name)
print(sweepstakes_one.contestants)  # Empty list

# Works as expected - Register_Contestant
sweepstakes_one.register_constestant(contestant_one)  # Append the list
print(sweepstakes_one.contestants)  # Print the list
print(UserInterface.display_contestant_info(sweepstakes_one.contestants[0]))  # Print specific parts of that list
sweepstakes_one.register_constestant(contestant_two)
sweepstakes_one.register_constestant(contestant_three)

# Works as expected - Pick_Winner
sweepstakes_one.pick_winner()

# Works as expected - View_Contestants
sweepstakes_one.view_contestants()

# Works as expected - Menu
sweepstakes_one.menu()

#  region MarketingFirm method checking

#  Works as expected - Instantiate a MarketingFirm
sweepstakes_list = list()
jwt_marketing = MarketingFirm("JWT Marketing", sweepstakes_list)

#  Works as expected - Create_Sweepstakes
jwt_marketing.create_sweepstakes()
print(jwt_marketing.sweepstakes_storage[0].name)

#  Works as expected - Change_Marketing_Firm_Name
jwt_marketing.change_marketing_firm_name()
print(jwt_marketing.name)

#  Works as expected - Select_Sweepstakes
jwt_marketing.select_sweepstakes()

#  Works as expected - Menu
jwt_marketing.menu()

#  endregion


#  endregion
