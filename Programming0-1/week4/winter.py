def winter_is_coming(seasons):
    count = 0
    for season in seasons:
        if season == "winter":
            count = 0
        else:
            count += 1
        if count >= 5:
            return True
    return False

print(winter_is_coming(["winter", "summer", "summer", "summer", "spring", "srping"]))