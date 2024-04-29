import tkinter as tk
from config import HEADER_FONT, LABEL_FONT, ENTRY_FONT
from recipes_search import load_background_image


class ShoppingList(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="Black")
        self.controller = controller

        # Load background image
        background_image = load_background_image("background_images/Shopping List.png")
        if background_image:
            # Create a label to hold the image
            self.background_label = tk.Label(self, image=background_image)
            self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
            self.background_label.image = background_image  # To keep a reference

        label = tk.Label(self, text="Shopping List", font=HEADER_FONT, bg="Black", fg="White")
        label.grid(row=0, column=0, pady=10, padx=10, columnspan=3)

        # Text Widget to display shopping list
        self.shopping_list_text = tk.Text(self, font=ENTRY_FONT, height=10, width=30)
        self.shopping_list_text.grid(row=2, column=0, pady=5, padx=10, sticky="nsew")
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Entry field for new items
        self.new_item_entry = tk.Entry(self, font=ENTRY_FONT, fg="grey")
        self.new_item_entry.grid(row=1, column=0, padx=10, sticky='ew')
        self.new_item_entry.insert(0, "Enter an item")
        self.new_item_entry.bind("<FocusIn>", self.clear_entry)
        self.new_item_entry.bind("<FocusOut>", self.restore_entry)
        self.grid_columnconfigure(0, weight=1)

        # Button to add new items
        add_button = tk.Button(self, text="Add to list", command=self.add_to_list, font=LABEL_FONT)
        add_button.grid(row=1, column=1, pady=15, padx=(0, 10))

        # Button to remove completed items
        remove_button = tk.Button(self, text="Remove completed items", command=self.remove_completed_items,
                                  font=LABEL_FONT)
        remove_button.grid(row=2, column=1, pady=5, padx=10)
        from .main_menu_frame import MainMenu

        back_button = tk.Button(self, text="Back to Main Menu", font=ENTRY_FONT,
                                command=lambda: controller.show_frame(MainMenu))
        back_button.grid(row=0, column=1, pady=5)

        # Bind mouse clicks to the text widget
        self.shopping_list_text.bind("<Button-1>", self.on_text_click)

        # Load shopping list
        self.load_shopping_list()

    def add_to_list(self):
        # Get the text from the entry field
        new_item = self.new_item_entry.get()

        # Add item to listbox
        self.shopping_list_text.insert(tk.END, f" [] {new_item}\n")

        # Clear the entry field
        self.new_item_entry.delete(0, tk.END)

    def on_text_click(self, event):
        # Get the index of the clicked character
        index = self.shopping_list_text.index("@%d,%d" % (event.x, event.y))
        # print(f"{index} index")

        # Get the line containing the clicked character
        line_start_index = self.shopping_list_text.index(f"{index} linestart")
        line_end_index = self.shopping_list_text.index(f"{index} lineend")

        # Get the content of the clicked line
        line_content = self.shopping_list_text.get(line_start_index, line_end_index)

        x_index = line_content.find("X")

        if x_index != -1:
            x_index = float(x_index)
            x_abs_index = float(line_start_index) + round((x_index / 10), 2)
            self.shopping_list_text.delete(x_abs_index)

        else:
            # If "X" is not present, insert it after the checkbox
            checkbox_index = line_content.find("[")
            if checkbox_index != -1:
                self.shopping_list_text.insert(f"{line_start_index} + {checkbox_index + 1}c", "X")

        self.save_shopping_list()

    def save_shopping_list(self):
        with open("shopping_list.txt", "w") as file:
            shopping_list_content = self.shopping_list_text.get("1.0", tk.END)
            file.write(shopping_list_content)

    def load_shopping_list(self):
        try:
            with open("shopping_list.txt", "r") as file:
                shopping_list_content = file.read()
                self.shopping_list_text.insert(tk.END, shopping_list_content)
        except FileNotFoundError:
            print("Shopping list file not found.")

    def remove_completed_items(self):
        lines = self.shopping_list_text.get("1.0", tk.END).split("\n")
        updated_items = [line for line in lines if "[X]" not in line and line.strip()]
        updated_content = "\n".join(updated_items)
        self.shopping_list_text.delete("1.0", tk.END)
        self.shopping_list_text.insert("1.0", updated_content)

        # Save to file
        self.save_shopping_list()

    def clear_entry(self, event):
        if self.new_item_entry.get() == "Enter an item":
            self.new_item_entry.delete(0, tk.END)
            self.new_item_entry.config(fg="black")

    def restore_entry(self, event):
        if not self.new_item_entry.get():
            self.new_item_entry.insert(0, "Enter an item")
            self.new_item_entry.config(fg="grey")
