from unittest import TestCase
from bs4 import BeautifulSoup
import requests
import scraper
import Recipe


headers = requests.utils.default_headers()
headers.update({'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'})
bacardiPinaColadaLink = 'https://www.liquor.com/recipes/bacardi-pina-colada'
smokeBreakLink = 'https://www.liquor.com/recipes/smoke-break'
veranoEnValenciaLink = 'https://www.liquor.com/recipes/azunia-verano-en-valencia'
hydrateLink = 'https://www.liquor.com/recipes/hydrate'
royalBalmoralPunchLink = 'https://www.liquor.com/recipes/royal-balmoral-punch/'

# class TestScrapRecipe(TestCase):
#     def test_scrapRecipe(self):
#         self.fail()

# TODO granish is not done yet
class TestScrapProfile(TestCase):
    def testBacardiPinaColada(self):
        recipe = Recipe.Recipe()
        scraper.scrapProfile(bacardiPinaColadaLink, recipe)
        #self.assertTrue(recipe.garnish[0] == '')
        self.assertTrue(recipe.flavor[0] == 'Fruity/Citrus-forward')
        self.assertTrue(recipe.base[0] == 'Rum')
        self.assertTrue(recipe.cocktailType[0] == 'Classics')
        self.assertTrue(recipe.cocktailType[1] == 'Tiki / Tropical')
        self.assertTrue(recipe.served[0] == 'Neat/Up')
        self.assertTrue(recipe.preparation[0] == 'Shaken')
        self.assertTrue(recipe.strength[0] == 'Medium')
        self.assertTrue(recipe.difficulty[0] == 'Medium')
        self.assertTrue(recipe.hours[0] == 'Afternoon')
        self.assertTrue(recipe.theme[0] == 'Summer')
        self.assertTrue(recipe.brands[0] == 'Bacardi')

    def testSmokeBreak(self):
        recipe = Recipe.Recipe()
        scraper.scrapProfile(smokeBreakLink, recipe)
        #self.assertTrue(recipe.garnish[0] == '')
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
        self.assertTrue(recipe.theme == [])
        self.assertTrue(recipe.brands[0] == 'Angostura')
        self.assertTrue(recipe.brands[1] == 'carpano')
        self.assertTrue(recipe.brands[2] == 'W.L. Weller')
        self.assertTrue(recipe.brands[3] == 'Woodford')

    def testVeranoEnValencia(self):
        recipe = Recipe.Recipe()
        scraper.scrapProfile(veranoEnValenciaLink, recipe)
        # self.assertTrue(recipe.garnish[0] == '')
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
        self.assertTrue(recipe.theme[0] == 'Summer')
        self.assertTrue(recipe.brands[0] == 'Azunia')
        self.assertTrue(recipe.brands[1] == 'Giffard')
        self.assertTrue(recipe.brands[2] == 'Taylor Fladgate')

    def testHydrate(self):
        recipe = Recipe.Recipe()
        scraper.scrapProfile(hydrateLink, recipe)
        # self.assertTrue(recipe.garnish[0] == '')
        self.assertTrue(recipe.flavor[0] == 'Fruity/Citrus-forward')
        self.assertTrue(recipe.base[0] == 'Vodka')
        self.assertTrue(recipe.cocktailType[0] == 'Modern Classics')
        self.assertTrue(recipe.served[0] == 'Neat/Up')
        self.assertTrue(recipe.preparation[0] == 'Shaken')
        self.assertTrue(recipe.strength[0] == 'Medium')
        self.assertTrue(recipe.difficulty[0] == 'Medium')
        self.assertTrue(recipe.hours[0] == 'Afternoon')
        self.assertTrue(recipe.hours[1] == 'Morning/Brunch')
        self.assertTrue(recipe.theme[0] == 'Summer')
        self.assertTrue(recipe.brands == [])

    def testRoyalBalmoralPunch(self):
        recipe = Recipe.Recipe()
        scraper.scrapProfile(royalBalmoralPunchLink, recipe)
        #self.assertTrue(recipe.garnish[0] == '')
        self.assertTrue(recipe.flavor[0] == 'Sour')
        self.assertTrue(recipe.flavor[1] == 'Sweet')
        self.assertTrue(recipe.base[0] == 'Scotch')
        self.assertTrue(recipe.cocktailType[0] == 'Punches')
        self.assertTrue(recipe.served[0] == 'On the Rocks')
        self.assertTrue(recipe.preparation == [])
        self.assertTrue(recipe.strength[0] == 'Medium')
        self.assertTrue(recipe.difficulty[0] == 'Medium')
        self.assertTrue(recipe.hours[0] == 'Evening')
        self.assertTrue(recipe.theme[0] == 'Fall')
        self.assertTrue(recipe.brands[0] == 'Glenfiddich')

