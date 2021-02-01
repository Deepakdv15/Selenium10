import pytest

@pytest.mark.skip
def test_divisible_by_13(Input_value):
    assert Input_value%13!=0

@pytest.mark.xfail
@pytest.mark.parametrize("num,output",[(1,11),(2,22),(4,44),(5,45),(6,66)])
def test_multiplication(num,output):
    assert num*11==output