def plus_one(x):
    return x+2

def test_1(x):
    msg = f"Expected plus_one(x) to return {x+1}, instead got {str(plus_one(x))}."
    assert plus_one(x) == x+1, msg

for x in range(-5, 6):
    test_1(x)