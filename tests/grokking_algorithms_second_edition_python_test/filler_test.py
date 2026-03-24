import pytest

from grokking_algorithms_second_edition_python.filler import dummy


@pytest.mark.unit_test
def test_dummy() -> None:
    assert dummy() == 0
