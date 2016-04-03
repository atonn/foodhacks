#simply prints the recipe from spoonacular-findByIngredients that has the most likes
access_token = "TOKEN HERE"

import unirest

#takes list of ingredient names (strings), returns spoonacular API response for recipe search
def get_recipes(ingredient_list):

    get_string = "https://spoonacular-recipe-food-nutrition-v1.p.mashape.com/recipes/findByIngredients?ingredients="
    
    for ingredient in ingredient_list:
        get_string = get_string + ingredient + "%2C"
    
    get_string = get_string + "&limitLicense=false&number=5&ranking=1"
    
    print "making API call ..."
    
    response = unirest.get(get_string,
      headers={
        "X-Mashape-Key": access_token,
        "Accept": "application/json"
      }
    )
    
    print "API call done ..."
    return response

user_input = raw_input("Enter space separated ingredients: ")
user_input = user_input.split(" ")

response = get_recipes(user_input)

#sort list by likes
sorted_list = sorted(response.body, key=lambda k: k['likes'], reverse=True)

print "###"

#for now, just print the factoids for the most liked recipe.
if sorted_list != []:
    for item in sorted_list[0]:
        print item, ": ", sorted_list[0][item]
else:
    "Nothing found ... :C"
    
