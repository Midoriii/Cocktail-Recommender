from bs4 import BeautifulSoup
import requests
import re
import os

import CompiledRegExs
import Recipe
import RecipeStatistics


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

    #A mistake on their part, this page doesn't work correctly
    recipe_pages.remove('https://www.liquor.com/recipes/godfather-101/')
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
    scrap_image(page, recipe)
    scrap_about(page, recipe)
    scrap_how_to_make(page, recipe)
    recipe.clean_recipe_attributes()
    return recipe


def scrap_title(page, recipe):
    title = page.title.string
    index = title.find(' Cocktail Recipe')  # each recipe title contains string 'Cocktail Recipe' at the end
    recipe.name = title[:index].replace(",","")


def scrap_ingredients(page, recipe):
    ingredient_class = str(page.findAll("div", {"class": "col-xs-9 x-recipe-ingredient"})).replace('\t', '')
    lines_with_ingredients = ingredient_class.split('\n')
    ingredient_without_link = compiled_reg_exs.ingredient_without_link_reg_ex
    ingredient_containing_link = compiled_reg_exs.ingredient_containing_link_reg_ex

    for ingredient_line in lines_with_ingredients:
        if ingredient_without_link.search(ingredient_line) is not None and ingredient_line.find('href') == -1:
            ingredient = ingredient_without_link.search(ingredient_line).group(1)
            recipe.ingredients.append(ingredient.replace(",",""))
        if ingredient_containing_link.search(ingredient_line) is not None and ingredient_line.find('href') != -1:
            ingredient = ingredient_containing_link.search(ingredient_line).group(1)
            recipe.ingredients.append(ingredient.replace(",",""))


def scrap_profile(page, recipe):
    for link in page.find_all('a'):
        link = str(link)

        # this string occurs after all attributes are scrapped and we can therefore stop
        if link == '<a id="spotim-comments" name="spotim-comments"></a>':
            break

        for recipe_attribute, regular_expresion in compiled_reg_exs.dict_of_compiled_profile_reg_exs.items():
            if regular_expresion.search(link) is not None:
                fill_recipe_profile_values(recipe_attribute, regular_expresion.search(link).group(2).replace(",",""), recipe)


def scrap_glass(page, recipe):
    line_with_glass = str(page.findAll("div", {"class": "col-xs-9 recipe-link x-recipe-glasstype no-padding"}))
    if compiled_reg_exs.glass_reg_ex.search(line_with_glass) is not None:
        text_regexp = compiled_reg_exs.glass_reg_ex.search(line_with_glass).group(2)
        text = text_regexp.replace(' or ', ',').replace('/', ',').split(',')  # glass can have more than one item separated by string ' or ' e.g. 'glass1 or glass2' .. or ',' or '/'
        recipe.glass.extend(text)


def scrap_image(page, recipe):
    for link in page.find_all('meta'):
        link = str(link)
        if compiled_reg_exs.image.search(link) is not None:
            recipe.image = compiled_reg_exs.image.search(link).group(1)
            break


def scrap_about(page, recipe):
    for link in page.find_all('span'):
        link = str(link).replace('\n', '')
        if compiled_reg_exs.about.search(link) is not None:
            string_with_links = compiled_reg_exs.about.search(link).group(1)
            string_without_links = re.sub(compiled_reg_exs.link_remover, '', string_with_links)
            recipe.about = string_without_links.replace('&amp;', '&')
            recipe.about = recipe.about.replace(",", "")


def scrap_how_to_make(page, recipe):
    if page.find_all('div', class_="row x-recipe-prep"):
      link = str(page.find_all('div', class_="row x-recipe-prep")[0]).replace('\n', '')
      string_with_links = link.replace('</p><p>', ' ')
      recipe.how_to_make = re.sub(compiled_reg_exs.link_remover, '', string_with_links)
      recipe.how_to_make = recipe.how_to_make.replace(",", "")
    else:
      recipe.how_to_make = '' 


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
        recipe.strength = text
    if recipe_attribute == 'difficulty':
        recipe.difficulty.append(text)
    if recipe_attribute == 'hours':
        recipe.hours.append(text)
    if recipe_attribute == 'occasion':
        recipe.occasion.append(text)
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
    recipes_file = open('data/recipes_crude.csv', 'w', encoding="utf-8")
    table_head = "Link,Name,Image,About,HowToMake,Ingredients,Garnish,Glass,Flavor,BaseSpirit,CocktailType,Preparation,Served,Strength,Difficulty,Hours,Occasions,Theme,Brands"
    
    pages_with_recipes = get_pages_with_recipes()
    recipe_pages = get_recipes(pages_with_recipes)
    recipes_file.write(table_head + '\n')

    for recipe_page in recipe_pages:
        print('working on: ', recipe_page)
        recipe = scrap_recipe(recipe_page)
        recipes_file.write(recipe.generate_csv_string())

    recipes_file.close()


def save_all_recipes_as_json():
    recipes_file = open('data/recipes.json', 'w', encoding="utf-8")

    pages_with_recipes = get_pages_with_recipes()
    recipe_pages = get_recipes(pages_with_recipes)

    recipes_file.write('[\n')
    for recipe_page in recipe_pages:
        print('working on: ', recipe_page)
        recipe = scrap_recipe(recipe_page)

        recipes_file.write(recipe.generate_json_string() + '\n')

    recipes_file.seek(recipes_file.tell() - 2, os.SEEK_SET)  # removes comma after last entry which is not allowed
    recipes_file.write('')
    recipes_file.write('\n]\n')
    recipes_file.close()


def get_statistical_data():
    recipeStatistics = RecipeStatistics.RecipeStatistics()
    pages_with_recipes = get_pages_with_recipes()
    recipe_pages = get_recipes(pages_with_recipes)
    total = len(recipe_pages)
    count = 0

    for recipe_page in recipe_pages:
        count += 1
        print('working on: ', recipe_page, ' ', count, ' from ', total)
        recipe = scrap_recipe(recipe_page)
        recipeStatistics.max_number_of_items(recipe)

    print(recipeStatistics.result_max_number_of_items())


if __name__ == "__main__":
    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'})
    compiled_reg_exs = CompiledRegExs.CompiledRegExs()
    pagesWithRecipesToLoad = 48  # there is currently 48 pages

    # list_of_recipes = scrap_all_recipes()
    # for recipe in list_of_recipes:
    #     print(recipe)
    # print(len(list_of_recipes))
    
    save_all_recipes_as_csv()
    save_all_recipes_as_json()

    # get_statistical_data()

    # test_recipe_link = 'https://www.liquor.com/recipes/hydrate'
    # recipe = scrap_recipe(test_recipe_link)
    # print(recipe.generate_json_string())
    # print(recipe)
else:
    # for test purposes
    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'})
    compiled_reg_exs = CompiledRegExs.CompiledRegExs()
