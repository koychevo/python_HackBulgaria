from datetime import date

first_name = input("Enter first name: ")
second_name = input("Enter second name: ")
third_name = input("Enter third name: ")
birth_year = int(input("Enter birth year: "))

current_year = date.today().year
current_age = current_year - birth_year

person = {
    "first_name": first_name,
    "second_name": second_name,
    "third_name": third_name,
    "birth_year": birth_year,
    "current_age": current_age
}

print(person)

