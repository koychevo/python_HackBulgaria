def get_people_count(activity):
    visitors = {}
    for person in activity:
        if person not in visitors:
            visitors[person] = 1
    return len(visitors)

print(get_people_count(["Rado", "Ivo", "Maria", "Anneta", "Rado", "Rado", "Anneta", "Ivo", "Maria", "Rado"]))