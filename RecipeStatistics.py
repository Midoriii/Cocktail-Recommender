class RecipeStatistics:
    def __init__(self):
        self.ingredients = 0
        self.garnish = 0
        self.glass = 0
        self.flavor = 0
        self.base = 0
        self.cocktail_type = 0
        self.served = 0
        self.preparation = 0
        self.strength = 0
        self.difficulty = 0
        self.hours = 0
        self.occasion = 0
        self.theme = 0
        self.brands = 0
        
    def max_number_of_items(self, recipe):
        self.ingredients = max(self.ingredients, len(recipe.ingredients))
        self.garnish = max(self.garnish, len(recipe.garnish))
        self.glass = max(self.glass, len(recipe.glass))
        self.flavor = max(self.flavor, len(recipe.flavor))
        self.base = max(self.base, len(recipe.base))
        self.cocktail_type = max(self.cocktail_type, len(recipe.cocktail_type))
        self.served = max(self.served, len(recipe.served))
        self.preparation = max(self.preparation, len(recipe.preparation))
        self.strength = max(self.strength, len(recipe.strength))
        self.difficulty = max(self.difficulty, len(recipe.difficulty))
        self.hours = max(self.hours, len(recipe.hours))
        self.occasion = max(self.occasion, len(recipe.occasion))
        self.theme = max(self.theme, len(recipe.theme))
        self.brands = max(self.brands, len(recipe.brands))
        
    def result_max_number_of_items(self):
        return ("Ingredients:  " + str(self.ingredients) + "\n" +
                "Garnish:      " + str(self.garnish) + "\n" +
                "Glass:        " + str(self.glass) + "\n" +
                "Flavor:       " + str(self.flavor) + "\n" +
                "BaseSpirit:   " + str(self.base) + "\n" +
                "CocktailType: " + str(self.cocktail_type) + "\n" +
                "Preparation:  " + str(self.preparation) + "\n" +
                "Served:       " + str(self.served) + "\n" +
                "Strength:     " + str(self.strength) + "\n" +
                "Difficulty:   " + str(self.difficulty) + "\n" +
                "Hours:        " + str(self.hours) + "\n" +
                "Occasion:     " + str(self.occasion) + "\n" +
                "Theme:        " + str(self.theme) + "\n" +
                "Brands:       " + str(self.brands) + "\n")
