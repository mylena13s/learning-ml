import pytest

# pytest.fixture - função para preparar o ambiente ou fornecer dados antes que sejam executados. ex: inicializar objetos, conectar com o banco de dados, etc.

@pytest.fixture
def my_fruit():
  return "banana"

def test_my_fruit_in_basket(my_fruit):
  print(f"Minha fruta é: {my_fruit}")

FRUIT_BASKET = ["banana", "apple"]

assert my_fruit in FRUIT_BASKET 
