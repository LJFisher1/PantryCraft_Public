import asyncio
import requests
import tkinter as tk
from config import HEADERS, ENTRY_FONT, format_instructions, LABEL_FONT
from PIL import Image, ImageTk
from io import BytesIO

images = []


def search_recipes(search_params, number=None):
    recipe_search_url = "https://api.spoonacular.com/recipes/complexSearch"
    params = {"query": search_params}

    if number is not None:
        params["number"] = number

    recipe_response = requests.get(url=recipe_search_url, params=params, headers=HEADERS)
    recipes_data = recipe_response.json()
    # print(recipes_data)

    return recipes_data["results"]


def search_recipes_by_ingredient(ingredients_input, number):
    ingredients = [ingredient.strip() for ingredient in ingredients_input.split(",")]

    recipes_by_ingredient_url = "https://api.spoonacular.com/recipes/findByIngredients"
    params = {"ingredients": ",".join(ingredients)}

    if number is not None:
        params['number'] = number

    response = requests.get(url=recipes_by_ingredient_url, params=params, headers=HEADERS)
    recipes_data = response.json()
    # print(recipes_data) # Debug Print
    return recipes_data


def get_recipe_instructions_bulk(recipe_ids):
    instructions_url = "https://api.spoonacular.com/recipes/informationBulk"
    params = {"ids": ",".join(str(id) for id in recipe_ids)}

    response = requests.get(url=instructions_url, params=params, headers=HEADERS)
    instructions_data = response.json()

    instructions_map = {recipe['id']: recipe.get('analyzedInstructions') for recipe in instructions_data}

    return instructions_map


def run_asyncio(recipe_id_entry, instructions_text):
    async def fetch_instructions_async(recipe_id_entry, instructions_text):
        recipe_ids = recipe_id_entry.get().split(',')
        instructions_map = get_recipe_instructions_bulk(recipe_ids)

        for recipe_id in recipe_ids:
            instructions = instructions_map.get(int(recipe_id))
            instructions_text.config(state=tk.NORMAL)
            instructions_text.delete('1.0', tk.END)

            if instructions:
                formatted_instructions = format_instructions(instructions)
                instructions_text.insert(tk.END, formatted_instructions)
            else:
                instructions_text.insert(tk.END, f'Instructions not found for recipe ID: {recipe_id}')

        instructions_text.config(state=tk.DISABLED)

    async def main(recipe_id_entry, instructions_text):
        await fetch_instructions_async(recipe_id_entry, instructions_text)

    asyncio.run(main(recipe_id_entry, instructions_text))


def instructions_window():
    window = tk.Toplevel()
    window.title("Recipe Instructions")

    # Label and entry for recipe ID
    label = tk.Label(window, text="Enter comma-separated recipe IDs", font=LABEL_FONT)
    label.pack()
    recipe_id_entry = tk.Entry(window, font=ENTRY_FONT)
    recipe_id_entry.pack()

    # Button for fetching
    fetch_button = tk.Button(window, text="Get Instructions", font=ENTRY_FONT,
                             command=lambda: run_asyncio(recipe_id_entry, instructions_text))
    fetch_button.pack()

    # Text widget to display instructions
    instructions_text = tk.Text(window, height=20, width=55, state=tk.DISABLED, borderwidth=1, wrap=tk.WORD,
                                font=ENTRY_FONT)
    instructions_text.pack()

    window.mainloop()


