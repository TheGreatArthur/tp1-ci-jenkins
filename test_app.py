from app import addition

def test_addition_simple():
    assert addition(2, 3) == 5

def test_addition_zero():
    assert addition(0, 10) == 10

def test_addition_negatif():
    assert addition(-5, 2) == -3
