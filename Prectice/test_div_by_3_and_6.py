import pytest

@pytest.mark.xfail
def test_divisible_by_3(Input_value):
    assert 12==Input_value/3

@pytest.mark.skip
def test_divisible_by_6(Input_value):
    assert 6==Input_value/6





