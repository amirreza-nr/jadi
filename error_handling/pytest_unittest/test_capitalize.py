from capitilize import make_capital

def test():
    assert make_capital("hello") == "Hello"
    assert make_capital("") == ""
    assert make_capital("hELLO MY NAME IS   ") == "Hello my name is   "
