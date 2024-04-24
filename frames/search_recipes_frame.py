import tkinter as tk
from config import HEADER_FONT, LABEL_FONT, ENTRY_FONT
from recipes_search import search_recipes, display_recipes, instructions_window


class SearchRecipes(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="Black")
        self.controller = controller

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)
        self.rowconfigure(3, weight=1)

        label = tk.Label(self, text="Search Recipes", font=HEADER_FONT, bg="Black", fg="White")
        label.grid(row=0, column=0, columnspan=4, pady=10, padx=10)

        back_button = tk.Button(self, text="Back to Main Menu", command=self.back_to_main_menu, font=LABEL_FONT)
        back_button.grid(row=0, column=2, pady=5)

        # Entry
        sr_label = tk.Label(self, text="Enter a recipe: ", font=LABEL_FONT, bg="Black", fg="White")
        sr_label.grid(row=1, column=0, padx=5, pady=(5, 0))
        self.sr_entry = tk.Entry(self, width=40, highlightthickness=2, font=ENTRY_FONT)
        self.sr_entry.grid(row=1, column=1, padx=5)

        # Number Entry - Number of results
        sr_num_label = tk.Label(self, text="Enter number of results (optional): ", font=LABEL_FONT, bg="Black",
                                fg="White")
        sr_num_label.grid(row=2, column=0, padx=5)
        self.sr_num_entry = tk.Entry(self, width=40, highlightthickness=2, font=ENTRY_FONT)
        self.sr_num_entry.grid(row=2, column=1, padx=5)

        # Button
        sr_button = tk.Button(self, text="Search Recipes", command=self.search_recipes_button, font=LABEL_FONT)
        sr_button.grid(row=1, column=2, padx=10)

        # Recipe instructions button
        fetch_button = tk.Button(self, text="Get Instructions", font=ENTRY_FONT, command=instructions_window)
        fetch_button.grid(row=2, column=2, pady=5)

        # Text widget for displaying results
        self.results_text = tk.Text(self, height=20, width=60, state=tk.DISABLED, borderwidth=2, wrap=tk.WORD,
                                    font=ENTRY_FONT)
        self.results_text.grid(row=3, column=1, columnspan=3, padx=10, pady=10, sticky='nsew')

        # Vertical Scrollbar
        scrollbar = tk.Scrollbar(self, command=self.results_text.yview)
        scrollbar.grid(row=3, column=3, sticky="nsew")
        self.results_text.config(yscrollcommand=scrollbar.set)

        self.image_canvas = tk.Canvas(self, width=100, height=100)
        self.image_canvas.grid(row=3, column=0, padx=0, pady=10, sticky='nsew')

    def back_to_main_menu(self):
        from frames.main_menu_frame import MainMenu
        self.controller.show_frame(MainMenu)

    def search_recipes_button(self):
        try:
            # print("Search_recipes_button called")
            search_params = self.sr_entry.get()
            # Get user input for the number of results (optional)
            number_str = self.sr_num_entry.get()
            # Check if the user provided a valid number or left it blank
            if number_str.strip().isdigit():
                number = int(number_str)
            else:
                number = None  # Use the default value from the API

            recipes = search_recipes(search_params=search_params, number=number)

            display_recipes(recipes=recipes, text_widget=self.results_text, canvas_widget=self.image_canvas)
        except Exception as e:
            print("Error: ", e)

        self.controller.update()
