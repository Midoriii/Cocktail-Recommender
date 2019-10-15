"""Class which holds all information about recipe"""


class Recipe:
    def __init__(self):
        # lists because some fields can have multiple values
        self.link = ""
        self.name = ""
        self.ingredients = []
        self.garnish = []
        self.glass = []
        self.flavor = []
        self.base = []
        self.cocktailType = []
        self.served = []
        self.preparation = []
        self.strength = []
        self.difficulty = []
        self.hours = []
        self.occasions = []
        self.theme = []
        self.brands = []

    def __str__(self):
        return ("Link:         " + self.link + "\n" +
                "Name:         " + self.name + "\n" +
                "Ingredients:  " + ", ".join(self.ingredients) + "\n" +
                "Garnish:      " + ", ".join(self.garnish) + "\n" +
                "Glass:        " + ", ".join(self.glass) + "\n" +
                "Flavor:       " + ", ".join(self.flavor) + " \n" +
                "Base Spirit:  " + ", ".join(self.base) + " \n" +
                "CocktailType: " + ", ".join(self.cocktailType) + "\n" +
                "Preparation:  " + ", ".join(self.preparation) + "\n" +
                "Served:       " + ", ".join(self.served) + "\n" +
                "Strength:     " + ", ".join(self.strength) + "\n" +
                "Difficulty:   " + ", ".join(self.difficulty) + "\n" +
                "Hours:        " + ", ".join(self.hours) + "\n" +
                "Occasions:    " + ", ".join(self.occasions) + "\n" +
                "Theme:        " + ", ".join(self.theme) + "\n" +
                "Brands:       " + ", ".join(self.brands) + "\n")
