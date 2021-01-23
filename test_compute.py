import compute

def test_has_x_1():
    assert compute.has_x("x")

def test_has_x_2():
    assert compute.has_x("X")

def test_is_number_1():
    assert compute.is_number("0.5")
    assert not compute.is_number("")

def test_is_number_2():
    assert not compute.is_number("x")

def test_is_number_3():
    assert not compute.is_number("2^4")