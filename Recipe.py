import json

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
        self.cocktail_type = []
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
                "Flavor:       " + ", ".join(self.flavor) + "\n" +
                "BaseSpirit:   " + ", ".join(self.base) + "\n" +
                "CocktailType: " + ", ".join(self.cocktail_type) + "\n" +
                "Preparation:  " + ", ".join(self.preparation) + "\n" +
                "Served:       " + ", ".join(self.served) + "\n" +
                "Strength:     " + ", ".join(self.strength) + "\n" +
                "Difficulty:   " + ", ".join(self.difficulty) + "\n" +
                "Hours:        " + ", ".join(self.hours) + "\n" +
                "Occasions:    " + ", ".join(self.occasions) + "\n" +
                "Theme:        " + ", ".join(self.theme) + "\n" +
                "Brands:       " + ", ".join(self.brands) + "\n")
    
    def generate_csv_string(self):
        return (self.link + "," +
                self.name + "," +
                ";".join(self.ingredients) + "," +
                ";".join(self.garnish) + "," +
                ";".join(self.glass) + "," +
                ";".join(self.flavor) + "," +
                ";".join(self.base) + "," +
                ";".join(self.cocktail_type) + "," +
                ";".join(self.preparation) + "," +
                ";".join(self.served) + "," +
                ";".join(self.strength) + "," +
                ";".join(self.difficulty) + "," +
                ";".join(self.hours) + "," +
                ";".join(self.occasions) + "," +
                ";".join(self.theme) + "," +
                ";".join(self.brands) + "\n")

    def generate_json_string(self):
        return ('{\n\t"name": "' + self.name + '",\n' +
                '\t"link": "' + self.link + '",\n' +
                '\t"ingredients": [\n\t\t"' + '",\n\t\t"'.join(self.ingredients) + '"\n\t],\n' +
                '\t"garnish": ["' + '", "'.join(self.garnish) + '"],\n' +
                '\t"glass": ["' + '", "'.join(self.glass) + '"],\n' +
                '\t"profile": {\n' +
                '\t\t"flavor": ["' + '", "'.join(self.flavor) + '"],\n' +
                '\t\t"base_spirit": ["' + '", "'.join(self.base) + '"],\n' +
                '\t\t"cocktail_type": ["' + '", "'.join(self.cocktail_type) + '"],\n' +
                '\t\t"preparation": ["' + '", "'.join(self.preparation) + '"],\n' +
                '\t\t"served": ["' + '", "'.join(self.served) + '"],\n' +
                '\t\t"strength": ["' + '", "'.join(self.strength) + '"],\n' +
                '\t\t"difficulty": ["' + '", "'.join(self.difficulty) + '"],\n' +
                '\t\t"hours": ["' + '", "'.join(self.hours) + '"],\n' +
                '\t\t"occasions": ["' + '", "'.join(self.occasions) + '"],\n' +
                '\t\t"theme": ["' + '", "'.join(self.theme) + '"],\n' +
                '\t\t"brands": ["' + '", "'.join(self.brands) + '"],\n' +
                '\t}\n}'
                )

    ''' Removes trailing spaces and occasional '*' from ingredients and garnish'''
    def clean_recipe_attributes(self):
        for item in range(len(self.garnish)):
            self.garnish[item] = self.garnish[item].strip().replace('*', '')
        for item in range(len(self.ingredients)):
            self.ingredients[item] = self.ingredients[item].strip().replace('*', '')
