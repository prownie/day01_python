class Recipe:

    def __init__(self, name, cook_lv, cooking_time, ing, desc, recipe_type):
        if (name == "" or isinstance(name, int)):
            exit("Name can't be a number or empty")
        self.name = name
        if (not isinstance(cook_lv, int) or
           (isinstance(cook_lv, int) and (cook_lv < 1 or cook_lv > 5))):
            exit("cooking_level needs to be a number between 1 and 5")
        self.cooking_lvl = cook_lv
        if (not isinstance(cooking_time, int) or
           (isinstance(cooking_time, int) and cooking_time < 0)):
            exit("cooking_time must be an int > 0")
        self.cooking_time = cooking_time
        if (not ing):
            exit("ingredients can't be empty")
        for i in ing:
            if (i.isnumeric()):
                exit("ingredients can't be a number")
        self.ingredients = ing
        if (isinstance(desc, int)):
            exit("description can't be a number")
        self.description = desc
        if (recipe_type not in ["starter", "lunch", "dessert"]):
            exit("Needs to chose starter, a lunch or a dessert ?")
        self.recipe_type = recipe_type

    def __str__(self):
        txt = ""
        txt += "\033[32mRecipe for\033[0m: {}\n".format(self.name)
        txt += "\033[32mDifficulty level\033[0m: {}\n".format(self.cooking_lvl)
        txt += "\033[32mTime needed\033[0m: {} min\n".format(self.cooking_time)
        if (self.description):
            txt += "\033[32mDescription\033[0m: {}\n".format(self.description)
        txt += "\033[32mIdeal for\033[0m: {}\n".format(self.recipe_type)
        txt += "\033[32mIngredients\033[0m:\n"
        for i in self.ingredients:
            txt += "\t - {}\n".format(i)
        return txt
