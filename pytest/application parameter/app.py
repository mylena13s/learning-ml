# o método recebe dois parâmetros, x e y, e retorna a soma entre eles. E, verifica se ambos são do tipo integer.

def add_two_numbers(x: int, y: int) -> int:
  """retorna a soma entre dois números.

  Parameters 
  ----------
x : int
   Primeiro número
y : int
   Segundo número
if not (isistance(x, int)  or isinstance(y, int)): 
   raise TypeError(f"Parametros {x=} e {y=} devem ser do tipo integer.")

return x + y
   
