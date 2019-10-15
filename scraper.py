from bs4 import BeautifulSoup
import requests

import CompiledRegExs
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


def scrapRecipe(recipeLink):
    page = parsePageFromLink(recipeLink)
    recipe = Recipe.Recipe()
    scrapTitle(page, recipe)
    scrapIngredients(page, recipe)
    scrapProfile(page, recipe)
    scrapGlass(page, recipe)
    print(recipe)


def scrapTitle(page, recipe):
    title = page.title.string
    index = title.find('Cocktail Recipe')
    recipe.name = title[:index]


def scrapIngredients(page, recipe):
    ingredientClass = str(page.findAll("div", {"class": "col-xs-9 x-recipe-ingredient"})).replace('\t', '')
    ingredientList = ingredientClass.split("\n")
    simpleIngredientsRegex = compiledRegExs.simpleIngredientsRegEx
    complexIngredientsRegex = compiledRegExs.complexIngredientsRegEx

    for ingredientLine in ingredientList:
        # extracts ingredients (not containing link to that ingredient)
        if simpleIngredientsRegex.search(ingredientLine) is not None and ingredientLine.find('href') == -1:
            recipe.ingredients.append(simpleIngredientsRegex.search(ingredientLine).group(1))
        # extracts ingredients with associated link
        if complexIngredientsRegex.search(ingredientLine) is not None and ingredientLine.find('href') != -1:
            recipe.ingredients.append(complexIngredientsRegex.search(ingredientLine).group(1))


def scrapProfile(page, recipe):
    for link in page.find_all('a'):
        link = str(link)

        for key, regularExpreasion in compiledRegExs.dictOfCompiledProfileRegExs.items():
            if regularExpreasion.search(link) is not None:

                # there are cocktailTypes at the end of page that doesn't belong to recipe once we reach them recipe
                # is scrapped ad we can end
                if key == 'cocktailType' and recipe.brands != []:
                    break

                fillRecipeProfileValues(key, regularExpreasion.search(link).group(2), recipe)


def scrapGlass(page, recipe):
    lineWithGlass = str(page.findAll("div", {"class": "col-xs-9 recipe-link x-recipe-glasstype no-padding"}))
    text = compiledRegExs.glassRegEx.search(lineWithGlass).group(2)
    text = text.split(' or ')  # there can be cocktails which can be served in 'glass1' or 'glass2'
    recipe.glass.extend(text)


def parsePageFromLink(link):
    pageRequest = requests.get(link, headers)
    return BeautifulSoup(pageRequest.text, 'html.parser')


def fillRecipeProfileValues(key, text, recipe):
    if key == 'garnish':
        # garnish can have more than one item separated by semicolon
        text = text.split('; ')
        recipe.garnish.extend(text)
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
    if key == 'occasions':
        recipe.hours.append(text)
    if key == 'theme':
        recipe.theme.append(text)
    if key == 'brands':
        recipe.brands.append(text)


headers = requests.utils.default_headers()
headers.update({'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'})
compiledRegExs = CompiledRegExs.CompiledRegExs()
pagesWithRecipesToLoad = 48  # there is currently 48 pages

pagesWithRecipes = []
recipePages = []

# getPagesWithRecipes()
# getRecipes()
testRecipeLink = 'https://www.liquor.com/recipes/azunia-verano-en-valencia'
scrapRecipe(testRecipeLink)

print("\n".join(recipePages))
print(len(recipePages))
