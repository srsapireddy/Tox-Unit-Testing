from my_module import square

def test_square_gives_correct_value():
    # When
    subject = square(4)

    # Then
    assert subject == 16
