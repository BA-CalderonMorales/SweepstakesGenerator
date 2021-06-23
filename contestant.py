import user_interface


class Contestant:
    def __init__(self, first, last, email, registration_number):
        self.key = {
            "first_name": first,
            "last_name": last,
            "email": email,
            "id": registration_number,
            "win_or_lose": False
        }

    def notify(self, is_winner):
        if is_winner.key['win_or_lose']:
            print(f"\n\t\t{is_winner.key['first_name']} {is_winner.key['last_name']}!\n"
                  f"\tLooks like you're the winner!")
        else:
            print(f"\n\t\t{is_winner.key['first_name']} {is_winner.key['last_name']}\n"
                  f"\tIt appears you didn't win this time.\n"
                  "\t\tBetter luck next time!")
