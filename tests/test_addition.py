from work import addition
import pytest


@pytest.mark.parametrize(
    "num1,num2,expected",
    [
        (1, 2, 3),
        (7, 2, 9),
        (10_000, 9382, 19_382),
    ],
)
def test_addition_works(num1: int, num2: int, expected: int) -> None:
    assert addition(num1, num2) == expected
