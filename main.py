import random
import tkinter as tk
from tkinter import ttk

# Initialize variables
heads = 0
tails = 0
results = []

# Define function to simulate coin flips
def flip_coin():
    global heads, tails, results
    num_flips = int(num_flips_entry.get())
    for i in range(num_flips):
        flip = random.randint(0, 1)
        if flip == 0:
            tails += 1
        else:
            heads += 1
        results.append((heads, tails))

    # Update the results label
    results_label.config(text=f"Heads: {heads}\nTails: {tails}")

    # Clear previous plot and create new one
    canvas.delete("all")
    canvas.create_rectangle(0, 0, 200, 200, fill="#FFFFFF", outline="")
    canvas.create_text(50, 180, text="Heads")
    canvas.create_text(150, 180, text="Tails")
    canvas.create_rectangle(50, 170, 90, 170 - heads*10, fill="#FF0000", outline="")
    canvas.create_rectangle(150, 170, 190, 170 - tails*10, fill="#0000FF", outline="")
    canvas.update()

# Set up the main window
root = tk.Tk()
root.title("Virtual Coin Flipper")
root.geometry("300x400")

# Set up the widgets
num_flips_label = ttk.Label(root, text="Number of Flips:")
num_flips_label.pack(pady=10)
num_flips_entry = ttk.Entry(root)
num_flips_entry.pack(pady=10)
flip_button = ttk.Button(root, text="Flip Coin", command=flip_coin)
flip_button.pack(pady=10)
results_label = ttk.Label(root, text="Heads: 0\nTails: 0")
results_label.pack(pady=10)
canvas = tk.Canvas(root, width=200, height=200)
canvas.pack(pady=10)

# Start the main loop
root.mainloop()
