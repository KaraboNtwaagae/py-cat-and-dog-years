from app.main import get_human_age


def test_should_return_zero_before_first_threshold() -> None:
    assert get_human_age(0, 0) == [0, 0]
    assert get_human_age(14, 14) == [0, 0]


def test_should_return_one_at_first_threshold() -> None:
    assert get_human_age(15, 15) == [1, 1]
    assert get_human_age(23, 23) == [1, 1]


def test_should_return_two_at_second_threshold() -> None:
    assert get_human_age(24, 24) == [2, 2]
    assert get_human_age(27, 27) == [2, 2]


def test_should_handle_cat_and_dog_differently_after_second_threshold() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_should_convert_large_values() -> None:
    assert get_human_age(100, 100) == [21, 17]


def test_cat_boundary_values() -> None:
    assert get_human_age(27, 24) == [2, 2]
    assert get_human_age(28, 24) == [3, 2]
    assert get_human_age(31, 24) == [3, 2]
    assert get_human_age(32, 24) == [4, 2]


def test_dog_boundary_values() -> None:
    assert get_human_age(24, 28) == [2, 2]
    assert get_human_age(24, 29) == [2, 3]
    assert get_human_age(24, 33) == [2, 3]
    assert get_human_age(24, 34) == [2, 4]
