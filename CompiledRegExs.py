import re


class CompiledRegExs:
    def __init__(self):
        self.glassRegEx = re.compile(r'/?post_type=recipe&amp;s=(.*)">(.*)</a></div>')
        self.ingredientWithoutLinkRegEx = re.compile(r'(.*)</div>')
        self.ingredientContainingLinkRegEx = re.compile(r'style="text-decoration: underline;">(.*)</a> </div>')

        self.garnish = re.compile(r'/?post_type=recipe&amp;s=(.*)"><span class="oz-value">(.*)</span><span class="ml-value"')
        self.flavor = re.compile(r'/flavor-profile/(.*)/?post_type=recipe">(.*)</a>')
        self.base = re.compile(r'/base/(.*)/?post_type=recipe">(.*)</a>')
        self.cocktailType = re.compile(r'/recipe-type/(.*)/?post_type=recipe">(.*)</a>')
        self.served = re.compile(r'/way-to-serve/(.*)/?post_type=recipe">(.*)</a>')
        self.preparation = re.compile(r'/preparation/(.*)/?post_type=recipe">(.*)</a>')
        self.strength = re.compile(r'/strength/(.*)/?post_type=recipe">(.*)</a>')
        self.difficulty = re.compile(r'/complexity/(.*)/?post_type=recipe">(.*)</a>')
        self.hours = re.compile(r'/hours/(.*)/?post_type=recipe">(.*)</a>')
        self.occasions = re.compile(r'/occasions/(.*)/?post_type=recipe">(.*)</a>')
        self.theme = re.compile(r'/theme/(.*)/?post_type=recipe">(.*)</a>')
        self.brands = re.compile(r'/?post_type=brand&amp;s=(.*)">(.*)</a>')
        
        self.dictOfCompiledProfileRegExs = {
            'garnish': self.garnish,
            'flavor': self.flavor,
            'base': self.base,
            'cocktailType': self.cocktailType,
            'served': self.served,
            'preparation': self.preparation,
            'strength': self.strength,
            'difficulty': self.difficulty,
            'hours': self.hours,
            'occasions': self.occasions,
            'theme': self.theme,
            'brands': self.brands,
        }
