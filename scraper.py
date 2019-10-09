from bs4 import BeautifulSoup
import requests
import re


def getPagesWithRecipes():
    for i in range(pagesWithRecipesToLoad):
        pagesWithRecipes.append("https://www.liquor.com/recipes/page/" + str(i) + "/")


def getRecipes():
    for pageWithRecipes in pagesWithRecipes:
        pageRequest = requests.get(pageWithRecipes, headers)
        page = BeautifulSoup(pageRequest.text, 'html.parser')

        for link in page.find_all('a'):
            link = str(link.get('href'))
            if link.find("https://www.liquor.com/recipes") != -1 and link.find("https://www.liquor.com/recipes/page") == -1:
                if link not in recipePages:
                    recipePages.append(link)


def scrapRecipe():
    recipeLink = 'https://www.liquor.com/recipes/bacardi-pina-colada'
    getIngrediences(recipeLink)
    getProfile(recipeLink)


def getIngrediences(recipeLink):
    pass


def getProfile(recipeLink):
    pageRequest = requests.get(recipeLink, headers)
    page = BeautifulSoup(pageRequest.text, 'html.parser')
    for link in page.find_all('a'):
        link = str(link)
        # print(link)

        for key, regularExpreasion in listOfRegularExpressions.items():
            profileRe = re.compile(regularExpreasion)
            if profileRe.search(link) is not None:
                print(key, ':', profileRe.search(link).group(2))


listOfRegularExpressions = {
    'flavor-profile': r'/flavor-profile/(.*)/?post_type=recipe">(.*)</a>',
    'base': r'/base/(.*)/?post_type=recipe">(.*)</a>',
    'recipe-type': r'/recipe-type/(.*)/?post_type=recipe">(.*)</a>',
    'way-to-serve': r'/way-to-serve/(.*)/?post_type=recipe">(.*)</a>',
    'preparation': r'/preparation/(.*)/?post_type=recipe">(.*)</a>',
    'strength': r'/strength/(.*)/?post_type=recipe">(.*)</a>',
    'complexity': r'/complexity/(.*)/?post_type=recipe">(.*)</a>',
    'hours': r'/hours/(.*)/?post_type=recipe">(.*)</a>',
    'theme': r'/theme/(.*)/?post_type=recipe">(.*)</a>',
    'brand': r'/?post_type=brand&amp;s=(.*)">(.*)</a>',  # once brands are done end search
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
