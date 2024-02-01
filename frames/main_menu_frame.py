import tkinter as tk
from .meal_planner_frame import MealPlanner
from .search_by_ingredient_frame import SearchByIngredient
from .shopping_list_frame import ShoppingList
from .pantry_inventory_frame import PantryInventory
from .search_recipes_frame import SearchRecipes
from .create_with_pantry_frame import CreateWithPantry


class MainMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="Black")
        self.controller = controller

        label = tk.Label(self, text="Main Menu", font=("Helvetica", 72, "normal"))
        label.grid(row=0, column=0, columnspan=2, pady=10, padx=10)

        meal_planner_button = tk.Button(self, text="Meal Planner", width=85, height=10,
                                        command=lambda: controller.show_frame(MealPlanner))
        meal_planner_button.grid(row=1, column=0, pady=50, padx=58)

        ingredient_button = tk.Button(self, text="Search by Ingredient", width=85, height=10,
                                      command=lambda: controller.show_frame(SearchByIngredient))
        ingredient_button.grid(row=1, column=1, pady=50, padx=58)

        shopping_list_button = tk.Button(self, text="Shopping List", width=85, height=10,
                                         command=lambda: controller.show_frame(ShoppingList))
        shopping_list_button.grid(row=2, column=0, pady=50, padx=58)

        pantry_inventory_button = tk.Button(self, text="Pantry Inventory", width=85, height=10,
                                            command=lambda: controller.show_frame(PantryInventory))
        pantry_inventory_button.grid(row=2, column=1, pady=50, padx=58)

        search_recipes_button = tk.Button(self, text="Search Recipes", width=85, height=10,
                                          command=lambda: controller.show_frame(SearchRecipes))
        search_recipes_button.grid(row=3, column=0, pady=50, padx=58)
        print("SearchRecipes frame initialized.")

        create_with_pantry_button = tk.Button(self, text="Create with Pantry", width=85, height=10,
                                              command=lambda: controller.show_frame(CreateWithPantry))
        create_with_pantry_button.grid(row=3, column=1, pady=50, padx=58)
