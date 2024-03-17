import requests
import csv

api_id = "fd0f2584"
api_key = "5a43398a87f217e7a9ae564ef90da41e"

def search(ingredient):
    ingredient_search = f'https://api.edamam.com/search?q={ingredient}&app_id={api_id}&app_key={api_key}'
    response = requests.get(ingredient_search)
    data = response.json()
    return data['hits']

def run():
    results = search(ingredient)
    for response in results:
        recipe = response['recipe']

        print(recipe['label'])
        print(recipe['uri'])
        print()


while True:
    ingredient = input("What ingredient would you like in your recipe? ")
    run()

    file_save = input("Would you like these saved in a file? Yes or No ")
    file_save = file_save.lower()

    if file_save == 'yes':

        recipes_file = open('recipes.txt', 'a')
        results = search(ingredient)

        recipes_file.write(f'Recipes with {ingredient}: ')
        recipes_file.write('\n')
        recipes_file.write(' \n')

        for response in results:
            recipe = response['recipe']

            recipes_file.write(recipe['label'])
            recipes_file.write('\n')
            recipes_file.write(recipe['uri'])
            recipes_file.write('\n')
            recipes_file.write(' \n')

        recipes_file.close()


    should_continue = input("Do you want to carry on? Yes or No ")
    should_continue = should_continue.lower()
    if should_continue == 'no':
        break
