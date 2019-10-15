from unittest import TestCase
import scraper
import Recipe

bacardi_pina_colada = scraper.parse_page_from_link('https://www.liquor.com/recipes/bacardi-pina-colada')
smoke_break = scraper.parse_page_from_link('https://www.liquor.com/recipes/smoke-break')
verano_en_valencia = scraper.parse_page_from_link('https://www.liquor.com/recipes/azunia-verano-en-valencia')
hydrate = scraper.parse_page_from_link('https://www.liquor.com/recipes/hydrate')
royal_balmoral_punch = scraper.parse_page_from_link('https://www.liquor.com/recipes/royal-balmoral-punch')
get_off_my_isle = scraper.parse_page_from_link('https://www.liquor.com/recipes/mozart-get-off-my-isle')  # recipe with two glasses, and have occasions in profile
kiwi_bird = scraper.parse_page_from_link('https://www.liquor.com/recipes/kiwi-birdmoral-punch')  # trailing **
bourbon_toscano = scraper.parse_page_from_link('https://www.liquor.com/recipes/bourbon-toscano')  # * is the first character
haileys_comet = scraper.parse_page_from_link('https://www.liquor.com/recipes/haileys-comet/')  # garnish with *

# TODO add tests for recipes with missing brands which cannot trigger end of scrapping
class TestScrapProfile(TestCase):
    def testBacardiPinaColada(self):
        recipe = Recipe.Recipe()
        scraper.scrap_profile(bacardi_pina_colada, recipe)
        self.assertTrue(recipe.garnish[0] == 'Pineapple slice')
        self.assertTrue(recipe.garnish[1] == 'Pineapple leaf')
        self.assertTrue(recipe.flavor[0] == 'Fruity/Citrus-forward')
        self.assertTrue(recipe.base[0] == 'Rum')
        self.assertTrue(recipe.cocktailType[0] == 'Classics')
        self.assertTrue(recipe.cocktailType[1] == 'Tiki / Tropical')
        self.assertTrue(recipe.served[0] == 'Neat/Up')
        self.assertTrue(recipe.preparation[0] == 'Shaken')
        self.assertTrue(recipe.strength[0] == 'Medium')
        self.assertTrue(recipe.difficulty[0] == 'Medium')
        self.assertTrue(recipe.hours[0] == 'Afternoon')
        self.assertTrue(recipe.occasions == [])
        self.assertTrue(recipe.theme[0] == 'Summer')
        self.assertTrue(recipe.brands[0] == 'Bacardi')

    def testSmokeBreak(self):
        recipe = Recipe.Recipe()
        scraper.scrap_profile(smoke_break, recipe)
        self.assertTrue(recipe.garnish[0] == 'Dark chocolate')
        self.assertTrue(recipe.garnish[1] == 'Dried black cherries')
        self.assertTrue(recipe.flavor[0] == 'Smoky')
        self.assertTrue(recipe.flavor[1] == 'Spirit-forward')
        self.assertTrue(recipe.base[0] == 'Bourbon / American Whiskey')
        self.assertTrue(recipe.base[1] == 'Whiskey')
        self.assertTrue(recipe.cocktailType[0] == 'Modern Classics')
        self.assertTrue(recipe.served[0] == 'Large Ice Cube')
        self.assertTrue(recipe.preparation[0] == 'Stirred')
        self.assertTrue(recipe.strength[0] == 'Strong')
        self.assertTrue(recipe.difficulty[0] == 'Medium')
        self.assertTrue(recipe.hours[0] == 'Evening')
        self.assertTrue(recipe.occasions == [])
        self.assertTrue(recipe.theme == [])
        self.assertTrue(recipe.brands[0] == 'Angostura')
        self.assertTrue(recipe.brands[1] == 'carpano')
        self.assertTrue(recipe.brands[2] == 'W.L. Weller')
        self.assertTrue(recipe.brands[3] == 'Woodford')

    def testVeranoEnValencia(self):
        recipe = Recipe.Recipe()
        scraper.scrap_profile(verano_en_valencia, recipe)
        self.assertTrue(recipe.garnish[0] == 'Thyme sprigs')
        self.assertTrue(recipe.garnish[1] == 'Dehydrated lemon wheel')
        self.assertTrue(recipe.flavor[0] == 'Fruity/Citrus-forward')
        self.assertTrue(recipe.flavor[1] == 'Sweet')
        self.assertTrue(recipe.base[0] == 'Tequila')
        self.assertTrue(recipe.cocktailType[0] == 'Modern Classics')
        self.assertTrue(recipe.served[0] == 'On the Rocks')
        self.assertTrue(recipe.preparation[0] == 'Built in Glass')
        self.assertTrue(recipe.strength[0] == 'Medium')
        self.assertTrue(recipe.difficulty[0] == 'Simple')
        self.assertTrue(recipe.hours[0] == 'Afternoon')
        self.assertTrue(recipe.hours[1] == 'Evening')
        self.assertTrue(recipe.occasions == [])
        self.assertTrue(recipe.theme[0] == 'Summer')
        self.assertTrue(recipe.brands[0] == 'Azunia')
        self.assertTrue(recipe.brands[1] == 'Giffard')
        self.assertTrue(recipe.brands[2] == 'Taylor Fladgate')

    def testHydrate(self):
        recipe = Recipe.Recipe()
        scraper.scrap_profile(hydrate, recipe)
        self.assertTrue(recipe.garnish[0] == 'Cucumber slice')
        self.assertTrue(recipe.garnish[1] == 'Mint sprig')
        self.assertTrue(recipe.flavor[0] == 'Fruity/Citrus-forward')
        self.assertTrue(recipe.base[0] == 'Vodka')
        self.assertTrue(recipe.cocktailType[0] == 'Modern Classics')
        self.assertTrue(recipe.served[0] == 'Neat/Up')
        self.assertTrue(recipe.preparation[0] == 'Shaken')
        self.assertTrue(recipe.strength[0] == 'Medium')
        self.assertTrue(recipe.difficulty[0] == 'Medium')
        self.assertTrue(recipe.hours[0] == 'Afternoon')
        self.assertTrue(recipe.occasions == [])
        self.assertTrue(recipe.hours[1] == 'Morning/Brunch')
        self.assertTrue(recipe.theme[0] == 'Summer')
        self.assertTrue(recipe.brands == [])

    def testRoyalBalmoralPunch(self):
        recipe = Recipe.Recipe()
        scraper.scrap_profile(royal_balmoral_punch, recipe)
        self.assertTrue(recipe.garnish[0] == 'Lemon wheel')
        self.assertTrue(recipe.flavor[0] == 'Sour')
        self.assertTrue(recipe.flavor[1] == 'Sweet')
        self.assertTrue(recipe.base[0] == 'Scotch')
        self.assertTrue(recipe.cocktailType[0] == 'Punches')
        self.assertTrue(recipe.served[0] == 'On the Rocks')
        self.assertTrue(recipe.preparation == [])
        self.assertTrue(recipe.strength[0] == 'Medium')
        self.assertTrue(recipe.difficulty[0] == 'Medium')
        self.assertTrue(recipe.hours[0] == 'Evening')
        self.assertTrue(recipe.occasions == [])
        self.assertTrue(recipe.theme[0] == 'Fall')
        self.assertTrue(recipe.brands[0] == 'Glenfiddich')

    def getOffMyIsle(self):
        recipe = Recipe.Recipe()
        scraper.scrap_profile(get_off_my_isle, recipe)
        self.assertTrue(recipe.garnish[0] == 'Dark chocolate shaving')
        self.assertTrue(recipe.flavor[0] == 'Sweet')
        self.assertTrue(recipe.base[0] == 'Scotch')
        self.assertTrue(recipe.cocktailType[0] == 'Modern Classics')
        self.assertTrue(recipe.served[0] == 'On the Rocks')
        self.assertTrue(recipe.preparation == 'Shaken')
        self.assertTrue(recipe.strength[0] == 'Medium')
        self.assertTrue(recipe.difficulty[0] == 'Complicated')
        self.assertTrue(recipe.hours[0] == 'Evening')
        self.assertTrue(recipe.occasions[0] == 'Valentine’s Day')
        self.assertTrue(recipe.theme[0] == 'Romantic')
        self.assertTrue(recipe.brands[0] == 'Mozart')

