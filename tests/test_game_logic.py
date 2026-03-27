from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"
    
from logic_utils import check_guess

def test_too_high():
    assert check_guess(60, 50) == "Too High"

def test_too_low():
    assert check_guess(40, 50) == "Too Low"

def test_win():
    assert check_guess(50, 50) == "Win"

def test_negative_number():
    assert check_guess(-10, 50) == "Too Low"

def test_large_number():
    assert check_guess(1000, 50) == "Too High"

def test_decimal_input_simulation():
    assert check_guess(int(49.9), 50) == "Too Low"

def test_boundary_min():
    assert check_guess(1, 1) == "Win"

def test_boundary_max():
    assert check_guess(100, 100) == "Win"    