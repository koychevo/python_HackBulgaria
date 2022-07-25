def square(number):
    return number ** 2

#print(square(2))
#print(square(5))

def fact(number):
    result = 1
    for num in range(1, number + 1):
        result *= num
    return result

#print(fact(0))
#print(fact(5))
#print(fact(6))

def count_elements(items):
    count = 0
    for item in items:
        count += 1
    return count

#print(count_elements([]))
#print(count_elements([1 , 2, 3]))

def member(x, xs):
    is_found = False
    for item in xs:
        if item == x:
            is_found = True
            break
    return is_found

#print(member(1, [2, 4, 6, 1, 2]))
#print(member("Python", ["Django", "Rails"]))

def grades_that_pass(students, grades, limit):
    result = []
    for i in range(len(grades)):
        if grades[i] >= limit:
            result += [students[i]]
    return result

students = ["Rado", "Ivo", "Maria", "Nina"]
grades = [3, 4.5, 5.5, 6]

result = grades_that_pass(students, grades, 4.0)
print(result)

