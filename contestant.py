import user_interface


class Contestant:
    "This class was made to better manipulate the information that is allowed \
    whenever a person registers into a sweepstake."
    def __init__(self, first, last, email, registration_number):
        "The constructor that holds a person's first name, last name, email, \
        registration number, and also whether they are a winning or losing \
        contestant."
        self.key = {
            "first_name": first,
            "last_name": last,
            "email": email,
            "id": registration_number,
            "win_or_lose": False
        }

    def notify(self, is_winner):
        "This method will notify all contestants whether they won or lost the \
        current sweepstake."
        if is_winner.key['win_or_lose']:
            print(f"\n\t\t{is_winner.key['first_name']} {is_winner.key['last_name']}!\n"
                  f"\tLooks like you're the winner!")
        else:
            print(f"\n\t\t{is_winner.key['first_name']} {is_winner.key['last_name']}\n"
                  f"\tIt appears you didn't win this time.\n"
                  "\t\tBetter luck next time!")
