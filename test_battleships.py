import pytest
from battleships import *

@pytest.mark.parametrize("ship_input, expected_output",
                         [
                             #tests that a cruiser is sunk in three hits
                             ((2, 3, False, 3, {(2, 3), (3, 3), (4, 3)}), True),
                             
                             #tests that a submarine is sunk in one hit
                             ((0, 1, True, 1, {(0, 1)}), True),
                             
                             #tests that a destroyer is sunk in two hits
                             ((4, 7, False, 2, {(4, 7), (5, 7)}), True),
                             
                             #tests that a battleship is sunk in four hits
                             ((9, 6, True, 4, {(9, 6), (9, 7), (9, 8), (9, 9)}), True),
                             
                             #tests that a destroyer is not sunk in one hit
                             ((7, 3, True, 2, {7, 4}), False),
                             
                             #tests that a battleship is not sunk in two hits
                             ((2, 0, False, 4, {(5, 0), (2, 0)}), False),
                             
                             #tests that a cruiser is not sunk in two hits
                             ((5, 5, True, 3, {(5, 6), (5, 7)}), False),
                             
                             #tests that a submarine is not sunk in no hits
                             ((3, 9, True, 1, set()), False),
                             
                             #tests that a destroyer is not sunk in no hits
                             ((8, 6, False, 2, set()), False),
                             
                             #tests that a cruiser is not sunk in no hits
                             ((1, 5, True, 3, set()), False),
                             
                             #tests that a battleship is not sunk in no hits
                             ((0, 3, True, 4, set()), False)
                         ]
                         )
def test_is_sunk1(ship_input, expected_output):
    assert is_sunk(ship_input) == expected_output


@pytest.mark.parametrize("ship_input, expected_output",
                         [
                             # tests that a horizontal ship of length 1 returns submarine
                             ((0, 0, True, 1, set()), "submarine"),

                             # tests that a vertical ship of length 1 returns submarine
                             ((2, 5, False, 1, set()), "submarine"),

                             # tests that a horizontal ship of length 2 returns destroyer
                             ((8, 3, True, 2, set()), "destroyer"),

                             # tests that a vertical ship of length 2 returns destroyer
                             ((7, 2, False, 2, set()), "destroyer"),

                             # tests that a horizontal ship of length 3 returns cruiser
                             ((4, 5, True, 3, set()), "cruiser"),

                             # tests that a vertical ship of length 3 returns cruiser
                             ((1, 6, False, 3, set()), "cruiser"),

                             # tests that a horizontal ship of length 4 returns battleship
                             ((4, 4, True, 4, set()), "battleship"),

                             # tests that a vertical ship of length 4 returns battleship
                             ((6, 9, False, 4, set()), "battleship"),

                             # tests that ship hits doesn't affect ship type on submarine
                             ((3, 1, True, 1, {(3, 1)}), "submarine"),

                             # tests that ship hits doesn't affect ship type on destroyer
                             ((5, 8, False, 2, {(5, 8), (6, 8)}), "destroyer"),

                             # tests that ship hits doesn't affect ship type on cruiser
                             ((7, 0, True, 3, {(7, 2)}), "cruiser"),

                             # tests that ship hits doesn't affect ship type on battleship
                             ((3, 3, False, 4, {(3, 3), (4, 3), (5, 3)}), "battleship")
                         ]
                         )
def test_ship_type1(ship_input, expected_output):
    assert ship_type(ship_input) == expected_output