class TestScrapIngredients(TestCase):
    def testBacardiPinaColada(self):
        recipe = Recipe.Recipe()
        scraper.scrap_ingredients(bacardi_pina_colada, recipe)
        self.assertTrue(recipe.ingredients[0] == 'Bacardí Superior rum')
        self.assertTrue(recipe.ingredients[1] == 'Fresh coconut water')
        self.assertTrue(recipe.ingredients[2] == 'Fresh pineapple juice')
        self.assertTrue(recipe.ingredients[3] == 'Fresh pineapple')
        self.assertTrue(recipe.ingredients[4] == 'Caster sugar')

    def testSmokeBreak(self):
        recipe = Recipe.Recipe()
        scraper.scrap_ingredients(smoke_break, recipe)
        self.assertTrue(recipe.ingredients[0] == 'Cherrywood chips')
        self.assertTrue(recipe.ingredients[1] == 'W.L. Weller Special Reserve bourbon')
        self.assertTrue(recipe.ingredients[2] == 'Cream sherry')
        self.assertTrue(recipe.ingredients[3] == 'Carpano Antica Formula vermouth')
        self.assertTrue(recipe.ingredients[4] == 'Woodford Reserve spiced cherry bourbon-barrel-aged bitters')
        self.assertTrue(recipe.ingredients[5] == 'Angostura bitters')

    def testVeranoEnValencia(self):
        recipe = Recipe.Recipe()
        scraper.scrap_ingredients(verano_en_valencia, recipe)
        self.assertTrue(recipe.ingredients[0] == 'Azuñia reposado organic tequila')
        self.assertTrue(recipe.ingredients[1] == 'Taylor Fladgate dry white port')
        self.assertTrue(recipe.ingredients[2] == 'Giffard apricot liqueur')
        self.assertTrue(recipe.ingredients[3] == 'Fresh lemon juice')
        self.assertTrue(recipe.ingredients[4] == 'Fever-Tree Mediterranean tonic water')

    def testHydrate(self):
        recipe = Recipe.Recipe()
        scraper.scrap_ingredients(hydrate, recipe)
        self.assertTrue(recipe.ingredients[0] == 'Organic cucumber vodka')
        self.assertTrue(recipe.ingredients[1] == 'Puréed watermelon')
        self.assertTrue(recipe.ingredients[2] == 'Fresh lime juice')
        self.assertTrue(recipe.ingredients[3] == 'Truvia')

    def testRoyalBalmoralPunch(self):
        recipe = Recipe.Recipe()
        scraper.scrap_ingredients(royal_balmoral_punch, recipe)
        self.assertTrue(recipe.ingredients[0] == 'Glenfiddich 21-year-old single-malt scotch')
        self.assertTrue(recipe.ingredients[1] == 'Tea syrup')
        self.assertTrue(recipe.ingredients[2] == 'Granny Smith apple juice')
        self.assertTrue(recipe.ingredients[3] == 'Lemonade')
        self.assertTrue(recipe.ingredients[4] == 'Champagne')
        self.assertTrue(recipe.ingredients[5] == 'Thistle')

    def getOffMyIsle(self):
        recipe = Recipe.Recipe()
        scraper.scrap_ingredients(get_off_my_isle, recipe)
        self.assertTrue(recipe.ingredients[0] == 'Peanut butter-washed scotch')
        self.assertTrue(recipe.ingredients[1] == 'Mozart chocolate cream liqueur')
        self.assertTrue(recipe.ingredients[2] == 'Cookie dough liqueur')
        self.assertTrue(recipe.ingredients[3] == 'Ponche de Crema')
        self.assertTrue(recipe.ingredients[4] == 'Angostura bitters')


