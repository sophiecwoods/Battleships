#see the readme.md file for description and data 

def is_sunk(ship):
    """returns Boolean value, which is True if ship is sunk and False otherwise"""
    row_pos = ship[0]
    col_pos = ship[1]
    horizontal = ship[2]
    ship_length = ship[3]
    hits = ship[4]
    num_of_hits = 0
    for i in range(ship_length):
        if horizontal:
            if (row_pos, col_pos + i) in hits:
                num_of_hits += 1
        else:
            if (row_pos + i, col_pos) in hits:
                num_of_hits += 1
    if num_of_hits == ship_length:
        return True
    else:
        return False


def ship_type(ship):
    """Returns one of the strings "battleship", "cruiser", "destroyer", or "submarine" identifying the type of ship"""
    ship_length = ship[3]
    if ship_length == 1:
        return "submarine"
    elif ship_length == 2:
        return "destroyer"
    elif ship_length == 3:
        return "cruiser"
    else:
        return "battleship"


def is_open_sea(row, column, fleet):
    """checks if the square given by row and column neither contains nor is adjacent (horizontally, vertically, or
     diagonally) to some ship in fleet. Returns Boolean True if so and False otherwise"""
    open_sea = True
    for ship in fleet:
        row_pos = ship[0]
        col_pos = ship[1]
        horizontal = ship[2]
        ship_length = ship[3]
        for i in range(ship_length):
            if horizontal:
                col_pos += i
            else:
                row_pos += i
            if (row_pos == row and col_pos == column) or \
                    (abs(row_pos - row) == 1 and col_pos == column) or \
                    (abs(col_pos - column) == 1 and row_pos == row) or \
                    (abs(row_pos - row) == 1 and abs(col_pos - column) == 1):
                open_sea = False
    return open_sea


def ok_to_place_ship_at(row, column, horizontal, length, fleet):
    """checks if addition of a ship, specified by row, column, horizontal, and length as in ship representation above,
    to the fleet results in a legal arrangement. If so, the function returns Boolean True and it returns False
    otherwise. This function makes use of the function is_open_sea"""
    ok_to_place = True
    if (horizontal and (column + length > 10)) or \
            (not horizontal and (row + length > 10)):
            ok_to_place = False
    for i in range(length):
        if horizontal:
            if not is_open_sea(row, column + i, fleet):
                ok_to_place = False
        else:
            if not is_open_sea(row + i, column, fleet):
                ok_to_place = False
    return ok_to_place


def place_ship_at(row, column, horizontal, length, fleet):
    """returns a new fleet that is the result of adding a ship, specified by row, column, horizontal, and length as in
    ship representation above, to fleet. It may be assumed that the resulting arrangement of the new fleet is legal"""
    ship = (row, column, horizontal, length, set())
    fleet.append(ship)
    return fleet

def randomly_place_all_ships():
    #remove pass and add your implementation
    pass

def check_if_hits(row, column, fleet):
    #remove pass and add your implementation
    pass

def hit(row, column, fleet):
    #remove pass and add your implementation
    pass

def are_unsunk_ships_left(fleet):
    #remove pass and add your implementation
    pass

def main():
    #the implementation provided below is indicative only
    #you should improve it or fully rewrite to provide better functionality (see readme file)
    current_fleet = randomly_place_all_ships()

    game_over = False
    shots = 0

    while not game_over:
        loc_str = input("Enter row and colum to shoot (separted by space): ").split()    
        current_row = int(loc_str[0])
        current_column = int(loc_str[1])
        shots += 1
        if check_if_hits(current_row, current_column, current_fleet):
            print("You have a hit!")
            (current_fleet, ship_hit) = hit(current_row, current_column, current_fleet)
            if is_sunk(ship_hit):
                print("You sank a " + ship_type(ship_hit) + "!")
        else:
            print("You missed!")

        if not are_unsunk_shis_left(current_fleet): game_over = True

    print("Game over! You required", shots, "shots.")


if __name__ == '__main__': #keep this in
   main()
