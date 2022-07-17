points = int(input("Въведете точки между 0 и 100: "))

if 0 <= points <= 50:
    print("Слаб 2")
elif points <= 60:
    print("Среден 3")
elif points <= 70:
    print("Добър 4")
elif points <= 80:
    print("Много Добър 5")
elif points < 100:
    print("Отличен 6")
elif points == 100:
    print("Много Отличен 7")
else:
    print("Няма такива точки!")