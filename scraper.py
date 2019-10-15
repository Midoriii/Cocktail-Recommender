from bs4 import BeautifulSoup
import requests

import CompiledRegExs
import Recipe


def get_pages_with_recipes():
    pages_with_recipes = []
    for i in range(pagesWithRecipesToLoad):
        pages_with_recipes.append("https://www.liquor.com/recipes/page/" + str(i) + "/")
    return pages_with_recipes


def get_recipes(pages_with_recipes):
    recipe_pages = []
    for recipePage in pages_with_recipes:
        page = parse_page_from_link(recipePage)

        for link in page.find_all('a'):
            link = str(link.get('href'))
            if link.find("https://www.liquor.com/recipes") != -1 and link.find(
                    "https://www.liquor.com/recipes/page") == -1:
                if link not in recipe_pages:
                    recipe_pages.append(link)

    return recipe_pages


def parse_page_from_link(link):
    page_request = requests.get(link, headers)
    return BeautifulSoup(page_request.text, 'html.parser')


def scrap_recipe(recipe_link):
    recipe = Recipe.Recipe()
    recipe.link = recipe_link
    page = parse_page_from_link(recipe_link)
    scrap_title(page, recipe)
    scrap_ingredients(page, recipe)
    scrap_profile(page, recipe)
    scrap_glass(page, recipe)
    return recipe


def scrap_title(page, recipe):
    title = page.title.string
    index = title.find('Cocktail Recipe')  # each recipe title contains string 'Cocktail Recipe' at the end
    recipe.name = title[:index]


def scrap_ingredients(page, recipe):
    # TODO some ingredients have trailing space get rid of it
    ingredient_class = str(page.findAll("div", {"class": "col-xs-9 x-recipe-ingredient"})).replace('\t', '')
    # some ingredients have '*' in name
    lines_with_ingredients = ingredient_class.replace('*', '').split('\n')
    ingredient_without_link = compiledRegExs.ingredientWithoutLinkRegEx
    ingredient_containing_link = compiledRegExs.ingredientContainingLinkRegEx

    for ingredientLine in lines_with_ingredients:
        if ingredient_without_link.search(ingredientLine) is not None and ingredientLine.find('href') == -1:
            recipe.ingredients.append(ingredient_without_link.search(ingredientLine).group(1))
        if ingredient_containing_link.search(ingredientLine) is not None and ingredientLine.find('href') != -1:
            recipe.ingredients.append(ingredient_containing_link.search(ingredientLine).group(1))


def scrap_profile(page, recipe):
    for link in page.find_all('a'):
        link = str(link)

        for recipeAttribute, regularExpresion in compiledRegExs.dictOfCompiledProfileRegExs.items():
            if regularExpresion.search(link) is not None:
                # there are cocktailTypes at the end of page that doesn't belong to recipe once we reach cocktailType
                # and last item of recipe (brands) has been filled we know that we are at the end
                # TODO not reliable some recipes don't have brands
                if recipeAttribute == 'cocktailType' and recipe.brands != []:
                    break
                fill_recipe_profile_values(recipeAttribute, regularExpresion.search(link).group(2), recipe)


def scrap_glass(page, recipe):
    line_with_glass = str(page.findAll("div", {"class": "col-xs-9 recipe-link x-recipe-glasstype no-padding"}))
    text = compiledRegExs.glassRegEx.search(line_with_glass).group(2)
    text = text.split(' or ')  # glass can have more than one item separated by string ' or ' e.g. 'glass1 or glass2'
    recipe.glass.extend(text)


def fill_recipe_profile_values(recipe_attribute, text, recipe):
    if recipe_attribute == 'garnish':
        # garnish can have more than one item separated by semicolon, and can contain '*'
        text = text.replace('*', '').split('; ')
        recipe.garnish.extend(text)
    if recipe_attribute == 'flavor':
        recipe.flavor.append(text)
    if recipe_attribute == 'base':
        recipe.base.append(text)
    if recipe_attribute == 'cocktailType':
        recipe.cocktailType.append(text)
    if recipe_attribute == 'served':
        recipe.served.append(text)
    if recipe_attribute == 'preparation':
        recipe.preparation.append(text)
    if recipe_attribute == 'strength':
        recipe.strength.append(text)
    if recipe_attribute == 'difficulty':
        recipe.difficulty.append(text)
    if recipe_attribute == 'hours':
        recipe.hours.append(text)
    if recipe_attribute == 'occasions':
        recipe.hours.append(text)
    if recipe_attribute == 'theme':
        recipe.theme.append(text)
    if recipe_attribute == 'brands':
        recipe.brands.append(text)


def scrap_all_recipes():
    pages_with_recipes = get_pages_with_recipes()
    recipe_pages = get_recipes(pages_with_recipes)

    list_of_recipes = []
    for recip_page in recipe_pages:
        print('working on: ', recip_page)
        recipe = scrap_recipe(recip_page)
        list_of_recipes.append(recipe)

    return list_of_recipes


headers = requests.utils.default_headers()
headers.update({'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'})
compiledRegExs = CompiledRegExs.CompiledRegExs()

if __name__ == "__main__":
    pagesWithRecipesToLoad = 1  # there is currently 48 pages
    list_of_recipes = scrap_all_recipes()
    for recipe in list_of_recipes:
        print(recipe)

# testRecipeLink = 'https://www.liquor.com/recipes/azunia-verano-en-valencia'
# scrap_recipe(testRecipeLink)
