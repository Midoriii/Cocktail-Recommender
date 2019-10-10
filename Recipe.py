"""Class which holds all information about recipe"""
class Recipe:
    def __init__(self):
        # lists because some fields can have multiple values
        self.name = ""
        self.garnish = []
        self.glass = []
        self.ingredients = []
        self.flavor = []
        self.base = []
        self.cocktailType = []
        self.served = []
        self.preparation = []
        self.strength = []
        self.difficulty = []
        self.hours = []
        self.theme = []
        self.brands = []

    def __str__(self):
        return ("name: " + self.name + "\n" +
                "garnish : " + ", ".join(self.garnish) + "\n" +
                "glass : " + ", ".join(self.glass) + "\n" +
                "ingredients : " + ", ".join(self.ingredients) + "\n" +
                "flavor: " + ", ".join(self.flavor) + " \n" +
                "base: " + ", ".join(self.base) + " \n" +
                "cocktailType : " + ", ".join(self.cocktailType) + "\n" +
                "preparation : " + ", ".join(self.preparation) + "\n" +
                "served : " + ", ".join(self.served) + "\n" +
                "strength : " + ", ".join(self.strength) + "\n" +
                "difficulty : " + ", ".join(self.difficulty) + "\n" +
                "hours : " + ", ".join(self.hours) + "\n" +
                "theme : " + ", ".join(self.theme) + "\n" +
                "brands : " + ", ".join(self.brands))


