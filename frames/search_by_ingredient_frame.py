import tkinter as tk
from config import HEADER_FONT, LABEL_FONT, ENTRY_FONT
from search_by_ingredient import search_by_ingredient


class SearchByIngredient(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Title
        label = tk.Label(self, text="Search by Ingredient", font=HEADER_FONT)
        label.grid(row=0, column=0, columnspan=4, pady=10, padx=10)

        # Ingredient entry
        ie_label_one = tk.Label(self, text="Enter first ingredient: ", font=LABEL_FONT)
        ie_label_one.grid(row=1, column=0, padx=5, pady=(5, 0))
        self.item_entry_one = tk.Entry(self, width=10, highlightthickness=2, font=ENTRY_FONT)
        self.item_entry_one.grid(row=1, column=1, padx=10, pady=5)

        ie_label_two = tk.Label(self, text="Enter second ingredient: ", font=LABEL_FONT)
        ie_label_two.grid(row=2, column=0, padx=5, pady=(5, 0))
        self.item_entry_two = tk.Entry(self, width=10, highlightthickness=2, font=ENTRY_FONT)
        self.item_entry_two.grid(row=2, column=1, padx=10, pady=5)

        ie_label_three = tk.Label(self, text="Enter third ingredient: ", font=LABEL_FONT)
        ie_label_three.grid(row=3, column=0, padx=5, pady=(5, 0))
        self.item_entry_three = tk.Entry(self, width=10, highlightthickness=2, font=ENTRY_FONT)
        self.item_entry_three.grid(row=3, column=1, padx=10, pady=10)

        ie_label_four = tk.Label(self, text="Enter fourth ingredient: ", font=LABEL_FONT)
        ie_label_four.grid(row=4, column=0, padx=5, pady=(5, 0))
        self.item_entry_four = tk.Entry(self, width=10, highlightthickness=2, font=ENTRY_FONT)
        self.item_entry_four.grid(row=4, column=1, padx=10, pady=10)

        # Search Button
        sr_button = tk.Button(self, text="Search", command=search_by_ingredient(), font=LABEL_FONT)
        sr_button.grid(row=6, column=1, padx=10)

        # Results window
        self.results_text = tk.Text(self, height=20, width=40, state=tk.DISABLED, borderwidth=1, wrap=tk.WORD,
                                    font=ENTRY_FONT)
        self.results_text.grid(row=1, column=3, rowspan=4, sticky='nse')

        from frames.main_menu_frame import MainMenu

        back_button = tk.Button(self, text="Back to Main Menu", command=lambda: controller.show_frame(MainMenu))
        back_button.grid(row=0, column=4, pady=5)
