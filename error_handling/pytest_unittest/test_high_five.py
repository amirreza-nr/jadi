import pytest
from high_five import high_five
def test_high_five():
    assert high_five(105) == True
    assert high_five(-5) == True
    assert high_five(5.0) == True

def test_high_five2():
    assert high_five(4) == False

def test_errors():
    assert high_five(10.0) == True
    with pytest.raises(TypeError):
        high_five(5.5)
