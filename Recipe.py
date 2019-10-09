"""Class which holds all information about recipe"""
class Recipe:
    def __init__(self):
        # lists because some fields can have multiple values
        self.name = "placeholder name"
        self.garnish = []
        self.glass = []
        self.ingredients = []
        self.flavor = []
        self.baseSpirit = []
        self.cocktailType = []
        self.served = []
        self.preparation = []
        self.strength = []
        self.difficulty = []
        self.hours = []
        self.brands = []

    def __str__(self):
        return ("name: " + self.name + "\n" +
                "garnish : " + ", ".join(self.garnish) + "\n" +
                "ingredients : " + ", ".join(self.ingredients) + "\n" +
                "baseSpirit : " + ", ".join(self.baseSpirit) + " \n" +
                "cocktailType : " + ", ".join(self.cocktailType) + "\n" +
                "preparation : " + ", ".join(self.preparation) + "\n" +
                "strength : " + ", ".join(self.strength) + "\n" +
                "difficulty : " + ", ".join(self.difficulty) + "\n" +
                "hours : " + ", ".join(self.hours) + "\n" +
                "brands : " + ", ".join(self.brands))


