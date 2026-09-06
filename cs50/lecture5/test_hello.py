from hello import hello

def test_argument():
    assert hello("world") == "hello, world"
    assert hello("Alice") == "hello, Alice"

def test_hello_default():
    assert hello() == "hello, world"
