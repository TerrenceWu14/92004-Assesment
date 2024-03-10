import math

def num_rounds():
    while True:
        num_round = input("How many rounds do you want to play (press <enter> for infinite): ")
        # Returns infinite if the user pressed <enter>
        if num_round == "":
            return "infinite"
        # Returns the number of rounds the user chose
        try:
            num_round = int(num_round)
            # Returns the number of rounds the user chose if it's greater than 0
            if num_round > 0:
                return num_round
            else:
                print()
                print("Please enter a number greater than 0 or press <enter> for infinite mode")
        # Handles errors if the input is not a number
        except ValueError:
            print()
            print("Please enter a valid number or press <enter> for infinite mode")


for item in range(0, 5):
    rounds = num_rounds()
    print(rounds)
