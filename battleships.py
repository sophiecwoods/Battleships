import random


def is_sunk(ship):
    """Returns Boolean value, which is True if ship is sunk and False otherwise."""
    # I have assigned the elements of ship to variables throughout for code readability
    row_pos = ship[0]
    col_pos = ship[1]
    horizontal = ship[2]
    ship_length = ship[3]
    hits = ship[4]
    # initialize number of hits to 0
    num_of_hits = 0

    # starting at top left square and incrementing row or column by 1 depending on ship orientation,
    # checks whether each square the ship occupies is hit and adds 1 to num_of_hits if it is
    for i in range(ship_length):
        if horizontal:
            if (row_pos, col_pos + i) in hits:
                num_of_hits += 1
        else:
            if (row_pos + i, col_pos) in hits:
                num_of_hits += 1

    # checks if all squares in ship are hit
    if num_of_hits == ship_length:
        return True
    else:
        return False


def ship_type(ship):
    """Returns one of the strings "battleship", "cruiser", "destroyer", or "submarine" identifying the type of ship."""
    ship_length = ship[3]

    if ship_length == 1: return "submarine"
    elif ship_length == 2: return "destroyer"
    elif ship_length == 3: return "cruiser"
    else: return "battleship"


def is_open_sea(row, column, fleet):
    """Checks if the square given by row and column neither contains nor is adjacent (horizontally, vertically, or
     diagonally) to some ship in fleet. Returns Boolean True if so and False otherwise."""
    open_sea = True

    # for each ship in fleet, starting at top left square and incrementing row or column by 1 depending on ship
    # orientation, checks whether each square the ship occupies contains or is next to the given square
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
    """Checks if addition of a ship, specified by row, column, horizontal, and length as in ship representation above,
    to the fleet results in a legal arrangement. If so, the function returns Boolean True and it returns False
    otherwise. This function makes use of the function is_open_sea."""
    ok_to_place = True

    # checks that placing ship at given square does not result in ship going off the edge of board
    if (horizontal and (column + length > 10)) or (not horizontal and (row + length > 10)):
        ok_to_place = False

    # starting at top left square and incrementing row or column by 1 depending on ship orientation, checks that each
    # square ship would occupy is a legal placement using is_open_sea function
    for i in range(length):
        if horizontal:
            if not is_open_sea(row, column + i, fleet):
                ok_to_place = False
        else:
            if not is_open_sea(row + i, column, fleet):
                ok_to_place = False

    return ok_to_place


def place_ship_at(row, column, horizontal, length, fleet):
    """Returns a new fleet that is the result of adding a ship, specified by row, column, horizontal, and length as in
    ship representation above, to fleet. It may be assumed that the resulting arrangement of the new fleet is legal."""
    ship = (row, column, horizontal, length, set())
    fleet.append(ship)
    return fleet


def randomly_place_all_ships():
    """Returns a fleet that is a result of a random legal arrangement of the 10 ships in the ocean. This function
     makes use of the functions ok_to_place_ship_at and place_ship_at."""
    fleet = []

    # places one battleships
    while len(fleet) < 1:
        random_row = random.randint(0, 9)
        random_column = random.randint(0, 9)
        random_horizontal = bool(random.getrandbits(1))
        if ok_to_place_ship_at(random_row, random_column, random_horizontal, 4, fleet):
            place_ship_at(random_row, random_column, random_horizontal, 4, fleet)

    # places two cruisers
    while len(fleet) < 3:
        random_row = random.randint(0, 9)
        random_column = random.randint(0, 9)
        random_horizontal = bool(random.getrandbits(1))
        if ok_to_place_ship_at(random_row, random_column, random_horizontal, 3, fleet):
            place_ship_at(random_row, random_column, random_horizontal, 3, fleet)

    # places three destroyers
    while len(fleet) < 6:
        random_row = random.randint(0, 9)
        random_column = random.randint(0, 9)
        random_horizontal = bool(random.getrandbits(1))
        if ok_to_place_ship_at(random_row, random_column, random_horizontal, 2, fleet):
            place_ship_at(random_row, random_column, random_horizontal, 2, fleet)

    # places four battleships
    while len(fleet) < 10:
        random_row = random.randint(0, 9)
        random_column = random.randint(0, 9)
        random_horizontal = bool(random.getrandbits(1))
        if ok_to_place_ship_at(random_row, random_column, random_horizontal, 1, fleet):
            place_ship_at(random_row, random_column, random_horizontal, 1, fleet)

    return fleet


