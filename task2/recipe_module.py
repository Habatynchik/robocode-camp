from collections import OrderedDict
from typing import Dict, List


def get_recipe(dish_name: str) -> Dict[str, Dict[str, List[str]]]:
    recipes = {
        "Pasta": {
            "ingredients": ["pasta", "olive oil", "garlic", "tomatoes", "parmesan"],
            "steps": ["Boil pasta", "Prepare sauce", "Mix pasta and sauce", "Serve with parmesan"]
        },
        "Salad": {
            "ingredients": ["lettuce", "tomatoes", "cucumber", "olive oil", "lemon juice"],
            "steps": ["Chop vegetables", "Mix vegetables", "Add olive oil and lemon juice", "Serve"]
        },
        "Cake": {
            "ingredients": ["flour", "sugar", "eggs", "butter", "baking powder"],
            "steps": ["Mix ingredients", "Bake in oven", "Cool and serve"]
        }
    }

    if dish_name not in recipes:
        raise ValueError("Recipe not found")

    return OrderedDict(recipes[dish_name])


def calculate_difficulty(recipe: Dict[str, List[str]]) -> int:
    if not recipe.get("ingredients") or not recipe.get("steps"):
        raise ValueError("Invalid recipe format")

    num_ingredients = len(recipe["ingredients"])
    num_steps = len(recipe["steps"])

    if num_ingredients <= 5 and num_steps <= 4:
        return 1
    elif num_ingredients <= 7 and num_steps <= 6:
        return 2
    else:
        return 3


def can_cook(user_ingredients: List[str], recipe: Dict[str, List[str]]) -> bool:
    if not recipe.get("ingredients"):
        raise ValueError("Invalid recipe format")

    return all(ingredient in user_ingredients for ingredient in recipe["ingredients"])
