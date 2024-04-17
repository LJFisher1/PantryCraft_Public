import os
import tkinter as tk
from tkcalendar import Calendar
from datetime import datetime
from config import HEADER_FONT, ENTRY_FONT


class MealPlanner(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.meals = {}  # Dictionary for the meals

        # Path for data directory
        self.date_dir = "date"
        # Create the directory if it doesn't exist
        os.makedirs(self.date_dir, exist_ok=True)
        # Define a path to meal file
        self.meals_file = "meals.txt"

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

        # Save meal button
        save_button = tk.Button(self, text="Save Meals", command=self.save_meal)
        save_button.grid(row=1, column=2, pady=10, padx=10, sticky="w")

        from .main_menu_frame import MainMenu

        back_button = tk.Button(self, text="Back to Main Menu", command=lambda: controller.show_frame(MainMenu))
        back_button.grid(row=0, column=1, pady=5, sticky='e')

        # Load meals from file
        self.load_meals_from_file()

        # Update the calendar to display the meals
        self.retrieve_meals()

        # Bind event to retrieve meals when date changes
        self.calendar.bind("<<CalendarSelected>>", self.retrieve_meals)  # Bind to retrieve meals when date changes

    # Add meal function
    def add_meal_to_date(self, date, meal):
        if date not in self.meals:
            self.meals[date] = []
        self.meals[date].append(meal)
        # print(f"Added meal '{meal}' to date '{date}'")  # Debug print

    # Retrieve meals
    def get_meals_for_date(self, date):
        return self.meals.get(date, [])

    def retrieve_meals(self, event=None):
        selected_date = self.calendar.get_date()
        selected_date = datetime.strptime(selected_date, "%m/%d/%y").strftime("%m/%d/%Y")  # Convert date format
        # print("(RM)Selected Date:", selected_date)  # Debug print
        meals_for_date = self.get_meals_for_date(selected_date)
        # print("(RM)Meals for Date:", meals_for_date)  # Debug print
        # print("(RM)All Dates in Meals: ", list(self.meals.keys()))
        self.meal_entry.delete("1.0", tk.END)  # Clear the text box
        for meal in meals_for_date:
            self.meal_entry.insert(tk.END, meal + "\n")
            self.update()

    def save_meal(self):
        meal = self.meal_entry.get("1.0", tk.END).strip()
        selected_date = self.calendar.get_date()
        formatted_date = datetime.strptime(selected_date, "%m/%d/%y").strftime("%m/%d/%Y")
        if meal:
            self.add_meal_to_date(formatted_date, meal)
            self.save_meals_to_file()
        self.meal_entry.delete("1.0", tk.END)  # Clear the text box

    def save_meals_to_file(self):
        try:
            # print("Saving meals to file:", self.meals_file)  # Debug print
            with open(self.meals_file, "w") as file:  # Open file in write mode (clears existing content)
                for date, meals in self.meals.items():
                    for meal in meals:
                        file.write(f"{date}\n{meal}\n")
        except Exception as e:
            print("Error saving meals to file:", e)

    def load_meals_from_file(self):
        try:
            with open(self.meals_file, "r") as file:
                current_date = None
                current_meals = []
                for line in file:
                    line = line.strip()
                    if not line:
                        continue
                    # print("Reading line:", line)  # Debug print
                    try:
                        if '/' in line and len(line.split('/')) == 3:  # Check if the line is in the correct format
                            if current_date is not None:
                                if current_date not in self.meals:
                                    self.meals[current_date] = current_meals
                                    # print("Loaded meals for date:", current_date)  # Debug print
                                    # print("Meals:", current_meals)  # Debug print
                                current_meals = []
                            current_date = datetime.strptime(line, "%m/%d/%Y").strftime("%m/%d/%Y")
                        else:
                            current_meals.append(line)
                    except Exception as e:
                        print("Error parsing line:", line)
                        print("Error details:", e)
                if current_date is not None:
                    if current_date not in self.meals:
                        self.meals[current_date] = current_meals
                        # print("Loaded meals for date:", current_date)  # Debug print
                        # print("Meals:", current_meals)  # Debug print
        except FileNotFoundError:
            print("Error: File Not Found")
        except Exception as e:
            print("Error loading meals from file:", e)