def check_if_hits(row, column, fleet):
    """Returns Boolean value, which is True if the shot of the human player at the square represented by row and column
    hits any of the ships of fleet, and False otherwise."""
    global ship_index
    global ship_hit

    hit = False

    # for each ship in fleet, starting at top left square and incrementing row or column by 1 depending on ship
    # orientation, checks whether given square results in a hit. If there's a hit, stores the ship that was hit and the
    # position of that ship in the fleet in global variables
    for index, ship in enumerate(fleet):
        row_pos = ship[0]
        col_pos = ship[1]
        horizontal = ship[2]
        ship_length = ship[3]
        ship_hits = ship[4]

        for i in range(ship_length):
            if horizontal:
                if row_pos == row and col_pos + i == column and (row_pos, col_pos + i) not in ship_hits:
                    hit = True
                    ship_index = index
                    ship_hit = ship
            else:
                if row_pos + i == row and col_pos == column and (row_pos + i, col_pos) not in ship_hits:
                    hit = True
                    ship_index = index
                    ship_hit = ship

    return hit


def hit(row, column, fleet):
    """Returns a tuple (fleet1, ship) where ship is the ship from the fleet fleet that receives a hit by the shot at
     the square represented by row and column, and fleet1 is the fleet resulting from this hit. It may be assumed that
     shooting at the square row, column results in of some ship in fleet."""

    # makes use of global variables from check_if_hits. Removes the hit ship from the fleet. Adds the hit square as a
    # tuple to hits set in ship. Re-inserts ship at same position in the fleet.
    if check_if_hits(row, column, fleet):
        hits = ship_hit[4]
        fleet.remove(fleet[ship_index])
        hits.add((row, column))
        fleet.insert(ship_index, ship_hit)

    return fleet, ship_hit


def are_unsunk_ships_left(fleet):
    """Returns Boolean value, which is True if there are ships in the fleet that are still not sunk, and False
     otherwise."""
    sunk_ships = 0

    # checks if number of sunk ships equals number of ships in fleet
    for ship in fleet:
        if is_sunk(ship):
            sunk_ships += 1

    if sunk_ships == len(fleet):
        return False
    else:
        return True


def main():
    """Returns nothing. It prompts the user to call out rows and columns of shots and outputs the responses of the
     computer iteratively until the game stops."""
    current_fleet = randomly_place_all_ships()

    game_over = False
    shots = 0

    while not game_over:
        try:
            input_str = input("Enter row and column (separated by space) to shoot or type 'quit' to end the game: ")
            if input_str == "quit" or input_str == "Quit":
                # reset shots to 0 if user quits game before completing it
                shots = 0
                game_over = True
                print("You have ended the game.")
            else:
                # if user input is not quit, store location of shot as integers
                loc_str = input_str.split()
                current_row = int(loc_str[0])
                current_column = int(loc_str[1])

                # check that user input is a valid number on the board
                if 0 <= current_row <= 9 and 0 <= current_column <= 9:
                    shots += 1

                    # check if shot is a hit, update fleet and ship if so, and check if shot sinks ship
                    if check_if_hits(current_row, current_column, current_fleet):
                        print("You have a hit!")
                        (current_fleet, current_ship) = hit(current_row, current_column, current_fleet)
                        if is_sunk(ship_hit):
                            print("You sank a " + ship_type(ship_hit) + "!")
                    else:
                        print("You missed!")

                else:
                    print("Invalid values for row and column. Please enter numbers between 0 and 9.")

            if not are_unsunk_ships_left(current_fleet): game_over = True

        # exception handling for invalid input i.e. non integers
        except ValueError:
            print("Invalid values for row and column. Please enter integer numbers only or type 'quit' to end game.")

        # exception handling for incorrectly formatted input or no input
        except IndexError:
            print("Invalid values for row and column. Please separate the values with a space.")

    # only prints this game over message if user completes the game and not if they choose to quit
    if shots != 0:
        print("Game over! You required", shots, "shots.")


if __name__ == '__main__':
    main()