#
# def get_recipe_instructions(recipe_id):
#     instructions_url = f"https://api.spoonacular.com/recipes/{recipe_id}/analyzedInstructions"
#     response = requests.get(url=instructions_url, headers=HEADERS)
#     instructions_data = response.json()
#
#     if instructions_data and instructions_data[0].get('steps'):
#         for step in instructions_data[0]['steps']:
#             if 'ingredients' in step:
#                 for ingredient in step['ingredients']:
#                     ingredient_id = ingredient.get('id')
#                     if ingredient_id:
#                         # Call the endpoint to get ingredient details
#                         ingredient_widget_url = f"https://api.spoonacular.com/recipes/{recipe_id}/ingredientWidget.json"
#                         ingredient_response = requests.get(url=ingredient_widget_url, headers=HEADERS)
#                         ingredient_widget_data = ingredient_response.json()
#                         # Extract the measurements
#                         for widget_ingredient in ingredient_widget_data['ingredients']:
#                             if widget_ingredient.get('id') == ingredient_id:
#                                 # measurement = None
#                                 if 'amount' in widget_ingredient and 'metric' in widget_ingredient['amount']:
#                                     metric_amount = widget_ingredient['amount']['metric']
#                                     if metric_amount['unit']:  # Check if unit value is not empty
#                                         measurement = {
#                                             'amount': metric_amount['value'],
#                                             'unit': metric_amount['unit']
#                                         }
#                                     else:
#                                         measurement = {
#                                             'amount': metric_amount['value'],
#                                             'unit': ''  # Set unit to empty string if it's empty in the API response
#                                         }
#                                 else:
#                                     measurement = None
#                                 # Add the measurement to the ingredient dictionary
#                                 ingredient['measurement'] = measurement
#                             # print("Widget Ingredient: ", widget_ingredient)
#
#     return instructions_data
#
#
# def instructions_window():
#     def fetch_instructions():
#         recipe_id = recipe_id_entry.get()
#         instructions = get_recipe_instructions(recipe_id)
#
#         # print(f"Recipe ID entered: {recipe_id}")  # Debug print
#         # print(instructions)
#         if instructions:
#             instructions_text.config(state=tk.NORMAL)
#             instructions_text.delete('1.0', tk.END)
#             formatted_instructions = format_instructions(instructions)
#             instructions_text.insert(tk.END, formatted_instructions)
#             instructions_text.config(state=tk.DISABLED)
#         else:
#             instructions_text.config(state=tk.NORMAL)
#             instructions_text.delete('1.0', tk.END)
#             instructions_text.insert(tk.END, 'Instructions not found for this recipe.')
#             instructions_text.config(state=tk.DISABLED)
#
#     window = tk.Toplevel()
#     window.title("Recipe Instructions")
#
#     # Label and entry for recipe ID
#     label = tk.Label(window, text="Enter recipe ID", font=LABEL_FONT)
#     label.pack()
#     recipe_id_entry = tk.Entry(window, font=ENTRY_FONT)
#     recipe_id_entry.pack()
#
#     # Button for fetching
#     fetch_button = tk.Button(window, text="Get Instructions", font=ENTRY_FONT, command=fetch_instructions)
#     fetch_button.pack()
#
#     # Text widget to display instructions
#     instructions_text = tk.Text(window, height=20, width=55, state=tk.DISABLED, borderwidth=1, wrap=tk.WORD,
#                                 font=ENTRY_FONT)
#     instructions_text.pack()
#

def load_image(image_url):
    response = requests.get(image_url)
    print("Image URL: ", image_url, "Status Code: ", response.status_code)
    if response.status_code == 200:
        image_data = BytesIO(response.content)
        pil_image = Image.open(image_data)
        # resized_image = pil_image.resize((100, 100))
        tk_image = ImageTk.PhotoImage(pil_image)
        return tk_image
    else:
        print("Failed to load image. Status Code: ", response.status_code)
        return None


def display_recipes(recipes, text_widget, canvas_widget):
    # Global variable to store image references
    global images
    # Clears previous image results before adding new ones
    images.clear()

    print("display_recipes called")
    text_widget.config(state=tk.NORMAL)
    text_widget.delete(1.0, tk.END)  # Clears previous results
    image_y = 100
    text_x = 150
    # images = []
    i = 0

    if not recipes:
        text_widget.insert(tk.END, "No recipes to display.\n")
    else:
        for result in recipes:
            text_widget.insert(tk.END, f"Name: {result['title']}\nID: {result['id']}\n\n")
            i += 1
            # Display image
            image_url = result['image']
            if image_url:
                image = load_image(image_url)

                if image:
                    # Display image in the Canvas widget
                    canvas_image = canvas_widget.create_image(text_x, image_y, anchor=tk.W, image=image)
                    # canvas_widget.image = image # Save a reference to prevent garbage collection
                    images.append((image, canvas_image))

                    text_widget.update_idletasks()
                    canvas_widget.update_idletasks()
                    print(f"Image {i} printed")

                    # Adjust canvas height and scrolling region
                    canvas_height = image_y + 250
                    canvas_widget.config(scrollregion=(0, 0, 0, canvas_height))
                    print("Canvas scroll region:", canvas_widget.cget("scrollregion"))

                image_y += 250

            text_widget.insert(tk.END, "\n")  # Add a line break after each result
    text_widget.config(state=tk.DISABLED)
    return images


def load_background_image(image_path):
    try:
        image = Image.open(image_path)
        tk_image = ImageTk.PhotoImage(image)
        return tk_image
    except Exception as e:
        print("Failed to load background image: ", e)
        return None
