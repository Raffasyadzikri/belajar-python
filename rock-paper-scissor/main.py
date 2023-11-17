from random import randint

title = "Rock-Paper-Scissor Game"
print(title)
print(f"{'=' * len(title)}")

weapon = "rock", "paper", "scissor"

Player = input("Choose your weapon(rock | paper | scissor):")
computer = weapon[randint(0, 2)]

if Player == computer:
    print("Player uses", Player)
    print("Computer uses", computer)
    print("Nobody wins!")
elif Player == "rock":
    if computer == "paper":
        print("Player uses", Player)
        print("Computer uses", computer)
        print("Computer wins!")
    elif computer == "scissor":
        print("Player uses", Player)
        print("Computer uses", computer)
        print("Player wins!")
elif Player == "paper":
    if computer == "rock":
        print("Player uses", Player)
        print("Computer uses", computer)
        print("Player wins!")
    elif computer == "scissor":
        print("Player uses", Player)
        print("Computer uses", computer)
        print("Computer wins!")
elif Player == "scissor":
    if computer == "rock":
        print("Player uses", Player)
        print("Computer uses", computer)
        print("Computer wins!")
    elif computer == "paper":
        print("Player uses", Player)
        print("Computer uses", computer)
        print("Player wins!")
else:
    print("Wrong weapon!")

    