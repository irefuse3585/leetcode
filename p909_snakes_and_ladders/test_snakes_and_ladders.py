from typing import List

import pytest

from p909_snakes_and_ladders.snakes_and_ladders import Solution


@pytest.mark.parametrize(
    "board, expected",
    [
        # 1x1 board: only one square (start and end), no moves needed
        ([[-1]], 0),
        # 2x2 board without snakes or ladders:
        # Boustrophedon numbering:
        #   (1)  (2)
        #   (4)  (3)
        # You can roll a 3 from 1 → 4 in one move.
        (
            [
                [-1, -1],
                [-1, -1],
            ],
            1,
        ),
        # 2x2 board with a ladder from 2 -> 4:
        # From 1, roll 1 -> land on 2 -> ladder to 4 = 1 move
        (
            [
                [-1, 4],
                [-1, -1],
            ],
            1,
        ),
        # 3x3 board without snakes or ladders:
        # Boustrophedon numbering:
        #    1   2   3
        #    6   5   4
        #    7   8   9
        # Minimum number of moves = ceil((9 - 1) / 6) = 2
        (
            [
                [-1, -1, -1],
                [-1, -1, -1],
                [-1, -1, -1],
            ],
            2,
        ),
        # 3x3 board with a snake cycle (still reachable in 2 moves):
        # board:
        #   row 2 -> [-1,  3,  2]
        # means: cell2 -> 3, cell3 -> 2 (cycle).
        # But from 1: roll 1->2->ladder to 3 (1 move),
        # then roll 6 -> 9 (2nd move). So answer = 2.
        (
            [
                [-1, -1, -1],
                [-1, -1, -1],
                [-1, 3, 2],
            ],
            2,
        ),
        # 4x4 board with a ladder 3 -> 15 and a snake 14 -> 4:
        # Boustrophedon numbering:
        #    1    2    3    4
        #    8    7    6    5
        #    9   10   11   12
        #   16   15   14   13
        # Path: from 1 roll 2 -> land on 3 -> ladder to 15 (1 move),
        # then roll 1 -> land on 16 (2nd move) => 2.
        (
            [
                [-1, -1, -1, -1],
                [-1, -1, -1, -1],
                [-1, -1, -1, 4],
                [-1, 15, -1, -1],
            ],
            2,
        ),
        # 4x4 board with a ladder 2 -> 16 (end):
        # To make cell #2 point to 16, we place 16 at (row=3, col=1).
        # Boustrophedon numbering (row=3 is bottom):
        #    (1)  (2)  (3)   (4)
        #    (8)  (7)  (6)   (5)
        #    (9) (10) (11)  (12)
        #   (16) (15) (14)  (13)
        # From 1, roll 1 -> land on 2, ladder to 16: 1 move total.
        (
            [
                [-1, -1, -1, -1],
                [-1, -1, -1, -1],
                [-1, -1, -1, -1],
                [-1, 16, -1, -1],
            ],
            1,
        ),
        # 5x5 board without snakes or ladders:
        # Boustrophedon numbering, no shortcuts:
        # Minimum moves = ceil((25 - 1) / 6) = 4
        (
            [
                [-1, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1],
            ],
            4,
        ),
        # 5x5 board with a ladder 4 -> 22:
        # Boustrophedon numbering:
        #    (1)  (2)  (3)  (4)   (5)
        #    (10) (9)  (8)  (7)   (6)
        #    (11) (12) (13) (14)  (15)
        #    (20) (19) (18) (17)  (16)
        #    (21) (22) (23) (24)  (25)
        # Ladder placed so that cell #4 maps to 22. From 1:
        # roll 3 -> land on 4 -> ladder to 22 (1 move),
        # then roll 3 -> land on 25 (2nd move) => 2.
        (
            [
                [-1, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1],
                [-1, -1, -1, 22, -1],
            ],
            2,
        ),
    ],
)
def test_snakes_and_ladders(board: List[List[int]], expected: int):
    assert Solution().snakesAndLadders(board) == expected
