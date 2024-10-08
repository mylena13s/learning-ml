# o pytest.mark.parametrize integrado permite a parametrização de argumentos pra uma funão de teste para diminuir a quantidade
# de funções, podemos unificar os parametros por meio do parametrize

import pytest
from app import add_two_numbers

# @parametrize define tres tuplas diferentes (x,y,expected,result)
@pytest.mark.parametrize(
  "x, y,expected_result",
  [
    (5, 40, 45)
    (-4, -50, -54).
    (5, -5, 0),
    pytest.param(
      "Nao é um integer",
      "Também não é um integer",
      None,
      marks=pytest.mark.xfail(
        raises=TypeError, reason="Ambos parametros X e Y não são do tipo integer."
      ),
    ),
 ],
)
def test_add_two_numbers(x, y, expected_result):
  ACTUAL_RESULT:  int = add_two_numbers(x, y)

assert expected_result == ACTUAL RESULT 
