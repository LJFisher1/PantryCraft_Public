import tkinter as tk
from config import HEADER_FONT, LABEL_FONT, ENTRY_FONT
from recipes_search import search_recipes_by_ingredient
import random


class CreateWithPantry(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Title
        label = tk.Label(self, text="Create with Pantry", font=HEADER_FONT)
        label.grid(row=0, column=0, columnspan=2, pady=10, padx=10)

        # Pantry inventory label
        self.pantry_inventory_label = tk.Label(self, text="You have: ", font=LABEL_FONT)
        self.pantry_inventory_label.grid(row=1, column=0, sticky='n')

        # Pantry Inventory text box
        self.pantry_inventory_text = tk.Text(self, height=20, width=40, font=ENTRY_FONT)
        self.pantry_inventory_text.grid(row=2, column=0, padx=10, pady=10, sticky='nsew')

        # Meal display label
        self.meals_display_label = tk.Label(self, text="You can make: ", font=LABEL_FONT)
        self.meals_display_label.grid(row=1, column=1, sticky='n')

        # Meal display box
        self.meals_display_text = tk.Text(self, height=20, width=40, font=ENTRY_FONT)
        self.meals_display_text.grid(row=2, column=1, padx=10, pady=10, sticky='nsew')

        # Load pantry inventory
        self.load_pantry_inventory()

        # Load meals based on pantry inventory
        self.load_meals()

        from .main_menu_frame import MainMenu

        back_button = tk.Button(self, text="Back to Main Menu", command=lambda: controller.show_frame(MainMenu))
        back_button.grid(row=0, column=2, pady=5)

    def load_pantry_inventory(self):
        # Code to load and display pantry inventory goes here
        try:
            with open("pantry_inventory.txt", "r") as file:
                pantry_inventory_data = file.read()
                self.pantry_inventory_text.insert(tk.END, pantry_inventory_data)
        except FileNotFoundError:
            self.pantry_inventory_text.insert(tk.END, "Pantry inventory not found.")

    def load_meals(self):
        ingredients_input = self.get_pantry_ingredients()
        if ingredients_input:

            recipes = search_recipes_by_ingredient(ingredients_input, number=10)
            if recipes:
                for recipe in recipes:
                    self.meals_display_text.insert(tk.END, f"{recipe['title']}\n\n")
            else:
                self.meals_display_text.insert(tk.END, "No meals found based on the ingredients in pantry.")
        else:
            self.meals_display_text.insert(tk.END, "No ingredients in pantry.")
        self.meals_display_text.config(wrap=tk.WORD)

    def get_pantry_ingredients(self):
        return self.pantry_inventory_text.get("1.0", tk.END).strip()
