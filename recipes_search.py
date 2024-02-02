import requests
import tkinter as tk
from config import HEADERS
from PIL import Image, ImageTk
from io import BytesIO


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

    return recipes_data


def get_recipe_instructions(recipe_id):
    instructions_url = f"https://api.spoonacular.com/recipes/{recipe_id}/analyzedInstructions"
    response = requests.get(url=instructions_url, headers=HEADERS)
    instructions_data = response.json()
    return instructions_data


def load_image(image_url):
    response = requests.get(image_url)
    # print("Image URL: ", image_url, "Status Code: ", response.status_code)
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
    # print("display_recipes called")
    text_widget.config(state=tk.NORMAL)
    text_widget.delete(1.0, tk.END)  # Clears previous results
    image_y = 0
    text_x = 150
    images = []

    if not recipes:
        text_widget.insert(tk.END, "No recipes to display.\n")
    else:
        for result in recipes:
            text_widget.insert(tk.END, f"Name: {result['title']}\n")

            # Display image
            image_url = result['image']
            if image_url:
                image = load_image(image_url)
                image_y += 100
                if image:
                    # Display image in the Canvas widget
                    # text_widget.image_create(tk.END, image=image)
                    # text_widget.insert(tk.END, "\n")
                    canvas_image = canvas_widget.create_image(text_x, image_y, anchor=tk.W, image=image)
                    # canvas_widget.image = image # Save a reference to prevent garbage collection
                    images.append(canvas_image)

                    text_widget.update_idletasks()
                    canvas_widget.update_idletasks()

            text_widget.insert(tk.END, "\n")  # Add a line break after each result
    text_widget.config(state=tk.DISABLED)
    return images

    # print(f"Processing recipe ID: {result['id']}")
    # text_widget.insert(tk.END, f"ID: {result['id']}\nName: {result['title']}\n\n")
    # text_widget.insert(current_position, f"Name: {result['title']}\n")
    # # text_widget.insert(tk.END, f"Name: {result['title']}\n\n")
    # # current_position = text_widget.index(tk.END)
    #
    # # Display image
    # image_url = result['image']
    # if image_url:
    #     image = load_image(image_url)
    #     if image:
    #         canvas_widget.create_image(0, current_position, anchor=tk.NW, image=image)
    #         canvas_widget.image = image
    #         # current_position = text_widget.index(tk.END)
    #         # display_image(text_widget, image)
    #     else:
    #         print("Image loading failed for URL: ", image_url)
    #
    # # text_widget.insert(tk.END, "\n")  # Add a line break after each result
    # text_widget.insert(current_position, "\n")
    # current_position = text_widget.index(tk.END)

    # # Load image from URL using PIL
    # pil_image = Image.open(image_url)
    # # Resize image as needed
    # resized_image = pil_image.resize((100, 100))
    # # Convert PIL image to Tkinter PhotoImage
    # tk_image = ImageTk.PhotoImage(resized_image)
    # return tk_image


def display_image(text_widget, image):
    # Display image in the Text widget
    text_widget.image_create(tk.END, image=image)
    # Add a newline after each image
    text_widget.insert(tk.END, "\n")
