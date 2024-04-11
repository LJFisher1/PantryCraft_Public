import tkinter as tk
from config import HEADER_FONT, LABEL_FONT, ENTRY_FONT


class PantryInventory(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="blue")
        self.controller = controller

        self.pantry_inventory = "pantry_inventory.txt"

        # Title
        label = tk.Label(self, text="Pantry Inventory", font=HEADER_FONT)
        label.grid(row=0, column=0, columnspan=4, pady=10, padx=10)

        # Inventory
        self.inventory_text = tk.Text(self, height=20, width=60, wrap=tk.WORD, state=tk.DISABLED, font=ENTRY_FONT)
        self.inventory_text.grid(row=1, column=0, padx=10, pady=10, columnspan=3, rowspan=6, sticky='nsew')

        # Item entry box
        ie_label = tk.Label(self, text="Enter an item: ", font=LABEL_FONT)
        ie_label.grid(row=1, column=3, padx=5, pady=(5, 0))
        self.item_entry = tk.Entry(self, width=30, highlightthickness=2, font=ENTRY_FONT)
        self.item_entry.grid(row=2, column=3, padx=10, pady=10)

        # Entry box for quantity
        qty_label = tk.Label(self, text="Enter a quantity: ", font=LABEL_FONT)
        qty_label.grid(row=3, column=3, padx=5, pady=(5, 0))
        self.qty_entry = tk.Entry(self, width=30, highlightthickness=2, font=ENTRY_FONT)
        self.qty_entry.grid(row=4, column=3, padx=10, pady=5)

        # Button to add items
        add_button = tk.Button(self, text="Add Item", highlightthickness=2, command=self.add_item, font=LABEL_FONT)
        add_button.grid(row=5, column=3, pady=10)
        from .main_menu_frame import MainMenu

        # Main menu button
        back_button = tk.Button(self, text="Back to Main Menu", command=lambda: controller.show_frame(MainMenu),
                                font=LABEL_FONT)
        back_button.grid(row=0, column=3, pady=5)

        self.load_items()

    def add_item(self):
        new_item = self.item_entry.get()
        quantity = self.qty_entry.get()

        if new_item:
            try:
                quantity = int(quantity)
            except ValueError:
                quantity = 1

            item_with_quantity = f"{new_item} (Qty: {quantity})"
            self.inventory_text.config(state=tk.NORMAL)
            self.inventory_text.insert(tk.END, f"{item_with_quantity}\n")
            self.inventory_text.config(state=tk.DISABLED)

            with open(self.pantry_inventory, "a") as file:
                file.write(f"{new_item}, {quantity}\n")

            self.item_entry.delete(0, tk.END)
            self.qty_entry.delete(0, tk.END)

    def load_items(self):
        self.inventory_text.config(state=tk.NORMAL)
        self.inventory_text.delete(1.0, tk.END)
        self.inventory_text.config(state=tk.DISABLED)

        # Load items from the file and into the display box
        try:
            with open(self.pantry_inventory, "r") as file:
                for line in file:
                    item, quantity = line.strip().split(",")
                    item_with_quantity = f"{item} (Qty: {quantity})"
                    self.inventory_text.config(state=tk.NORMAL)
                    self.inventory_text.insert(tk.END, f"{item_with_quantity}\n")
                    self.inventory_text.config(state=tk.DISABLED)
        # No items to load if there is no file
        except FileNotFoundError:
            pass