@pytest.mark.parametrize("row_input, column_input, fleet_input, expected_output",
                         [
                             # tests that square in empty board returns True
                             (8, 0, [], True),

                             # tests that square with no adjacent ships and one ship on board returns True
                             (4, 2, [(8, 3, True, 3, set())], True),

                             # tests that square with no adjacent ships and five ships on board returns True
                             (6, 7, [(8, 5, False, 2, set()), (4, 3, True, 4, set()), (3, 8, False, 1, set()),
                                     (6, 1, True, 1, set()), (0, 2, True, 3, set())], True),

                             # tests that square with no adjacent ships and nine ships on board returns True
                             (2, 9, [(6, 9, False, 4, set()), (3, 2, True, 3, set()), (6, 3, False, 3, set()),
                                     (2, 0, False, 2, set()), (7, 6, True, 2, set()), (1, 7, False, 2, set()),
                                     (9, 7, False, 1, set()), (0, 4, True, 1, set()), (4, 9, True, 1, set())], True),

                             # tests that square occupied by ship and one ship on board returns False
                             (1, 5, [(0, 5, False, 4, set())], False),

                             # tests that square occupied by ship and four ships on board returns False
                             (2, 1, [(5, 3, True, 2, set()), (1, 1, False, 2, set()), (6, 0, False, 1, set()),
                                     (8, 6, True, 3, set())], False),

                             # tests that square horizontally adjacent to ship returns False
                             (7, 7, [(3, 2, False, 3, set()), (7, 3, True, 4, set()), (5, 9, True, 1, set())], False),

                             # tests that square diagonally adjacent to ship returns False
                             (9, 8, [(2, 8, True, 1, set()), (8, 1, True, 3, set()), (3, 1, False, 1, set()),
                                     (1, 6, True, 1, set()), (5, 3, True, 2, set()), (6, 7, False, 3, set())], False),

                             # tests that square vertically adjacent to ship returns False
                             (6, 2, [(9, 5, 4, False, set()), (3, 7, True, 3, set()), (1, 1, False, 3, set()),
                                     (5, 0, False, 2, set()), (3, 7, True, 2, set()), (4, 4, True, 2, set()),
                                     (5, 2, True, 1, set())], False),

                             # tests that square horizontally and diagonally adjacent to ships returns False
                             (3, 4, [(7, 8, False, 1, set()), (8, 2, True, 2, set()), (4, 3, False, 3, set()),
                                     (1, 7, True, 1, set()), (0, 0, True, 4, set()), (3, 0, False, 2, set()),
                                     (3, 5, True, 2, set()), (0, 9, False, 3, set())], False),

                             # tests that square vertically and diagonally adjacent to ships returns False
                             (2, 6, [(3, 6, 4, False, set()), (8, 4, True, 3, set()), (6, 2, True, 3, set()),
                                     (3, 8, False, 2, set()), (2, 1, False, 2, set()), (0, 3, False, 2, set()),
                                     (9, 1, True, 1, set()), (1, 5, True, 1, set()), (7, 0, False, 1, set())], False)
                         ]
                         )
def test_is_open_sea1(row_input, column_input, fleet_input, expected_output):
    assert is_open_sea(row_input, column_input, fleet_input) == expected_output


