import tkinter as tk
from frames.main_menu_frame import MainMenu
from frames.meal_planner_frame import MealPlanner
from frames.search_by_ingredient_frame import SearchByIngredient
from frames.shopping_list_frame import ShoppingList
from frames.pantry_inventory_frame import PantryInventory
from frames.search_recipes_frame import SearchRecipes
from frames.create_with_pantry_frame import CreateWithPantry

FRAMES_LIST = (
    MainMenu, MealPlanner, SearchByIngredient, ShoppingList, PantryInventory, SearchRecipes, CreateWithPantry
)


class PantryCraft(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # Set custom window size
        window_width = 1440
        window_height = 915
        self.geometry(f"{window_width}x{window_height}")

        container = tk.Frame(self)
        container.pack(fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in FRAMES_LIST:
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(MainMenu)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


if __name__ == "__main__":
    app = PantryCraft()
    app.title("PantryCraft")
    app.geometry("1440x915")
    app.mainloop()
