import tkinter as tk
from battleships import *

def on_shoot():
    global current_fleet  # a fleet which is created by calling randomly_place_all_ships
    global shots  # counts the number of shots. Initialized to 0

    current_row = int(row_entry.get())
    current_column = int(col_entry.get())
    row_entry.delete(0, "end")
    col_entry.delete(0, "end")
    shots += 1
    print(current_row, current_column, shots)


# sets up window and frames
root = tk.Tk()
root.title("Battleships")
root.geometry("800x800")

results_frame = tk.Frame(root)
board_frame = tk.Frame(root)
controls_frame = tk.Frame(root)

results_frame.grid(row=1, sticky="nsew")
board_frame.grid(row=2, sticky="nsew")
controls_frame.grid(row=3, sticky="nsew")

# widgets for board_frame
# sets up the board
board = {}
for r in range(0, 11):
   for c in range(0, 11):
       if r == 0 and c == 0:
           continue
       elif r == 0:
           tk.Label(board_frame, text=str(c-1)).grid(row=r, column=c, pady=5)
       elif c == 0:
           tk.Label(board_frame, text=str(r-1)).grid(row=r, column=c, padx=(50, 5))
       else:
           board_canvas = tk.Canvas(board_frame, bg="lightblue", height=40, width=40)
           board_canvas.grid(row=r, column=c)
           board[(r-1, c-1)] = board_canvas

# widgets for controls frame
# label headings for user entry boxes
row_lab = tk.Label(controls_frame, text="Enter row", fg="royalblue4", font=("helvetica", 18))
col_lab = tk.Label(controls_frame, text="Enter column", fg="royalblue4", font=("helvetica", 18))
row_lab.grid(row=0, column=0, padx=(180,20), pady=(20,0))
col_lab.grid(row=0, column=1, pady=(20,0))

# entry widgets for user to input co-ordinates
row_entry = tk.Entry(controls_frame, width=10)
col_entry = tk.Entry(controls_frame, width=10)
row_entry.grid(row=1, column=0, padx=(180,20), pady=10)
col_entry.grid(row=1, column=1, pady=10)

# button to click 'shoot' and bind to on_shoot function
shoot_button = tk.Button(controls_frame, text="Shoot", font=("helvetica", 16, "bold"), command=on_shoot)
shoot_button.grid(row=1, column=2, padx=20, pady=10)

current_fleet = randomly_place_all_ships()
shots = 0

root.mainloop()