@pytest.mark.parametrize("row_input, column_input, horizontal_input, length_input, fleet_input, expected_output",
                         [  # tests that legal placement of battleship on empty board returns True
                             (3, 5, True, 4, [], True),

                             # tests that legal placement of cruiser on board with 3 other ships returns True
                             (4, 8, False, 3, [(0, 1, False, 4, set()), (6, 3, True, 1, set()), (8, 5, True, 2, set())],
                              True),

                             # tests that legal placement of submarine on board with 9 other ships returns True
                             (1, 8, True, 1, [(6, 5, True, 4, set()), (2, 0, False, 3, set()), (9, 2, True, 3, set()),
                                              (3, 4, True, 2, set()), (6, 2, True, 2, set()), (8, 0, False, 2, set()),
                                              (9, 9, False, 1, set()), (1, 4, True, 1, set()), (3, 7, True, 1, set())],
                              True),

                             # tests that destroyer placed with first square vertically next to another ship, and 2
                             # ships on board, returns False
                             (3, 1, False, 2, [(2, 0, True, 3, set()), (7, 9, False, 2, set())], False),

                             # tests that battleship placed with third square horizontally next to another ship, and 4
                             # ships on board, returns False
                             (5, 4, False, 4, [(1, 6, False, 3, set()), (5, 9, False, 2, set()), (9, 6, True, 1, set()),
                                               (7, 2, True, 3, set())], False),

                             # tests that cruiser placed with last square diagonally next to a ship, and 6 ships on
                             # board, returns False
                             (6, 0, True, 3, [(0, 1, True, 4, set()), (3, 3, False, 3, set()), (8, 6, True, 3, set()),
                                              (2, 7, False, 2, set()), (9, 0, True, 2, set()), (8, 4, True, 1, set())],
                              False),

                             # tests that submarine placed horizontally and diagonally next to 2 ships, and 9 ships on
                             # board, returns False
                             (8, 7, False, 1, [(5, 1, True, 4, set()), (6, 6, False, 3, set()), (0, 6, True, 3, set()),
                                               (9, 8, True, 2, set()), (2, 0, True, 2, set()), (7, 4, False, 2, set()),
                                               (8, 1, False, 1, set()), (3, 9, False, 1, set()),
                                               (2, 5, True, 1, set())], False),

                             # tests that battleship placed vertically with not enough rows on the board to fit returns
                             # False
                             (7, 0, False, 4, [(0, 0, True, 3, set()), (9, 3, True, 1, set()), (3, 4, False, 3, set()),
                                               (1, 6, False, 2, set()), (6, 6, True, 3, set())], False),

                             # tests that cruiser placed horizontally with not enough columns on the board to fit
                             # returns False
                             (4, 9, True, 3, [(4, 2, True, 4, set())], False)
                         ]
                         )
def test_ok_to_place_ship_at1(row_input, column_input, horizontal_input, length_input, fleet_input, expected_output):
    assert ok_to_place_ship_at(row_input, column_input, horizontal_input, length_input, fleet_input) == expected_output


@pytest.mark.parametrize("row_input, column_input, horizontal_input, length_input, fleet_input, expected_output",
                         [
                             #tests that placing first submarine in an empty fleet returns a fleet of that 1 submarine
                             (5, 9, True, 1, [], [(5, 9, True, 1, set())]),

                             #tests that placing a destroyer in a fleet of 1 ship returns a fleet of 2 ships with the
                             #destroyer added to the end
                             (1, 7, False, 2, [(5, 5, False, 4, set())], [(5, 5, False, 4, set()),
                                                                          (1, 7, False, 2, set())]),

                             #tests that placing a cruiser in a fleet of 5 ships returns a fleet of 6 ships with the
                             #cruiser added to the end
                             (6, 4, False, 3, [(2, 0, True, 4, set()), (5, 7, False, 2, set()), (6, 9, False, 1, set()),
                                               (8, 0, False, 1, set()), (2, 6, True, 3, set())],
                              [(2, 0, True, 4, set()), (5, 7, False, 2, set()), (6, 9, False, 1, set()),
                               (8, 0, False, 1, set()), (2, 6, True, 3, set()), (6, 4, False, 3, set())]),

                            #tests that placing a submarine in a fleet of 9 ships returns a fleet of 10 ships with the
                            #submarine added to the end
                            (0, 4, True, 1, [(3, 2, False, 4, set()), (7, 5, True, 3, set()), (1, 7, True, 3, set()),
                                             (3, 5, False, 2, set()), (9, 1, True, 2, set()), (6, 0, False, 2, set()),
                                             (1, 1, False, 1, set()), (4, 9, True, set()), (8, 9, True, 1, set())],
                             [(3, 2, False, 4, set()), (7, 5, True, 3, set()), (1, 7, True, 3, set()),
                              (3, 5, False, 2, set()), (9, 1, True, 2, set()), (6, 0, False, 2, set()),
                              (1, 1, False, 1, set()), (4, 9, True, set()), (8, 9, True, 1, set()),
                              (0, 4, True, 1, set())]),

                            #tests that placing first battleship in an empty fleet returns a fleet of that 1 battleship
                            (9, 2, True, 4, [], [(9, 2, True, 4, set())])
                         ]
                         )
