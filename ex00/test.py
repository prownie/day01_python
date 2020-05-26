from book import Book
from recipe import Recipe


class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


first_book = Book("firstone")
print(first_book.name)
print(first_book.last_update)
print(first_book.creation_date)
print(first_book.recipes_list)

test = Recipe("tourte", 3, 90, ['pain', 'fromage'], "nom nom", "starter")
print(test)


print("----------------------------------------------------")
first_book.get_recipes_by_types("starter")

first_book.add_recipe(test)
first_book.get_recipes_by_types("starter")

print("----------------------------------------------------")
testreturn = first_book.get_recipe_by_name("tourte")


print(type(testreturn))
print(testreturn)

first_book.get_recipes_by_types("lunch")
first_book.get_recipes_by_types("starter")
