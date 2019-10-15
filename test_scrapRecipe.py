from unittest import TestCase
import requests
import scraper
import Recipe


headers = requests.utils.default_headers()
headers.update({'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'})
bacardiPinaColada = scraper.parsePageFromLink('https://www.liquor.com/recipes/bacardi-pina-colada')
smokeBreak = scraper.parsePageFromLink('https://www.liquor.com/recipes/smoke-break')
veranoEnValencia = scraper.parsePageFromLink('https://www.liquor.com/recipes/azunia-verano-en-valencia')
hydrate = scraper.parsePageFromLink('https://www.liquor.com/recipes/hydrate')
royalBalmoralPunch = scraper.parsePageFromLink('https://www.liquor.com/recipes/royal-balmoral-punch')
getOffMyIsle = scraper.parsePageFromLink('https://www.liquor.com/recipes/mozart-get-off-my-isle')  # recipe with two glasses, and have occasions in profile


# TODO granish is not done yet
class TestScrapProfile(TestCase):
    def testBacardiPinaColada(self):
        recipe = Recipe.Recipe()
        scraper.scrapProfile(bacardiPinaColada, recipe)
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
        scraper.scrapProfile(smokeBreak, recipe)
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
        scraper.scrapProfile(veranoEnValencia, recipe)
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
        scraper.scrapProfile(hydrate, recipe)
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
        scraper.scrapProfile(royalBalmoralPunch, recipe)
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
        scraper.scrapProfile(getOffMyIsle, recipe)
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
        scraper.scrapIngredients(bacardiPinaColada, recipe)
        self.assertTrue(recipe.ingredients[0] == 'Bacardí Superior rum')
        self.assertTrue(recipe.ingredients[1] == 'Fresh coconut water')
        self.assertTrue(recipe.ingredients[2] == 'Fresh pineapple juice')
        self.assertTrue(recipe.ingredients[3] == 'Fresh pineapple')
        self.assertTrue(recipe.ingredients[4] == 'Caster sugar')

    def testSmokeBreak(self):
        recipe = Recipe.Recipe()
        scraper.scrapIngredients(smokeBreak, recipe)
        self.assertTrue(recipe.ingredients[0] == 'Cherrywood chips')
        self.assertTrue(recipe.ingredients[1] == 'W.L. Weller Special Reserve bourbon')
        self.assertTrue(recipe.ingredients[2] == 'Cream sherry')
        self.assertTrue(recipe.ingredients[3] == 'Carpano Antica Formula vermouth')
        self.assertTrue(recipe.ingredients[4] == 'Woodford Reserve spiced cherry bourbon-barrel-aged bitters ')  # space at the end, is in the name on webpage
        self.assertTrue(recipe.ingredients[5] == 'Angostura bitters')

    def testVeranoEnValencia(self):
        recipe = Recipe.Recipe()
        scraper.scrapIngredients(veranoEnValencia, recipe)
        self.assertTrue(recipe.ingredients[0] == 'Azuñia reposado organic tequila')
        self.assertTrue(recipe.ingredients[1] == 'Taylor Fladgate dry white port ')  # TODO space at the end, why is it here? - get rid of it
        self.assertTrue(recipe.ingredients[2] == 'Giffard apricot liqueur')
        self.assertTrue(recipe.ingredients[3] == 'Fresh lemon juice')
        self.assertTrue(recipe.ingredients[4] == 'Fever-Tree Mediterranean tonic water')

    def testHydrate(self):
        recipe = Recipe.Recipe()
        scraper.scrapIngredients(hydrate, recipe)
        self.assertTrue(recipe.ingredients[0] == 'Organic cucumber vodka')
        self.assertTrue(recipe.ingredients[1] == 'Puréed watermelon')
        self.assertTrue(recipe.ingredients[2] == 'Fresh lime juice')
        self.assertTrue(recipe.ingredients[3] == 'Truvia')

    def testRoyalBalmoralPunch(self):
        recipe = Recipe.Recipe()
        scraper.scrapIngredients(royalBalmoralPunch, recipe)
        self.assertTrue(recipe.ingredients[0] == 'Glenfiddich 21-year-old single-malt scotch')
        self.assertTrue(recipe.ingredients[1] == 'Tea syrup')
        self.assertTrue(recipe.ingredients[2] == 'Granny Smith apple juice')
        self.assertTrue(recipe.ingredients[3] == 'Lemonade')
        self.assertTrue(recipe.ingredients[4] == 'Champagne')
        self.assertTrue(recipe.ingredients[5] == 'Thistle')

    def getOffMyIsle(self):
        recipe = Recipe.Recipe()
        scraper.scrapIngredients(getOffMyIsle, recipe)
        self.assertTrue(recipe.ingredients[0] == 'Peanut butter-washed scotch')
        self.assertTrue(recipe.ingredients[1] == 'Mozart chocolate cream liqueur')
        self.assertTrue(recipe.ingredients[2] == 'Cookie dough liqueur')
        self.assertTrue(recipe.ingredients[3] == 'Ponche de Crema')
        self.assertTrue(recipe.ingredients[4] == 'Angostura bitters')


class TestScrapGlass(TestCase):
    def testBacardiPinaColada(self):
        recipe = Recipe.Recipe()
        scraper.scrapGlass(bacardiPinaColada, recipe)
        self.assertTrue(recipe.glass[0] == 'Hurricane')

    def testSmokeBreak(self):
        recipe = Recipe.Recipe()
        scraper.scrapGlass(smokeBreak, recipe)
        self.assertTrue(recipe.glass[0] == 'Rocks')

    def testVeranoEnValencia(self):
        recipe = Recipe.Recipe()
        scraper.scrapGlass(veranoEnValencia, recipe)
        self.assertTrue(recipe.glass[0] == 'Wine')

    def testHydrate(self):
        recipe = Recipe.Recipe()
        scraper.scrapGlass(hydrate, recipe)
        self.assertTrue(recipe.glass[0] == 'Martini')

    def testRoyalBalmoralPunch(self):
        recipe = Recipe.Recipe()
        scraper.scrapGlass(royalBalmoralPunch, recipe)
        self.assertTrue(recipe.glass[0] == 'Teacup')

    def getOffMyIsle(self):
        recipe = Recipe.Recipe()
        scraper.scrapGlass(getOffMyIsle, recipe)
        self.assertTrue(recipe.glass[0] == 'Highball')
        self.assertTrue(recipe.glass[1] == 'Collins')

