import math
import pytest

@pytest.mark.great
def test_sqr():
    assert 5==math.sqrt(25)

@pytest.mark.great
def testequal():
    assert 7*7==40

@pytest.mark.great
def tesNum():
    assert 10==11

@pytest.mark.others
def test_grester_numner():
    num=20
    assert 21>num
    
@pytest.mark.others
def test_less_number():
    num=20
    assert 12<num