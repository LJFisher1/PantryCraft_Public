import tkinter as tk
from .meal_planner_frame import MealPlanner
from .search_by_ingredient_frame import SearchByIngredient
from .shopping_list_frame import ShoppingList
from .pantry_inventory_frame import PantryInventory
from .search_recipes_frame import SearchRecipes
from .create_with_pantry_frame import CreateWithPantry
from config import ENTRY_FONT, HEADER_FONT


class MainMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="Black")
        self.controller = controller

        button_width = 20
        button_height = 5
        button_xpad = 20
        button_ypad = 20

        label = tk.Label(self, text="Main Menu", font=HEADER_FONT, bg="Black", fg="White")
        label.grid(row=0, column=0, columnspan=2, padx=10, sticky="new")

        meal_planner_button = tk.Button(self, text="Meal Planner", width=button_width, height=button_height,
                                        font=ENTRY_FONT,
                                        command=lambda: controller.show_frame(MealPlanner))
        meal_planner_button.grid(row=1, column=0, padx=button_xpad, pady=button_ypad, sticky="nsew")

        ingredient_button = tk.Button(self, text="Search by Ingredient", width=button_width, height=button_height,
                                      font=ENTRY_FONT,
                                      command=lambda: controller.show_frame(SearchByIngredient))
        ingredient_button.grid(row=1, column=1, padx=button_xpad, pady=button_ypad, sticky="nsew")

        shopping_list_button = tk.Button(self, text="Shopping List", width=button_width, height=button_height,
                                         font=ENTRY_FONT,
                                         command=lambda: controller.show_frame(ShoppingList))
        shopping_list_button.grid(row=2, column=0, padx=button_xpad, pady=button_ypad, sticky="nsew")

        pantry_inventory_button = tk.Button(self, text="Pantry Inventory", width=button_width, height=button_height,
                                            font=ENTRY_FONT,
                                            command=lambda: controller.show_frame(PantryInventory))
        pantry_inventory_button.grid(row=2, column=1, padx=button_xpad, pady=button_ypad, sticky="nsew")

        search_recipes_button = tk.Button(self, text="Search Recipes", width=button_width, height=button_height,
                                          font=ENTRY_FONT,
                                          command=lambda: controller.show_frame(SearchRecipes))
        search_recipes_button.grid(row=3, column=0, padx=button_xpad, pady=button_ypad, sticky="nsew")

        create_with_pantry_button = tk.Button(self, text="Create with Pantry", width=button_width, height=button_height,
                                              font=ENTRY_FONT,
                                              command=lambda: controller.show_frame(CreateWithPantry))
        create_with_pantry_button.grid(row=3, column=1, padx=button_xpad, pady=button_ypad, sticky="nsew")

        # Configure row and column weights to distribute extra space evenly
        self.grid_rowconfigure((0, 4), weight=1)
        self.grid_columnconfigure((0, 1), weight=1)