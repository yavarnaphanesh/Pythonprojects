import random
logo = """ 

   ________                              ___________.__              _______               ___.                 
 /  _____/ __ __   ____   ______ ______ \__    ___/|  |__   ____    \      \  __ __  _____\_ |__   ___________ 
/   \  ___|  |  \_/ __ \ /  ___//  ___/   |    |   |  |  \_/ __ \   /   |   \|  |  \/     \| __ \_/ __ \_  __ \
\    \_\  \  |  /\  ___/ \___ \ \___ \    |    |   |   Y  \  ___/  /    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/
 \______  /____/  \___  >____  >____  >   |____|   |___|  /\___  > \____|__  /____/|__|_|  /___  /\___  >__|   
        \/            \/     \/     \/                  \/     \/          \/            \/    \/     \/       
 
 """
print(logo)
print("Welcome Number Guess Game")
print("I am thinking of a number between 1 to 100.")
print("Choose a difficulty easy or hard")
difficulty = input().lower()
# num_list = [int(x)for x in range(1,101)]
# print(num_list)
if difficulty == "easy":
    easy_attempt = 10
    computer_guess = random.randint(1, 101)
    for i in range(easy_attempt):
        j = easy_attempt-i
        user_guess = int(input("Guess the number:"))
        if user_guess > computer_guess:
            print(f"you have {j} attempts remaining to guess the number")
            print("Too High")
            print("Guess Again")

        elif user_guess < computer_guess:
            print(f"you have {j} attempts remaining to guess the number")
            print("Too Low")
            print("Guess Again")
        else:
            print("You got it ! The answer is :", user_guess)
            print("Guess Again")
            break
    game = False
elif difficulty == "hard":
    hard_attempt = 5
    computer_guess = random.randint(1, 101)
    for k in range(1, hard_attempt+1):
        l = hard_attempt-k
        print("Guess the number")
        user_guess = int(input())
        if user_guess > computer_guess:
            print(f"you have {l} attempts remaining to guess the number")
            print("Too High")
            print("Guess Again")

        elif user_guess < computer_guess:
            print(f"you have {l} attempts remaining to guess the number")
            print("Too Low")
            print("Guess Again")
        else:
            # print(f"you have {j} attempts remaining to guess the number")
            print("You got it ! The answer is :", user_guess)
            print("Guess Again")
            break