class TestScrapIngredients(TestCase):
    def testBacardiPinaColada(self):
        recipe = Recipe.Recipe()
        scraper.scrapIngredients(bacardiPinaColadaLink, recipe)
        self.assertTrue(recipe.ingredients[0] == 'Bacardí Superior rum')
        self.assertTrue(recipe.ingredients[1] == 'Fresh coconut water')
        self.assertTrue(recipe.ingredients[2] == 'Fresh pineapple juice')
        self.assertTrue(recipe.ingredients[3] == 'Fresh pineapple')
        self.assertTrue(recipe.ingredients[4] == 'Caster sugar')

    def testSmokeBreak(self):
        recipe = Recipe.Recipe()
        scraper.scrapIngredients(smokeBreakLink, recipe)
        print(recipe.ingredients)
        self.assertTrue(recipe.ingredients[0] == 'Cherrywood chips')
        self.assertTrue(recipe.ingredients[1] == 'W.L. Weller Special Reserve bourbon')
        self.assertTrue(recipe.ingredients[2] == 'Cream sherry')
        self.assertTrue(recipe.ingredients[3] == 'Carpano Antica Formula vermouth')
        self.assertTrue(recipe.ingredients[4] == 'Woodford Reserve spiced cherry bourbon-barrel-aged bitters ')  # TODO space at the end, why is it here? - get rid of it
        self.assertTrue(recipe.ingredients[5] == 'Angostura bitters')  # TODO why is it missing?

    def testVeranoEnValencia(self):
        recipe = Recipe.Recipe()
        scraper.scrapIngredients(veranoEnValenciaLink, recipe)
        self.assertTrue(recipe.ingredients[0] == 'Azuñia reposado organic tequila')
        self.assertTrue(recipe.ingredients[1] == 'Taylor Fladgate dry white port ')  # TODO space at the end, why is it here? - get rid of it
        self.assertTrue(recipe.ingredients[2] == 'Giffard apricot liqueur')
        self.assertTrue(recipe.ingredients[3] == 'Fresh lemon juice')
        self.assertTrue(recipe.ingredients[4] == 'Fever-Tree Mediterranean tonic water')

    def testHydrate(self):
        recipe = Recipe.Recipe()
        scraper.scrapIngredients(hydrateLink, recipe)
        print(recipe.ingredients)
        self.assertTrue(recipe.ingredients[0] == 'Organic cucumber vodka')
        self.assertTrue(recipe.ingredients[1] == 'Puréed watermelon')
        self.assertTrue(recipe.ingredients[2] == 'Fresh lime juice')
        self.assertTrue(recipe.ingredients[3] == 'Truvia')  # TODO why is it missing?

    def testRoyalBalmoralPunch(self):
        recipe = Recipe.Recipe()
        scraper.scrapIngredients(royalBalmoralPunchLink, recipe)
        self.assertTrue(recipe.ingredients[0] == 'Glenfiddich 21-year-old single-malt scotch')
        self.assertTrue(recipe.ingredients[1] == 'Tea syrup')
        self.assertTrue(recipe.ingredients[2] == 'Granny Smith apple juice')
        self.assertTrue(recipe.ingredients[3] == 'Lemonade')
        self.assertTrue(recipe.ingredients[4] == 'Champagne')
        self.assertTrue(recipe.ingredients[5] == 'Thistle')


class TestScrapGlass(TestCase):
    def testBacardiPinaColada(self):
        recipe = Recipe.Recipe()
        scraper.scrapGlass(bacardiPinaColadaLink, recipe)
        self.assertTrue(recipe.glass[0] == 'Hurricane')

    def testSmokeBreak(self):
        recipe = Recipe.Recipe()
        scraper.scrapGlass(smokeBreakLink, recipe)
        self.assertTrue(recipe.glass[0] == 'Rocks')

    def testVeranoEnValencia(self):
        recipe = Recipe.Recipe()
        scraper.scrapGlass(veranoEnValenciaLink, recipe)
        self.assertTrue(recipe.glass[0] == 'Wine')

    def testHydrate(self):
        recipe = Recipe.Recipe()
        scraper.scrapGlass(hydrateLink, recipe)
        self.assertTrue(recipe.glass[0] == 'Martini')

    def testRoyalBalmoralPunch(self):
        recipe = Recipe.Recipe()
        scraper.scrapGlass(royalBalmoralPunchLink, recipe)
        self.assertTrue(recipe.glass[0] == 'Teacup')