def test_place_ship_at1(row_input, column_input, horizontal_input, length_input, fleet_input, expected_output):
    assert place_ship_at(row_input, column_input, horizontal_input, length_input, fleet_input) == expected_output


@pytest.mark.parametrize("row_input, column_input, fleet_input, expected_output",
                         [
                             (3, 0, [(1, 0, False, 4, set())], True),

                             (4, 4, [(9, 0, True, 2, {(9, 1), (9, 1)}),
                                     (4, 1, True, 3, {(4, 3)}), (0, 6, False, 4, set()), (6, 9, True, 1, set())], False)
                         ]
                         )
def test_check_if_hits1(row_input, column_input, fleet_input, expected_output):
    assert check_if_hits(row_input, column_input, fleet_input) == expected_output


@pytest.mark.parametrize("row_input, column_input, fleet_input, expected_output",
                         [
                             (7, 2, [(7, 1, True, 3, {(7, 1)}), (0, 3, False, 4, {2, 3}), (6, 5, True, 1, set()),
                                     (1, 9, False, 2, set())], ([(7, 1, True, 3, {(7, 1), (7, 2)}),
                                                                 (0, 3, False, 4, {2, 3}), (6, 5, True, 1, set()),
                                     (1, 9, False, 2, set())], (7, 1, True, 3, {(7, 1,), (7, 2)}))),

                             (9, 9, [(4, 1, True, 1, {(4, 1)}), (7, 2, False, 3, {(7, 2), (8, 2), (9, 2)}),
                                     (2, 6, False, 4, {(2, 6), (3, 6),}), (9, 8, True, 2, set())],
                              ([(4, 1, True, 1, {(4, 1)}), (7, 2, False, 3, {(7, 2), (8, 2), (9, 2)}),
                                     (2, 6, False, 4, {(2, 6), (3, 6),}), (9, 8, True, 2, {(9, 9)})],
                             (9, 8, True, 2, {(9, 9)}))),

                             (5, 5, [(5, 2, True, 4, {(5, 2), (5, 3), (5, 4)}), (3, 4, True, 2, {(3, 4), (3, 5)}),
                                     (0, 7, True, 1, {(0, 7)}), (4, 8, False, 3, {(4, 8), (5, 8), (6, 8)})],
                              ([(5, 2, True, 4, {(5, 2), (5, 3), (5, 4), (5, 5)}), (3, 4, True, 2, {(3, 4), (3, 5)}),
                                     (0, 7, True, 1, {(0, 7)}), (4, 8, False, 3, {(4, 8), (5, 8), (6, 8)})],
                              (5, 2, True, 4, {(5, 2), (5, 3), (5, 4), (5, 5)})))
                         ]
                         )
def test_hit1(row_input, column_input, fleet_input, expected_output):
    assert hit(row_input, column_input, fleet_input) == expected_output


@pytest.mark.parametrize("fleet_input, expected_output",
                         [
                             ([(1, 2, True, 2, {(1, 2), (1, 3)}), (3, 4, True, 1, {(3, 4)}),
                             (6, 8, False, 3, {(8, 8)}), (1, 9, False, 4, {(1, 9), (2, 9), (3, 9), (4, 9)})], False),

                             ([(1, 1, False, 3, {(1, 1), (2, 1), (3, 1)}), (9, 2, True, 2, {(9, 2), (9, 3)}),
                               (2, 3, True, 4, {(2, 3), (2, 4), (2, 5), (2, 6)}), (5, 4, True, 1, {(5, 4)})], True)
                         ]
                         )
def test_are_unsunk_ships_left1(fleet_input, expected_output):
    assert are_unsunk_ships_left(fleet_input) == expected_output

