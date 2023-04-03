import requests

# Get up to 7 ingredients from user input
ingredients_list = []
for i in range(7):
    ingredient = input("Enter an ingredient (or 'done' when finished): ")
    if ingredient.lower() == "done":
        break
    ingredients_list.append(ingredient)

# Make API request to find recipes with specified ingredients
API_KEY = "ENTER YOUR OWN API KEY HERE"
url = f"https://api.spoonacular.com/recipes/findByIngredients?ingredients=" \
      f"{','.join(ingredients_list)}&number=1&apiKey={API_KEY}"

response = requests.get(url)

# Print recipe if found, or error message if not found
if response.status_code == 200 and len(response.json()) > 0:
    recipe = response.json()[0]
    recipe_url = f"https://api.spoonacular.com/recipes/{recipe['id']}/information?includeNutrition=false&apiKey={API_KEY}"
    recipe_response = requests.get(recipe_url)
    recipe_info = recipe_response.json()
    print(f"Here's a recipe you can make with {','.join(ingredients_list)}:")
    print(f"Title: {recipe['title']}")
    print(f"Link: {recipe_info['spoonacularSourceUrl']}")

else:
    print("No recipe found with those ingredients.")
