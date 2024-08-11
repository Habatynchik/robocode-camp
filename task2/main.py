import recipe_module


def main():
    try:
        dish_name = input("Enter the name of the dish (Pasta, Salad, Cake): ")
        recipe = recipe_module.get_recipe(dish_name)
        print(f"Recipe for {dish_name}: {recipe}")

        difficulty = recipe_module.calculate_difficulty(recipe)
        difficulty_levels = {1: "Easy", 2: "Medium", 3: "Hard"}
        print(f"Cooking difficulty: {difficulty_levels[difficulty]}")

        user_ingredients = input("Enter the ingredients you have, separated by spaces: ").split()
        if recipe_module.can_cook(user_ingredients, recipe):
            print("You can cook this dish!")
        else:
            print("You are missing some ingredients.")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"Unknown error: {e}")


if __name__ == "__main__":
    main()
