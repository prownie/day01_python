from datetime import date
from recipe import Recipe


class Book:

    def __init__(self, name):
        if (name == "" or isinstance(name, int)):
            exit("Name can't be a number or empty")
        self.name = name
        self.recipes_list = {'starter': {},
                             'lunch': {},
                             'dessert': {}}
        today = date.today()
        self.creation_date = today
        self.last_update = today

    def get_recipes_by_types(self, recipe_type):
        if recipe_type not in self.recipes_list:
            print("Wrong recipe name, chose between starter lunch and dessert")
            return()
        print("List of the " + recipe_type + " recipes:\n")
        for i in self.recipes_list[recipe_type]:
            print("- " + i)

    def get_recipe_by_name(self, name):
        for recipe_type in self.recipes_list:
            for recipe in self.recipes_list[recipe_type]:
                if (name == recipe.name):
                    print("Recipe : " + name + " found !")
                    return(self.recipes_list[recipe_type][name])
        print("Recipe : " + name + " not found")

    def add_recipe(self, recipe):
        if not isinstance(recipe, Recipe):
            print("Not a recipe")
            return()
        self.recipes_list[recipe.recipe_type][recipe.name] = recipe
        self.last_update = date.today()
