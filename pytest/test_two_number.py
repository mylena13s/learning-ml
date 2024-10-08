# test app

import pytest
from app import add_two_numbers

# soma de dois números positivos
def test_add_positives():
  X: int = 5
  Y: int = 40
  EXPECTED_RESULT: int = 45
  ACTUAL_RESULT: int = add_two_numbers(X, Y)

assert EXPECTED_RESULT == ACTUAL_RESULT

# soma de dois números negativos;
def test_add_negatives():
 X: int = -4
 Y: int = -50
EXPECTED_RESULT: int = -54
ACTUAL_RESULT: int = add_two_numbers(X, Y)

assert EXPECTED_RESULT == ACTUAL_RESULT

# soma de um número positivo com um negativo
def test_add_mixed():
 X: int = 5
 Y: int = -5
EXPECTED_RESULT: int = 0
ACTUAL_RESULT: int = add_two_numbers(X, Y)

assert EXPECTED_RESULT == ACTUAL_RESULT

