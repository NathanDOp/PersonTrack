# Name: Nathan D'Agostino
# Date: 6/20/2023
# Desc: This is gross and with the power of fuck me I did it. This is ineffective and OVERLY reliant
#       on the user not putting in letters but I do what it do.

import sys
import tkinter as tk
from tkinter import messagebox

def get_user_input(): # User do shit here
    global name_entry, height_entry, weight_entry
    name = name_entry.get()
    height = float(height_entry.get())
    weight = float(weight_entry.get())
    return name, height, weight

def store_data(): # Store funny number
    name, height, weight = get_user_input()
    with open("user_data.txt", "a") as file:
        file.write(f"Name: {name}, Height: {height}, Weight: {weight}\n")
    messagebox.showinfo("Success", "Data saved successfully!")
    name_entry.delete(0, tk.END)
    height_entry.delete(0, tk.END)
    weight_entry.delete(0, tk.END)

def display_data(): # Application Unga Bunga
    try:
        with open("user_data.txt", "r") as file:
            data = file.read()
            if data:
                messagebox.showinfo("Data", data)
            else:
                messagebox.showinfo("Data", "No data found.")
    except FileNotFoundError:
        messagebox.showerror("Error", "File not found.")

def main(): # Google saved me I won't lie.
    root = tk.Tk()
    root.title("User Data App")

    name_label = tk.Label(root, text="Name:")
    name_label.grid(row=0, column=0, padx=10, pady=10)
    global name_entry
    name_entry = tk.Entry(root)
    name_entry.grid(row=0, column=1, padx=10, pady=10)

    height_label = tk.Label(root, text="Height (m):")
    height_label.grid(row=1, column=0, padx=10, pady=10)
    global height_entry
    height_entry = tk.Entry(root)
    height_entry.grid(row=1, column=1, padx=10, pady=10)

    weight_label = tk.Label(root, text="Weight (kg):")
    weight_label.grid(row=2, column=0, padx=10, pady=10)
    global weight_entry
    weight_entry = tk.Entry(root)
    weight_entry.grid(row=2, column=1, padx=10, pady=10)

    save_button = tk.Button(root, text="Save Data", command=store_data)
    save_button.grid(row=3, column=0, padx=10, pady=10)

    display_button = tk.Button(root, text="Display Data", command=display_data)
    display_button.grid(row=3, column=1, padx=10, pady=10)

    root.mainloop()
# Id note more but I dont care for 5 pts off ngl.
if __name__ == "__main__":
    main()