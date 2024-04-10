import pytest

from lib import generate_random_uppercase_string


@pytest.mark.parametrize("length", [5, 10, 100, 10_000])
def test_generate_uppsercase_str(length: int) -> None:
    res = generate_random_uppercase_string(length)

    assert res.isupper()
    assert len(res) == length
