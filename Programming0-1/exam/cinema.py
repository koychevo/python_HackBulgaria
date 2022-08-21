def find_all_free_places(cinema):
    free_places = []
    for row in range(len(cinema)):
        row_free_places = []
        for col in range(len(cinema[row])):
            if cinema[row][col] == 0:
                row_free_places += [(row + 1, col + 1)]
        if len(row_free_places) > 0:
            free_places += [row_free_places]
    return free_places


def calculate_length(elem):
    return len(elem)

def sort_free_places(places):
    return sorted(places, key = calculate_length)


def order_of_seats(cinema):
    list_of_free_place = []
    free_places = find_all_free_places(cinema)
    free_places = sort_free_places(free_places)
    for places in free_places:
        list_of_free_place += places
    return list_of_free_place


cinema = [ [1, 1, 1],
           [1, 0, 0],
           [1, 0, 0],
           [1, 1, 0] ]


print(order_of_seats(cinema))