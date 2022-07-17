from random import randint

first_player_name = "Ivan"
second_player_name = "Mariya"
first_player_score = 1001
second_player_score = 1001

while first_player_score != 0 or second_player_score != 0:
    first_player_dice = 0
    for i in range(5):
        first_player_dice += randint(1, 6)
    if first_player_score < 0:
        first_player_score += first_player_dice
    else:
        first_player_score -= first_player_dice
    print(f"{first_player_name} rolls {first_player_dice} and has {first_player_score} score.")
    if first_player_score == 0:
        print(f"The winner is {first_player_name}")
        break

    second_player_dice = 0
    for i in range(5):
        second_player_dice += randint(1, 6)
    if second_player_score < 0:
        second_player_score += second_player_dice
    else:
        second_player_score -= second_player_dice
    print(f"{second_player_name} rolls {second_player_dice} and has {second_player_score} score.")
    if second_player_score == 0:
        print(f"The winner is {second_player_name}")
        break
