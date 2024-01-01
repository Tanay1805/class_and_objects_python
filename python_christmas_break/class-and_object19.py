class Ingredient:
    def __init__(self, name):
        self.name = name

class Recipe:
    def __init__(self, title, ingredients, instructions, user):
        self.title = title
        self.ingredients = ingredients
        self.instructions = instructions
        self.user = user

class User:
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email

class RecipeManagementSystem:
    def __init__(self):
        self.recipes = []

    def add_recipe(self, title, ingredient_names, instructions, user):
        ingredients = [Ingredient(name) for name in ingredient_names]
        recipe = Recipe(title, ingredients, instructions, user)
        self.recipes.append(recipe)
        print(f"Recipe '{title}' added successfully by {user.name}.")

    def search_by_ingredient(self, ingredient_name):
        matching_recipes = []
        for recipe in self.recipes:
            if any(ingredient.name.lower() == ingredient_name.lower() for ingredient in recipe.ingredients):
                matching_recipes.append(recipe)
        return matching_recipes

# Example Usage with User Input:
recipe_system = RecipeManagementSystem()

while True:
    print("\n1. Add Recipe\n2. Search by Ingredient\n3. Exit")
    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        title = input("Enter Recipe Title: ")
        ingredient_names = input("Enter Ingredient Names (comma-separated): ").split(',')
        instructions = input("Enter Recipe Instructions: ")
        user_name = input("Enter Your Name: ")
        user_email = input("Enter Your Email: ")
        user = User(1, user_name, user_email)
        recipe_system.add_recipe(title, ingredient_names, instructions, user)
    elif choice == '2':
        ingredient_to_search = input("Enter an ingredient to search for recipes: ")
        matching_recipes = recipe_system.search_by_ingredient(ingredient_to_search)
        if matching_recipes:
            print(f"Recipes containing {ingredient_to_search}:")
            for recipe in matching_recipes:
                print(f"{recipe.title} by {recipe.user.name}")
        else:
            print(f"No recipes found containing {ingredient_to_search}.")
    elif choice == '3':
        break
    else:
        print("Invalid Choice. Please enter a valid option.")
