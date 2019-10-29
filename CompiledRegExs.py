import re


class CompiledRegExs:
    def __init__(self):
        self.glass_reg_ex = re.compile(r'/?post_type=recipe&amp;s=(.*)">(.*)</a></div>')
        self.ingredient_without_link_reg_ex = re.compile(r'(.*)</div>')
        self.ingredient_containing_link_reg_ex = re.compile(r'style="text-decoration: underline;">(.*)</a> </div>')

        self.garnish = re.compile(r'/?post_type=recipe&amp;s=(.*)"><span class="oz-value">(.*)</span><span class="ml-value"')
        self.flavor = re.compile(r'/flavor-profile/(.*)/?post_type=recipe">(.*)</a>')
        self.base = re.compile(r'/base/(.*)/?post_type=recipe">(.*)</a>')
        self.cocktail_type = re.compile(r'/recipe-type/(.*)/?post_type=recipe">(.*)</a>')
        self.served = re.compile(r'/way-to-serve/(.*)/?post_type=recipe">(.*)</a>')
        self.preparation = re.compile(r'/preparation/(.*)/?post_type=recipe">(.*)</a>')
        self.strength = re.compile(r'/strength/(.*)/?post_type=recipe">(.*)</a>')
        self.difficulty = re.compile(r'/complexity/(.*)/?post_type=recipe">(.*)</a>')
        self.hours = re.compile(r'/hours/(.*)/?post_type=recipe">(.*)</a>')
        self.occasion = re.compile(r'/occasion/(.*)/?post_type=recipe">(.*)</a>')
        self.theme = re.compile(r'/theme/(.*)/?post_type=recipe">(.*)</a>')
        self.brands = re.compile(r'/?post_type=brand&amp;s=(.*)">(.*)</a>')
        
        self.dict_of_compiled_profile_reg_exs = {
            'garnish': self.garnish,
            'flavor': self.flavor,
            'base': self.base,
            'cocktail_type': self.cocktail_type,
            'served': self.served,
            'preparation': self.preparation,
            'strength': self.strength,
            'difficulty': self.difficulty,
            'hours': self.hours,
            'occasion': self.occasion,
            'theme': self.theme,
            'brands': self.brands,
        }
