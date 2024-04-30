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
        self.entry_fields = []
        for i in range(4):
            label_text = f"Enter ingredient {i + 1}: "
            label = tk.Label(self, text=label_text, font=LABEL_FONT, bg="Black", fg="White")
            label.grid(row=i + 1, column=0, padx=5, pady=(5, 0))

            entry = tk.Entry(self, width=10, highlightthickness=2, font=("Helvetica", 14, "normal"), fg="Grey")
            entry.grid(row=i + 1, column=1, padx=10, pady=5)
            entry.insert(0, "Enter an item")
            entry.bind("<FocusIn>", self.clear_entry)
            entry.bind("<FocusOut>", self.restore_entry)
            self.entry_fields.append(entry)

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
            for entry in self.entry_fields:
                entry_value = entry.get()
                if entry_value == "Enter an item":
                    entry.delete(0, tk.END)

            # Get input from the user
            ingredient_one = self.entry_fields[0].get()
            ingredient_two = self.entry_fields[1].get()
            ingredient_three = self.entry_fields[2].get()
            ingredient_four = self.entry_fields[3].get()

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

            recipe_info = f"Title: {recipe_title}\nID: {recipe_id}\nUsed Ingredients:\n{used_ingredients_info}\n\n"

            self.results_text.insert(tk.END, f"{recipe_info}\n")

        self.results_text.config(state=tk.DISABLED)

    def clear_entry(self, event):
        entry = event.widget
        if entry.get() == "Enter an item":
            entry.delete(0, tk.END)
            entry.config(fg="Grey")

    def restore_entry(self, event):
        entry = event.widget
        if not entry.get():
            entry.insert(0, "Enter an item")
            entry.config(fg="Grey")
