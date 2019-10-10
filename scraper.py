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
    scrapIngrediences(recipeLink, recipe)
    scrapProfile(recipeLink, recipe)
    print(recipe)



def scrapIngrediences(recipeLink, recipe):
    pass


def scrapProfile(recipeLink, recipe):
    page = parsePageFromLink(recipeLink)
    recipe.name = page.title.string  # TODO remove 'Cocktail Recipe' at the end

    for link in page.find_all('a'):
        link = str(link)
        # print(link)

        for key, regularExpreasion in listOfProfileRegularExpressions.items():
            profileRe = re.compile(regularExpreasion)
            if profileRe.search(link) is not None:
                # print(key, ':', profileRe.search(link).group(2))
                fillRecipeValues(key, profileRe.search(link).group(2), recipe)


def parsePageFromLink(link):
    pageRequest = requests.get(link, headers)
    return BeautifulSoup(pageRequest.text, 'html.parser')


def fillRecipeValues(key, text, recipe):
    if key == 'garnish':
        recipe.garnish.append(text)
    if key == 'glass':
        recipe.glass.append(text)
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
    'garnish': r'/?post_type=recipe&amp;s=(.*)"><span class="oz-value">(.*)</span><span class="ml-value"',
    'glass': r'/?post_type=recipe&amp;s=(.*)">(.*)</a>',  # TODO probably scrap from <div class=... not <a href...
    'flavor': r'/flavor-profile/(.*)/?post_type=recipe">(.*)</a>',
    'base': r'/base/(.*)/?post_type=recipe">(.*)</a>',
    'cocktailType': r'/recipe-type/(.*)/?post_type=recipe">(.*)</a>',
    'served': r'/way-to-serve/(.*)/?post_type=recipe">(.*)</a>',
    'preparation': r'/preparation/(.*)/?post_type=recipe">(.*)</a>',
    'strength': r'/strength/(.*)/?post_type=recipe">(.*)</a>',
    'difficulty': r'/complexity/(.*)/?post_type=recipe">(.*)</a>',
    'hours': r'/hours/(.*)/?post_type=recipe">(.*)</a>',
    'theme': r'/theme/(.*)/?post_type=recipe">(.*)</a>',
    'brands': r'/?post_type=brand&amp;s=(.*)">(.*)</a>',  # once brands are done end search
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
