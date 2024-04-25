import tkinter as tk
from config import HEADER_FONT, LABEL_FONT, ENTRY_FONT
from recipes_search import search_recipes_by_ingredient, instructions_window, load_background_image


class SearchByIngredient(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="Black")
        self.controller = controller

        # Load background image
        background_image = load_background_image("background_images/Ingredient Search.png")
        if background_image:
            # Create a label to hold the image
            self.background_label = tk.Label(self, image=background_image)
            self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
            self.background_label.image = background_image  # To keep a reference

        # Title
        label = tk.Label(self, text="Search by Ingredient", font=HEADER_FONT, bg="Black", fg="White")
        label.grid(row=0, column=0, columnspan=4, pady=10, padx=10)

        # Ingredient entry
        ie_label_one = tk.Label(self, text="Enter first ingredient: ", font=LABEL_FONT, bg="Black", fg="White")
        ie_label_one.grid(row=1, column=0, padx=5, pady=(5, 0))
        self.item_entry_one = tk.Entry(self, width=10, highlightthickness=2, font=ENTRY_FONT)
        self.item_entry_one.grid(row=1, column=1, padx=10, pady=5)

        ie_label_two = tk.Label(self, text="Enter second ingredient: ", font=LABEL_FONT, bg="Black", fg="White")
        ie_label_two.grid(row=2, column=0, padx=5, pady=(5, 0))
        self.item_entry_two = tk.Entry(self, width=10, highlightthickness=2, font=ENTRY_FONT)
        self.item_entry_two.grid(row=2, column=1, padx=10, pady=5)

        ie_label_three = tk.Label(self, text="Enter third ingredient: ", font=LABEL_FONT, bg="Black", fg="White")
        ie_label_three.grid(row=3, column=0, padx=5, pady=(5, 0))
        self.item_entry_three = tk.Entry(self, width=10, highlightthickness=2, font=ENTRY_FONT)
        self.item_entry_three.grid(row=3, column=1, padx=10, pady=10)

        ie_label_four = tk.Label(self, text="Enter fourth ingredient: ", font=LABEL_FONT, bg="Black", fg="White")
        ie_label_four.grid(row=4, column=0, padx=5, pady=(5, 0))
        self.item_entry_four = tk.Entry(self, width=10, highlightthickness=2, font=ENTRY_FONT)
        self.item_entry_four.grid(row=4, column=1, padx=10, pady=10)

        # Search Button
        sr_button = tk.Button(self, text="Search", command=self.search_by_ingredient_button, font=LABEL_FONT)
        sr_button.grid(row=6, column=1, padx=10)

        # Fetch Button
        fetch_button = tk.Button(self, text="Get Instructions", font=ENTRY_FONT, command=instructions_window)
        fetch_button.grid(row=6, column=0, padx=10)

        # Results window
        self.results_text = tk.Text(self, height=20, width=55, state=tk.DISABLED, borderwidth=1, wrap=tk.WORD,
                                    font=ENTRY_FONT)
        self.results_text.grid(row=1, column=3, rowspan=4, sticky='nse')

        from frames.main_menu_frame import MainMenu

        back_button = tk.Button(self, text="Back to Main Menu", font=ENTRY_FONT,
                                command=lambda: controller.show_frame(MainMenu))
        back_button.grid(row=0, column=3, pady=5, sticky='e')

    def search_by_ingredient_button(self):
        try:
            # Get input from the user
            ingredient_one = self.item_entry_one.get()
            ingredient_two = self.item_entry_two.get()
            ingredient_three = self.item_entry_three.get()
            ingredient_four = self.item_entry_four.get()

            # Prepare list of ingredients
            ingredients = [ingredient for ingredient in
                           [ingredient_one, ingredient_two, ingredient_three, ingredient_four] if ingredient]

            # Default value for number
            number = 10

            recipes = search_recipes_by_ingredient(",".join(ingredients), number)

            self.display_recipes(recipes)

        except Exception as e:
            print("Error: ", e)

    def display_recipes(self, recipes):
        self.results_text.config(state=tk.NORMAL)
        self.results_text.delete('1.0', tk.END)
        # Display new results
        for recipe in recipes:
            recipe_title = recipe.get('title', 'Unknown Title')
            recipe_used_ingredients = recipe.get('usedIngredients', [])
            # recipe_image = recipe.get('image', 'No Image Available')
            recipe_id = recipe.get('id', 'No id available')

            # Format used ingredients
            used_ingredients_info = ""
            for ingredient in recipe_used_ingredients:
                ingredient_name = ingredient.get('name', 'Unknown Ingredient')
                ingredient_amount = ingredient.get('amount', 'Unknown Amount')
                ingredient_unit = ingredient.get('unit', 'Unknown Unit')
                used_ingredients_info += f"{ingredient_amount} {ingredient_unit} {ingredient_name}\n"

            # recipe_info = f"Title: {recipe_title}\nUsed Ingredients:\n{used_ingredients_info}\nImage: {recipe_image}\nID: {recipe_id}\n\n"
            recipe_info = f"Title: {recipe_title}\nID: {recipe_id}\nUsed Ingredients:\n{used_ingredients_info}\n\n"

            self.results_text.insert(tk.END, f"{recipe_info}\n")

        self.results_text.config(state=tk.DISABLED)

        # Debug print
        # print(recipes)
