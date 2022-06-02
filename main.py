import random

name = input("Input your name: ")
name = str(name)

while True:
  
    user_option = input("Enter Your Choice(R , P , S): ").upper()
    options = ["R" ,"P", "S"]
    comp_option = random.choice(options)
    if user_option == "R" or user_option == "P" or user_option == "S":
        print(f"\n {name} choose {user_option}, Computer choose {comp_option}.\n ")
    
        
        if user_option == comp_option:
            print(f" {name} and Computer both choose {user_option}, It's a tie")

        elif user_option == "R":
            if comp_option == "S":
                print(f"You win, Rock Beats Scissors")
            else:
                print(f"You loose, Paper beats Rock")

        elif user_option == "P":
            if comp_option == "R":
                print(f"You win, Paper Beats Rock")
            else:
                print(f"You loose, Scissors beats Paper")

        elif user_option == "S":

            if comp_option == "P":
                print(f"You win, Scissors Beats Paper")
            else:
                print(f"You loose, rock beats Scissors")

        play_again = input("Play again? (y/n): ")
        if play_again.lower() != "y" and play_again.lower() != "yes":
            break

    else:
        print("Invalid Input")
       