from random import randint

n = int(input("Enter dice side: "))
first_player_name = input("Enter player1 name: ")
second_player_name = input("Enter player2 name: ")

first_player_dice = randint(1, n)
second_player_dice = randint(1, n)

print(f"{first_player_name} rolls {first_player_dice}")
print(f"{second_player_name} rolls {second_player_dice}")

if first_player_dice > second_player_dice:
    print(f"{first_player_name} wins!")
elif first_player_dice < second_player_dice:
    print(f"{second_player_name} wins!")
else:
    print("Draw!")