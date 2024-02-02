import tkinter as tk
from config import HEADER_FONT


class SearchByIngredient(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="Search by Ingredient", font=HEADER_FONT)
        label.grid(row=0, column=0, pady=10, padx=10)

        from frames.main_menu_frame import MainMenu

        back_button = tk.Button(self, text="Back to Main Menu", command=lambda: controller.show_frame(MainMenu))
        back_button.grid(row=0, column=2, pady=5)
