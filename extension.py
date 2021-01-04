import tkinter as tk
from battleships import *

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

root.mainloop()