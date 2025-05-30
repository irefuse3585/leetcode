import pytest

from p2359_find_closest_node.find_closest_node import Solution


@pytest.mark.parametrize(
    "edges,node1,node2,expected",
    [
        ([5, 4, 5, 4, 3, 6, -1], 0, 1, -1),
        ([2, 2, 3, -1], 0, 1, 2),
        ([1, -1], 0, 1, 1),
        ([1, 2, 0], 0, 2, 0),
        ([1, 2, 3, 4, -1], 0, 2, 2),
    ],
)
def test_closest_meeting_node(edges, node1, node2, expected):
    assert Solution().closestMeetingNode(edges, node1, node2) == expected
