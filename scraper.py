from bs4 import BeautifulSoup
import requests
import re

import Recipe


def getPagesWithRecipes():
    for i in range(pagesWithRecipesToLoad):
        pagesWithRecipes.append("https://www.liquor.com/recipes/page/" + str(i) + "/")


def getRecipes():
    for recipePage in pagesWithRecipes:
        page = parsePageFromLink(recipePage)

        for link in page.find_all('a'):
            link = str(link.get('href'))
            if link.find("https://www.liquor.com/recipes") != -1 and link.find("https://www.liquor.com/recipes/page") == -1:
                if link not in recipePages:
                    recipePages.append(link)


def scrapRecipe():
    recipeLink = 'https://www.liquor.com/recipes/bacardi-pina-colada'
    recipe = Recipe.Recipe()
    scrapIngredients(recipeLink, recipe)
    scrapProfile(recipeLink, recipe)
    scrapGlass(recipeLink, recipe)
    print(recipe)


def scrapIngredients(recipeLink, recipe):
    page = parsePageFromLink(recipeLink)
    ingredientClass = str(page.findAll("div", {"class": "col-xs-9 x-recipe-ingredient"}))
    print('ingredients', ingredientClass)
    ingrediants = re.compile(r'<div class="col-xs-9 x-recipe-ingredient">(.*)</div>')
    # print(ingrediants.search(ingredientClass).group(1))



def scrapProfile(recipeLink, recipe):
    page = parsePageFromLink(recipeLink)
    recipe.name = removeCocktailRecipeStringFromEndOfTitle(page.title.string)

    for link in page.find_all('a'):
        link = str(link)
        # print(link)

        for key, regularExpreasion in listOfProfileRegularExpressions.items():
            profileRe = re.compile(regularExpreasion)
            if profileRe.search(link) is not None:

                # there are cocktailTypes at the end of page that doesn't belong to recipe once we reach them recipe
                # is scrapped ad we can end
                if key == 'cocktailType' and recipe.brands != []:
                    break

                fillRecipeProfileValues(key, profileRe.search(link).group(2), recipe)


def scrapGlass(recipeLink, recipe):  # TODO is there recipe with two or more glasses?
    page = parsePageFromLink(recipeLink)
    linewWithGlass = str(page.findAll("div", {"class": "col-xs-9 recipe-link x-recipe-glasstype no-padding"}))
    glassRe = re.compile(r'/?post_type=recipe&amp;s=(.*)">(.*)</a></div>')
    recipe.glass.append(glassRe.search(linewWithGlass).group(2))

def scrapGarnish(recipeLink, recipe):
    pass


def parsePageFromLink(link):
    pageRequest = requests.get(link, headers)
    return BeautifulSoup(pageRequest.text, 'html.parser')


def removeCocktailRecipeStringFromEndOfTitle(title):
    # Title has string 'Cocktail Recipe' at the end this function removes it
    index = title.find('Cocktail Recipe')
    return title[:index]


def fillRecipeProfileValues(key, text, recipe):
    if key == 'garnish':
        recipe.garnish.append(text)
    if key == 'flavor':
        recipe.flavor.append(text)
    if key == 'base':
        recipe.base.append(text)
    if key == 'cocktailType':
        recipe.cocktailType.append(text)
    if key == 'served':
        recipe.served.append(text)
    if key == 'preparation':
        recipe.preparation.append(text)
    if key == 'strength':
        recipe.strength.append(text)
    if key == 'difficulty':
        recipe.difficulty.append(text)
    if key == 'hours':
        recipe.hours.append(text)
    if key == 'theme':
        recipe.theme.append(text)
    if key == 'brands':
        recipe.brands.append(text)


listOfProfileRegularExpressions = {
    'garnish': r'/?post_type=recipe&amp;s=(.*)"><span class="oz-value">(.*)</span><span class="ml-value"',  # TODO get rid of semicolon
    'flavor': r'/flavor-profile/(.*)/?post_type=recipe">(.*)</a>',
    'base': r'/base/(.*)/?post_type=recipe">(.*)</a>',
    'cocktailType': r'/recipe-type/(.*)/?post_type=recipe">(.*)</a>',
    'served': r'/way-to-serve/(.*)/?post_type=recipe">(.*)</a>',
    'preparation': r'/preparation/(.*)/?post_type=recipe">(.*)</a>',
    'strength': r'/strength/(.*)/?post_type=recipe">(.*)</a>',
    'difficulty': r'/complexity/(.*)/?post_type=recipe">(.*)</a>',
    'hours': r'/hours/(.*)/?post_type=recipe">(.*)</a>',
    'theme': r'/theme/(.*)/?post_type=recipe">(.*)</a>',
    'brands': r'/?post_type=brand&amp;s=(.*)">(.*)</a>',  # TODO once brands are done end search
}


headers = requests.utils.default_headers()
headers.update({'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'})
pagesWithRecipesToLoad = 48  # there is currently 48 pages

pagesWithRecipes = []
recipePages = []

# getPagesWithRecipes()
# getRecipes()

scrapRecipe()
print("\n".join(recipePages))
print(len(recipePages))
