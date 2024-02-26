import json

def read_ingredients(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def make_spaghetti(recipe_name, ingredients):
    if recipe_name in ingredients:
        print(f"Making {recipe_name} Spaghetti carbonara with the following ingredients:")
        for step, ingredient in ingredients[recipe_name].items():
            print(f"{step}: {ingredient}")
    else:
        print("Recipe not found.")

if __name__ == "__main__":
    ingredients = read_ingredients("ingredients.json")
    # Example: Making Carbonara
    make_spaghetti("Carbonara", ingredients)
