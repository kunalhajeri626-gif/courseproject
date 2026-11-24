import pytest
from Student import calculate_grade


@pytest.mark.parametrize("avg,grade", [
    (95, "S"), (90, "S"), (85, "A"), (80, "A"), (70, "B"), (65, "B"),
    (55, "C"), (50, "C"), (45, "D"), (40, "D"), (39.9, "F"), (0, "F"),
])
def test_grades(avg, grade):
    assert calculate_grade(avg) == grade
