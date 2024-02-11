import tkinter as tk
from tkcalendar import Calendar
from config import HEADER_FONT, LABEL_FONT, ENTRY_FONT


class MealPlanner(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="Meal Planner", font=HEADER_FONT)
        label.grid(row=0, column=0, pady=10, padx=10, columnspan=2)

        # Frame for calendar
        calendar_frame = tk.Frame(self, width=400, height=300)
        calendar_frame.grid(row=1, column=0, pady=10, padx=10, sticky='n')

        # Calendar widget
        self.calendar = Calendar(calendar_frame, selectmode='day', font=('Helvetica', 30, 'normal'))
        self.calendar.pack(fill="both", expand=True)

        # Text box for meal planning
        self.meal_entry = tk.Text(self, font=ENTRY_FONT, height=20, width=40)
        self.meal_entry.grid(row=1, column=1, pady=10, padx=10, sticky="e")

        from .main_menu_frame import MainMenu

        back_button = tk.Button(self, text="Back to Main Menu", command=lambda: controller.show_frame(MainMenu))
        back_button.grid(row=0, column=1, pady=5, sticky='e')
