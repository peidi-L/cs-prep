# from calculator import square

# def main():
#     test_square()

# def test_square():
#     try:
#         assert square(2) == 4
#     except AssertionError:
#         print("Test failed for square(2)")

#     try:
#         assert square(3) == 9
#     except AssertionError:
#         print("Test failed for square(3)")

#     try:
#         assert square(-2) == 4
#     except AssertionError:
#         print("Test failed for square(-2)")

#     try:
#         assert square(-3) == 9
#     except AssertionError:
#         print("Test failed for square(-3)")

#     try:
#         assert square(0) == 0
#     except AssertionError:
#         print("Test failed for square(0)")

# if __name__ == "__main__":
#     main()

from calculator import square

import pytest

def test_positive():
    assert square(2) == 4
    assert square(3) == 9

def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9

def test_zero():
    assert square(0) == 0

def test_str():
    with pytest.raises(TypeError):
        square("string")
