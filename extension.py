import tkinter as tk
from battleships import *

def on_shoot():
    global current_fleet  # a fleet which is created by calling randomly_place_all_ships
    global shots  # counts the number of shots. Initialized to 0

    # gets the row and column inputs and then clears the fields; increments number of shots and displays the
    # updated number; clears any previous error messages
    try:
        current_row = int(row_entry.get())
        current_column = int(col_entry.get())
        row_entry.delete(0, "end")
        col_entry.delete(0, "end")
        shots += 1
        shots_lab.config(text=shots)
        error_lab.config(text="")

        # checks if given square results in hit, display message and change given square on board to red if so
        if check_if_hits(current_row, current_column, current_fleet):
            is_hit_lab.config(text="You have a hit!", fg="seagreen", font=("helvetica", 28))
            sunk_lab.config(text="")
            board[current_row, current_column].config(bg="red")
            (current_fleet, ship_hit) = hit(current_row, current_column, current_fleet)

            # checks if given square results in ship being sunk, display message and change text in given square to
            # first letter of ship type if so
            if is_sunk(ship_hit):
                sunk_lab.config(text="You sank a " + ship_type(ship_hit) + "!", fg="blue2", font=("helvetica", 28))
                if ship_type(ship_hit) == "submarine":
                    board[current_row, current_column].create_text(22, 22, text="S")
                elif ship_type(ship_hit) == "destroyer":
                    for square in ship_hit[4]:
                        board[square[0], square[1]].create_text(22, 22, text="D")
                elif ship_type(ship_hit) == "cruiser":
                    for square in ship_hit[4]:
                        board[square[0], square[1]].create_text(22, 22, text="C")
                else:
                    for square in ship_hit[4]:
                        board[square[0], square[1]].create_text(22, 22, text="B")

        # displays miss message and changes given square on board to grey
        else:
            is_hit_lab.config(text="You missed!", fg="red4", font=("helvetica", 28))
            sunk_lab.config(text="")
            board[current_row, current_column].config(bg="darkgrey")

    # exception handling for shoot button being clicked before row and/or integer values are entered
    except NameError:
        error_lab.config(text="Enter row and column values (between 0 and 9) first", font=("helvetica", 18))
        is_hit_lab.config(text="")
        sunk_lab.config(text="")
        game_over_lab.config(text="")

    # exception handling for integer inputs greater than 9 i.e squares not on the board
    except KeyError:
        error_lab.config(text="Enter numbers between 0 and 9", font=("helvetica", 18))
        is_hit_lab.config(text="")
        sunk_lab.config(text="")
        game_over_lab.config(text="")

    # exception handling for invalid input i.e. non integers
    except ValueError:
        error_lab.config(text="Enter numbers between 0 and 9", font=("helvetica", 18))
        is_hit_lab.config(text="")
        sunk_lab.config(text="")

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

# widgets for results_frame
# labels for keeping track of the number of shots
shots_heading_lab = tk.Label(results_frame, text="Number of shots", font=("helvetica", 16))
shots_lab = tk.Label(results_frame, text="", height=3, width=6, borderwidth=2, relief="solid")

shots_heading_lab.grid(row=0, column=0, padx=30, pady=(10,0))
shots_lab.grid(row=1, column=0, padx=30, pady=10)

# label to tell user result of their input
is_hit_lab = tk.Label(results_frame, text="")
is_hit_lab.grid(row=1, column=1, padx=10, pady=10)

# label to tell user result when a ship is sunk
sunk_lab = tk.Label(results_frame, text="")
sunk_lab.grid(row=1, column=2, padx=10, pady=10)

# labels to tell user result when game ends
game_over_lab = tk.Label(results_frame, text="")
shots_req_lab = tk.Label(results_frame, text="")
game_over_lab.grid(row=0, column=1, padx=(10,0), pady=10)
shots_req_lab.grid(row=0, column=2, pady=10)

# label to print error messages on invalid input
error_lab = tk.Label(results_frame, text="")
error_lab.grid(row=1, column=4, padx=10, pady=10)

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