import tkinter as tk
from frames.main_menu_frame import MainMenu
from frames.meal_planner_frame import MealPlanner
from frames.search_by_ingredient_frame import SearchByIngredient
from frames.shopping_list_frame import ShoppingList
from frames.pantry_inventory_frame import PantryInventory
from frames.search_recipes_frame import SearchRecipes
from frames.create_with_pantry_frame import CreateWithPantry

FRAMES_LIST = (
    MainMenu, MealPlanner, SearchByIngredient, ShoppingList, PantryInventory, SearchRecipes, CreateWithPantry
)


# from config import FONT
# from tkinter import ttk, messagebox
# from recipes_search import search_recipes, search_recipes_by_ingredient, display_recipes, get_recipe_instructions


class PantryCraft(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.grid(row=0, column=0, sticky="nsew")
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in FRAMES_LIST:
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(MainMenu)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


if __name__ == "__main__":
    app = PantryCraft()
    app.title("PantryCraft")
    app.geometry("1440x915")
    app.mainloop()

#
#
# def search_recipes_button():
#     search_params = sr_entry.get()
#     # Get user input for the number of results (optional)
#     number_str = sr_num_entry.get()
#     # Check if the user provided a valid number or left it blank
#     if number_str.strip().isdigit():
#         number = int(number_str)
#     else:
#         number = None  # Use the default value from the API
#     recipes = search_recipes(search_params=search_params, number=number)
#     display_recipes(recipes=recipes, text_widget=results_text)
#
#
# def search_by_ingredient_button(entry_ingredients, entry_number):
#     ingredients_input = entry_ingredients.get()
#     number_input = entry_number.get()
#     if number_input.strip().isdigit():
#         number = int(number_input)
#     else:
#         number = None
#     recipes = search_recipes_by_ingredient(ingredients_input, number)
#     display_recipes(recipes=recipes, text_widget=results_text)


# def format_instructions(instructions_data):
#     formatted_text = ""
#     for section in instructions_data:
#         formatted_text += f"{section['name']}:\n"
#         for step in section['steps']:
#             formatted_text += f"{step['number']}. {step['step']}\n"
#             if 'ingredients' in step:
#                 formatted_text += "   - Ingredients: " + ", ".join(
#                     ingredient['name'] for ingredient in step['ingredients']) + "\n"
#             if 'equipment' in step:
#                 equipment_list = [equipment['name'] for equipment in step['equipment']]
#                 if equipment_list:
#                     formatted_text += "   - Equipment: " + ", ".join(equipment_list) + "\n"
#             if 'length' in step:
#                 formatted_text += f"   - Time: {step['length']['number']} {step['length']['unit']}\n"
#         formatted_text += "\n"
#
#     return formatted_text

# def get_recipe_instructions_button(recipe_id):
#     try:
#         instructions_data = get_recipe_instructions(recipe_id)
#         formatted_text = format_instructions(instructions_data)
#         messagebox.showinfo("Recipe Instructions", formatted_text)
#     except ValueError:
#         messagebox.showerror("Invalid ID")


# # GUI Setup
# window = tk.Tk()
# window.title("Pantry Craft")
# window.config(bg="teal")
#
# # --- Search Recipes ---
# # Entry
# sr_label = tk.Label(window, text="Enter a recipe: ")
# sr_label.grid(row=0, column=0, padx=5, pady=(5, 0))
# sr_entry = tk.Entry(window, width=20)
# sr_entry.grid(row=0, column=1, padx=5)
# # Number Entry - Number of results
# sr_num_label = tk.Label(window, text="Enter number of results (optional): ")
# sr_num_label.grid(row=1, column=0, padx=5)
# sr_num_entry = tk.Entry(window, width=20)
# sr_num_entry.grid(row=1, column=1, padx=5)
# # Button
# sr_button = tk.Button(window, text="Search Recipes", command=search_recipes_button)
# sr_button.grid(row=1, column=2, padx=10)
# # Separator
# separator = ttk.Separator(window, orient="horizontal")
# separator.grid(row=2, column=0, columnspan=3, pady=10, sticky="ew")
#
# # --- Search Recipes by Ingredient(s) ---
# # Entry
# si_label = tk.Label(window, text="Enter ingredients (separated with commas): ")
# si_label.grid(row=3, column=0, padx=5)
# si_entry = tk.Entry(window, width=20)
# si_entry.grid(row=3, column=1, padx=5)
# # Number of results
# si_num_e_label = tk.Label(window, text="Enter number of results (optional): ")
# si_num_e_label.grid(row=4, column=0, padx=5)
# si_num_entry = tk.Entry(window, width=20)
# si_num_entry.grid(row=4, column=1, padx=5)
# # Button
# si_button = tk.Button(window, text="Search by Ingredient",
#                       command=lambda: search_by_ingredient_button(si_entry, si_num_entry))
# si_button.grid(row=4, column=2, padx=10)
# # Separator
# separator = ttk.Separator(window, orient="horizontal")
# separator.grid(row=5, column=0, columnspan=3, pady=10, sticky="ew")
#
# # --- Recipe Instructions ---
# # Entry
# ri_label = tk.Label(window, text="Recipe Instructions (Input Dish ID):")
# ri_label.grid(row=6, column=0, padx=5)
# ri_entry = tk.Entry(window, width=20)
# ri_entry.grid(row=6, column=1, padx=5)
# # Button
# ri_button = tk.Button(window, text="Find Instructions",
#                       command=lambda: get_recipe_instructions_button(recipe_id=ri_entry.get()))
# ri_button.grid(row=6, column=2, padx=10)
#
# # Result Text - Change the row/column if needed later
# results_text = tk.Text(window, height=20, width=60, state=tk.DISABLED, borderwidth=2, wrap=tk.WORD)
# results_text.grid(row=15, column=0, columnspan=3, padx=10, pady=10)
# # Vertical Scrollbar
# scrollbar = tk.Scrollbar(window, command=results_text.yview)
# scrollbar.grid(row=15, column=3, sticky="ns")
# results_text.config(yscrollcommand=scrollbar.set)
#
# window.mainloop()