class TestScrapGlass(TestCase):
    def testBacardiPinaColada(self):
        recipe = Recipe.Recipe()
        scraper.scrap_glass(bacardi_pina_colada, recipe)
        self.assertTrue(recipe.glass[0] == 'Hurricane')

    def testSmokeBreak(self):
        recipe = Recipe.Recipe()
        scraper.scrap_glass(smoke_break, recipe)
        self.assertTrue(recipe.glass[0] == 'Rocks')

    def testVeranoEnValencia(self):
        recipe = Recipe.Recipe()
        scraper.scrap_glass(verano_en_valencia, recipe)
        self.assertTrue(recipe.glass[0] == 'Wine')

    def testHydrate(self):
        recipe = Recipe.Recipe()
        scraper.scrap_glass(hydrate, recipe)
        self.assertTrue(recipe.glass[0] == 'Martini')

    def testRoyalBalmoralPunch(self):
        recipe = Recipe.Recipe()
        scraper.scrap_glass(royal_balmoral_punch, recipe)
        self.assertTrue(recipe.glass[0] == 'Teacup')

    def getOffMyIsle(self):
        recipe = Recipe.Recipe()
        scraper.scrap_glass(get_off_my_isle, recipe)
        self.assertTrue(recipe.glass[0] == 'Highball')
        self.assertTrue(recipe.glass[1] == 'Collins')


class TestStarCharNotPresent(TestCase):
    def kiwiBird(self):
        recipe = Recipe.Recipe()
        scraper.scrap_ingredients(kiwi_bird, recipe)
        self.assertTrue(recipe.ingredients[2] == 'Coconut cream')
        self.assertTrue(recipe.ingredients[3] == 'Kiwi syrup')

    def bourbonToscano(self):
        recipe = Recipe.Recipe()
        scraper.scrap_ingredients(bourbon_toscano, recipe)
        self.assertTrue(recipe.ingredients[3] == 'Smoked ice cubes')

    def haileysComet(self):
        recipe = Recipe.Recipe()
        scraper.scrap_ingredients(haileys_comet, recipe)
        self.assertTrue(recipe.garnish[0] == 'Orgeat-chantilly cream')
