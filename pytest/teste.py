# pytest = framework de testes para trabalhar em projetos maestro, através da esteira Data Workflow, que use python script.

import pytest 

# function

def soma(a, b):
  return a + b

# teste
def teste_soma():
  resultado = soma(2, 5)
  assert resultado == 7, f'erro: esperado 7, mas obteve{resultado}' 
