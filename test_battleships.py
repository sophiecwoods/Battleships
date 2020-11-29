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
                             ((0, 0, True, 1, set()), "submarine"),
                             ((7, 2, False, 2, set()), "cruiser"),
                             ((4, 5, True, 3, {(4, 7)}), "destroyer"),
                             ((6, 9, False, 4, {(7, 9), (8, 9)}), "battleship"),
                         ]
                         )
def test_ship_type1(ship_input, expected_output):
    assert ship_type(ship_input) == expected_output

@pytest.mark.parametrize("row_input, column_input, fleet_input, expected_output",
                         [
                             (8, 0, [], True),
                             (4, 2, [(8, 3, True, 3, set())], True),
                             (1, 5, [(0, 5, False, 4, set())], False),
                             (7, 7, [(3, 2, False, 3, set()), (7, 3, True, 4, set()), (5, 9, True, 1, set())], False),
                         ]
                         )
def test_is_open_sea1(row_input, column_input, fleet_input, expected_output):
    assert is_open_sea(row_input, column_input, fleet_input) == expected_output

@pytest.mark.parametrize("row_input, column_input, horizontal_input, length_input, fleet_input, expected_output",
                         [
                             (3, 5, True, 2, [], True),

                             (4, 8, False, 3, [(0, 1, False, 4, set()), (6, 3, True, 1, set()), (8, 5, True, 2, set())],
                              True),

                             (3, 2, True, 1, [(2, 0, True, 3, set()), (7, 9, False, 2, set())], False),

                             (7, 0, False, 4, [(0, 0, True, 3, set()), (9, 3, True, 1, set()), (3, 4, False, 3, set()),
                                               (1, 6, False, 2, set()), (6, 6, True, 3, set())], False)
                         ]
                         )
def test_ok_to_place_ship_at1(row_input, column_input, horizontal_input, length_input, fleet_input, expected_output):
    assert ok_to_place_ship_at(row_input, column_input, horizontal_input, length_input, fleet_input) == expected_output

@pytest.mark.parametrize("row_input, column_input, horizontal_input, length_input, fleet_input, expected_output",
                         [
                             (5, 9, True, 1, [], [(5, 9, True, 1, set())]),

                             (1, 7, False, 2, [(5, 5, False, 4, set())], [(1, 7, False, 2, set()),
                                                                          (5, 5, False, 4, set())]),

                             (6, 4, False, 3, [(2, 0, True, 4, set()), (5, 7, False, 2, set())],
                              [(6, 4, False, 3, set()), (2, 0, True, 4, set()), (5, 7, False, 2, set())])
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


