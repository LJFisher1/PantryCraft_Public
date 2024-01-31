import requests
import tkinter as tk
from config import HEADERS
# from tkinter import messagebox
# from PIL import Image, ImageTk
# from urllib.request import urlopen
# from io import BytesIO


def search_recipes(search_params, number=None):
    recipe_search_url = "https://api.spoonacular.com/recipes/complexSearch"
    params = {"query": search_params}

    if number is not None:
        params["number"] = number

    recipe_response = requests.get(url=recipe_search_url, params=params, headers=HEADERS)
    recipes_data = recipe_response.json()

    return recipes_data["results"]


def search_recipes_by_ingredient(ingredients_input, number):
    ingredients = [ingredient.strip() for ingredient in ingredients_input.split(",")]

    recipes_by_ingredient_url = "https://api.spoonacular.com/recipes/findByIngredients"
    params = {"ingredients": ",".join(ingredients)}

    if number is not None:
        params['number'] = number

    response = requests.get(url=recipes_by_ingredient_url, params=params, headers=HEADERS)
    recipes_data = response.json()

    return recipes_data


def get_recipe_instructions(recipe_id):
    instructions_url = f"https://api.spoonacular.com/recipes/{recipe_id}/analyzedInstructions"
    response = requests.get(url=instructions_url, headers=HEADERS)
    instructions_data = response.json()
    return instructions_data


# def format_instructions(recipe_id, results_text):
#     try:
#         instructions_data = get_recipe_instructions(recipe_id)
#
#         for step in instructions_data[0]['steps']:
#             formatted_step = f"Step {step['number']}: {step['step']}\n"
#
#             if step['ingredients']:
#                 formatted_step += "Ingredients:\n"
#                 for ingredient in step['ingredients']:
#                     formatted_step += f"  - {ingredient['name']}\n"
#
#             if step['equipment']:
#                 formatted_step += "Equipment:\n"
#                 for equipment in step['equipment']:
#                     formatted_step += f"  - {equipment['name']}\n"
#
#             if 'length' in step and 'unit' in step['length']:
#                 length_unit = step['length']['unit']
#                 length_number = step['length']['number']
#                 formatted_step += f"Length: {length_number} {length_unit}\n"
#
#             formatted_step += "\n"  # Separate steps with a blank line
#             results_text.insert(tk.END, formatted_step)
#
#     except ValueError:
#         messagebox.showerror("Invalid ID")


def display_recipes(recipes, text_widget):
    text_widget.config(state=tk.NORMAL)
    text_widget.delete(1.0, tk.END)  # Clears previous results

    for result in recipes:
        text_widget.insert(tk.END, f"ID: {result['id']}\nName: {result['title']}\n\n")
        # text_widget.insert(tk.END, f"ID: {result['id']}")
        # # Display image
        # image_url = result['image']
        # if image_url:
        #     response = requests.get(image_url)
        #     image_data = BytesIO(response.content)
        #     image = Image.open(image_data)
        #     image = ImageTk.PhotoImage(image)
        #     canvas.create_image(10, 10, anchor=tk.NW, image=image)

        text_widget.insert(tk.END, "\n")  # Add a line break after each result

    text_widget.config(state=tk.DISABLED)
