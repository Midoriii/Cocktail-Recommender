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
        print("getting recipe: ", recipePage)
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
    recipe.clean_recipe_attributes()
    return recipe


def scrap_title(page, recipe):
    title = page.title.string
    index = title.find(' Cocktail Recipe')  # each recipe title contains string 'Cocktail Recipe' at the end
    recipe.name = title[:index]


def scrap_ingredients(page, recipe):
    ingredient_class = str(page.findAll("div", {"class": "col-xs-9 x-recipe-ingredient"})).replace('\t', '')
    lines_with_ingredients = ingredient_class.split('\n')
    ingredient_without_link = compiled_reg_exs.ingredient_without_link_reg_ex
    ingredient_containing_link = compiled_reg_exs.ingredient_containing_link_reg_ex

    for ingredient_line in lines_with_ingredients:
        if ingredient_without_link.search(ingredient_line) is not None and ingredient_line.find('href') == -1:
            ingredient = ingredient_without_link.search(ingredient_line).group(1)
            recipe.ingredients.append(ingredient)
        if ingredient_containing_link.search(ingredient_line) is not None and ingredient_line.find('href') != -1:
            ingredient = ingredient_containing_link.search(ingredient_line).group(1)
            recipe.ingredients.append(ingredient)


def scrap_profile(page, recipe):
    for link in page.find_all('a'):
        link = str(link)

        # this string occurs after all attributes are scrapped and we can therefore stop
        if link == '<a id="spotim-comments" name="spotim-comments"></a>':
            break

        for recipe_attribute, regular_expresion in compiled_reg_exs.dict_of_compiled_profile_reg_exs.items():
            if regular_expresion.search(link) is not None:
                fill_recipe_profile_values(recipe_attribute, regular_expresion.search(link).group(2), recipe)


def scrap_glass(page, recipe):
    line_with_glass = str(page.findAll("div", {"class": "col-xs-9 recipe-link x-recipe-glasstype no-padding"}))
    if compiled_reg_exs.glass_reg_ex.search(line_with_glass) is not None:
        text = compiled_reg_exs.glass_reg_ex.search(line_with_glass).group(2)
        text = text.split(' or ')  # glass can have more than one item separated by string ' or ' e.g. 'glass1 or glass2'
        recipe.glass.extend(text)


def fill_recipe_profile_values(recipe_attribute, text, recipe):
    if recipe_attribute == 'garnish':
        text = text.split('; ')
        recipe.garnish.extend(text)
    if recipe_attribute == 'flavor':
        recipe.flavor.append(text)
    if recipe_attribute == 'base':
        recipe.base.append(text)
    if recipe_attribute == 'cocktail_type':
        recipe.cocktail_type.append(text)
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
    for recipe_page in recipe_pages:
        print('working on: ', recipe_page)
        recipe = scrap_recipe(recipe_page)
        list_of_recipes.append(recipe)

    return list_of_recipes


def save_all_recipes_as_csv():
    recipes_file = open('recipes.csv', 'w')
    table_head = "Link,Name,Ingredients,Garnish,Glass,Flavor,BaseSpirit,CocktailType,Preparation,Served,Strength,Difficulty,Hours,Occasions,Theme,Brands"
    
    pages_with_recipes = get_pages_with_recipes()
    recipe_pages = get_recipes(pages_with_recipes)
    recipes_file.write(table_head)

    for recipe_page in recipe_pages:
        print('working on: ', recipe_page)
        recipe = scrap_recipe(recipe_page)
        recipes_file.write(recipe.generate_csv_string())

    recipes_file.close()


if __name__ == "__main__":
    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'})
    compiled_reg_exs = CompiledRegExs.CompiledRegExs()
    pagesWithRecipesToLoad = 1  # there is currently 48 pages

    # list_of_recipes = scrap_all_recipes()
    # for recipe in list_of_recipes:
    #     print(recipe)
    # print(len(list_of_recipes))
    
    # save_all_recipes_as_csv()

    test_recipe_link = 'https://www.liquor.com/recipes/bacardi-pina-colada'
    recipe = scrap_recipe(test_recipe_link)
    print(recipe.generate_csv_string())
    print(recipe.generate_json_string())
    print(recipe)
else:
    # for test purposes
    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'})
    compiled_reg_exs = CompiledRegExs.CompiledRegExs()
