import tkinter as tk
from tkinter import ttk, messagebox

from config import HEADER_FONT, LABEL_FONT, ENTRY_FONT


class PantryInventory(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="Black")
        self.controller = controller

        self.pantry_inventory = "pantry_inventory.txt"

        # Title
        label = tk.Label(self, text="Pantry Inventory", font=HEADER_FONT, bg="Black", fg="White")
        label.grid(row=0, column=0, columnspan=4, pady=10, padx=10)

        # Inventory
        self.inventory_frame = tk.Frame(self)
        self.inventory_frame.grid(row=1, column=0, columnspan=3, rowspan=6, sticky='nsew', padx=(0, 10))

        self.inventory_text = tk.Text(self, height=20, width=60, wrap=tk.WORD, state=tk.DISABLED, font=ENTRY_FONT)
        self.inventory_text.grid(row=1, column=0, padx=10, pady=10, columnspan=3, rowspan=6, sticky='nsew')
        self.grid_columnconfigure(0, weight=1)
        self.inventory_frame.grid_rowconfigure(0, weight=1)  # Allow the frame to expand vertically

        # Scrollbar for inventory text box
        self.inventory_scrollbar = ttk.Scrollbar(self.inventory_frame, orient='vertical',
                                                 command=self.inventory_text.yview)
        self.inventory_scrollbar.grid(row=0, column=0, sticky='ns', padx=(0, 10))
        self.inventory_scrollbar.lift()
        self.inventory_text.config(yscrollcommand=self.inventory_scrollbar.set)

        # Item entry box
        ie_label = tk.Label(self, text="Enter an item: ", font=LABEL_FONT, bg="Black", fg="White")
        ie_label.grid(row=1, column=3, padx=5, pady=(5, 0))
        self.item_entry = tk.Entry(self, width=30, highlightthickness=2, font=ENTRY_FONT)
        self.item_entry.grid(row=2, column=3, padx=10, pady=10)

        # Entry box for quantity
        qty_label = tk.Label(self, text="Enter a quantity: ", font=LABEL_FONT, bg="Black", fg="White")
        qty_label.grid(row=3, column=3, padx=5, pady=(5, 0))
        self.qty_entry = tk.Entry(self, width=30, highlightthickness=2, font=ENTRY_FONT)
        self.qty_entry.grid(row=4, column=3, padx=10, pady=5)

        # Button to add items
        add_button = tk.Button(self, text="Add Item", highlightthickness=2, command=self.add_item, font=LABEL_FONT)
        add_button.grid(row=5, column=3, pady=10)
        from .main_menu_frame import MainMenu

        # Button to remove items
        remove_button = tk.Button(self, text="Remove Item", highlightthickness=2, command=self.remove_item,
                                  font=LABEL_FONT)
        remove_button.grid(row=6, column=3, pady=(0, 10))

        # Main menu button
        back_button = tk.Button(self, text="Back to Main Menu", command=lambda: controller.show_frame(MainMenu),
                                font=LABEL_FONT)
        back_button.grid(row=0, column=3, pady=5)

        self.load_items()

    def add_item(self):
        new_item = self.item_entry.get().strip()
        quantity = self.qty_entry.get().strip()

        if new_item and quantity:
            try:
                quantity = int(quantity)
                if quantity <= 0:
                    raise ValueError("Quantity must be a positive integer")
            except ValueError:
                messagebox.showerror("Error", "Quantity must be a positive integer")
                return

            # Get all text from the widget
            all_text = self.inventory_text.get("1.0", "end").strip()
            # Split the text into lines
            lines = all_text.split("\n")

            updated_text = ""
            found = False
            for i, line in enumerate(lines):
                parts = line.split(", ")
                if len(parts) == 2:
                    item, old_quantity = parts
                    if item.lower() == new_item.lower():
                        old_quantity = int(old_quantity)
                        old_quantity += quantity  # Increment the quantity
                        lines[i] = f"{item}, {old_quantity}"
                        found = True
                        break

            if not found:
                lines.append(f"{new_item}, {quantity}")

            updated_text = "\n".join(lines)

            # Clear the text widget
            self.inventory_text.config(state=tk.NORMAL)
            self.inventory_text.delete("1.0", "end")
            # Insert the updated text into the widget
            self.inventory_text.insert("1.0", updated_text)
            self.inventory_text.config(state=tk.DISABLED)

            # Update the inventory file
            with open(self.pantry_inventory, "w") as file:
                file.write(updated_text)

            self.item_entry.delete(0, tk.END)
            self.qty_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please enter both item and quantity")

    def remove_item(self):
        item_to_remove = self.item_entry.get().strip()
        quantity_to_remove = int(self.qty_entry.get().strip()) if self.qty_entry.get().strip() else 1

        if item_to_remove:
            # Get all text from the widget
            all_text = self.inventory_text.get("1.0", "end").strip()
            # Split the text into lines
            lines = all_text.split("\n")

            new_lines = []
            updated_text = ""
            removed = False
            for line in lines:
                parts = line.split(", ")
                if len(parts) == 2:
                    item, quantity = parts
                    quantity = int(quantity)
                    if item.lower() == item_to_remove.lower():
                        quantity -= quantity_to_remove
                        if quantity > 0:
                            new_lines.append(f"{item}, {quantity}")
                        removed = True
                    else:
                        new_lines.append(line)
                else:
                    new_lines.append(line)

            if removed:
                updated_text = "\n".join(new_lines)

                # Clear the text widget
                self.inventory_text.config(state=tk.NORMAL)
                self.inventory_text.delete("1.0", tk.END)
                # Insert the updated text into the widget
                self.inventory_text.insert("1.0", updated_text)
                self.inventory_text.config(state=tk.DISABLED)

                # Update the inventory file
                with open(self.pantry_inventory, "w") as file:
                    file.write(updated_text)
            else:
                messagebox.showinfo("Item not found", "Item not found in the inventory.")
        else:
            messagebox.showinfo("No Item Entered", "Please enter an item to remove.")

    def load_items(self):
        self.inventory_text.config(state=tk.NORMAL)
        self.inventory_text.delete("1.0", "end")

        # Load items from the file and into the display box
        try:
            with open(self.pantry_inventory, "r") as file:
                for line in file:
                    self.inventory_text.insert(tk.END, line)
        # No items to load if there is no file
        except FileNotFoundError:
            pass

        self.inventory_text.config(state=tk.DISABLED)
