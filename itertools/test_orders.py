from orders import generate_id

def test():
    result = generate_id(100)

    first = next(result)
    second = next(result)
    third = next(result)

    assert first == 100
    assert second == 101
    assert third == 102
