import os
import tkinter as tk
from tkcalendar import Calendar
from config import HEADER_FONT, ENTRY_FONT


class MealPlanner(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.meals = {}  # Dictionary for the meals

        # Path for data directory
        self.date_dir = "data"
        # Create the directory if it doesn't exist
        os.makedirs(self.date_dir, exist_ok=True)
        # Define a path to meal file
        self.meals_file = os.path.join(self.date_dir, "Meals.txt")

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

        # Pre-fill meal entry with headings
        # self.pre_fill_meal_entry()

        # Save meal button
        save_button = tk.Button(self, text="Save Meals", command=self.save_meal)
        save_button.grid(row=1, column=2, pady=10, padx=10, sticky="w")

        from .main_menu_frame import MainMenu

        back_button = tk.Button(self, text="Back to Main Menu", command=lambda: controller.show_frame(MainMenu))
        back_button.grid(row=0, column=1, pady=5, sticky='e')

        # Bind event to retrieve meals when date changes
        self.calendar.bind("<<CalendarSelected>>", self.retrieve_meals)  # Bind to retrieve meals when date changes

        # Load meals from file
        self.load_meals_from_file()

    # Add meal function
    def add_meal_to_date(self, date, meal):
        if date not in self.meals:
            self.meals[date] = []
        self.meals[date].append(meal)

    # # Pre-fill meal entry with headings
    # def pre_fill_meal_entry(self):
    #     default_text = "\n\n\n".join(["{}:".format(meal_type) for meal_type in ["Breakfast", "Lunch", "Dinner"]])
    #     self.meal_entry.insert(tk.END, default_text)

    # Retrieve meals
    def get_meals_for_date(self, date):
        return self.meals.get(date, [])

    def retrieve_meals(self, event=None):
        selected_date = self.calendar.get_date()
        # print("Selected Date:", selected_date)  # Debug print
        meals_for_date = self.get_meals_for_date(selected_date)
        # print("Meals for Date:", meals_for_date)  # Debug print
        # self.meal_entry.delete("1.0", tk.END)  # Clear the text box
        for meal in meals_for_date:
            self.meal_entry.insert(tk.END, meal + "\n")

    def save_meal(self):
        meal = self.meal_entry.get("1.0", tk.END).strip()
        selected_date = self.calendar.get_date()
        if meal:
            self.add_meal_to_date(selected_date, meal)
            self.save_meals_to_file()
            self.retrieve_meals()

    def save_meals_to_file(self):
        try:
            print("Saving meals to file:", self.meals_file)  # Debug print
            with open("meals.txt", "a") as file:
                for date, meals in self.meals.items():
                    file.write(date + "\n")
                    for meal in meals:
                        file.write(meal + "\n")
                    file.write("\n")
        except Exception as e:
            print("Error saving meals to file:", e)

    # def load_meals_from_file(self):
    #     try:
    #         with open(self.meals_file, "r") as file:
    #             lines = file.readlines()
    #             date = None
    #             meals = []
    #             for line in lines:
    #                 line = line.strip()
    #                 if not line:  # empty line indicates an end of meals for the date
    #                     if date and meals:
    #                         self.meals[date] = meals
    #                         date = None
    #                         meals = []
    #                 elif ":" in line:
    #                     date = line.rstrip(":")
    #                 elif date:
    #                     date = line
    #                 else:
    #                     meals.append(line)
    #             if date and meals:
    #                 self.meals[date] = meals
    #     except FileNotFoundError:
    #         pass
    #     except Exception as e:
    #         print("Error loading meals from file: ", e)
    def load_meals_from_file(self):
        try:
            with open(self.meals_file, "r") as file:
                date = None
                for line in file:
                    line = line.strip()
                    if ":" in line:
                        date = line.rstrip(":")
                        if date not in self.meals:
                            self.meals[date] = []
                    elif date:
                        self.meals[date].append(line)
        except FileNotFoundError:
            pass  # If file doesn't exist, ignore and start with empty meals dictionary
        except Exception as e:
            print("Error loading meals from file:", e)
