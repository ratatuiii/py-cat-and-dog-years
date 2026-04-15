import pytest


from app.main import get_human_age


def test_should_calculate_zero_year_correctly() -> None:
    assert get_human_age(0, 0) == [0, 0]
    assert get_human_age(14, 14) == [0, 0]


def test_should_calculate_one_year_correctly() -> None:
    assert get_human_age(15, 15) == [1, 1]
    assert get_human_age(23, 23) == [1, 1]


def test_should_calculate_two_years_correctly() -> None:
    assert get_human_age(24, 24) == [2, 2]
    assert get_human_age(27, 27) == [2, 2]
    assert get_human_age(28, 28) == [3, 2]


def test_should_calculate_three_and_more_years_correctly() -> None:
    assert get_human_age(28, 28) == [3, 2]
    assert get_human_age(100, 100) == [21, 17]


def test_should_validate_input_correctly() -> None:
    with pytest.raises(ValueError):
        get_human_age(-1, 0)


def test_should_validate_input_type_correctly() -> None:
    with pytest.raises(TypeError):
        get_human_age([1, 2, 3], "a")
