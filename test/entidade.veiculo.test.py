#!\bin\python
# Ref: https://docs.python.org/pt-br/3/library/unittest.html#
import unittest
from src.entidades.veiculo import Veiculo

class VeiculoTest(unittest.TestCase):
    def setUp(self):
        self.veiculo = Veiculo()

    def tearDown(self):
        pass
                
    def test_instacia_correta(self):
        self.assertIsInstance(self.veiculo, Veiculo, "Objeto veiculo é uma instância da classe Veiculo")

    def test_veiculo_tem_placa(self):
        self.assertTrue(hasattr(self.veiculo, "placa"),"Veículo deve ter placa")

    def test_veiculo_tem_marca(self):
        self.assertTrue(hasattr(self.veiculo, "marca"),"Veículo deve ter marca")

    def test_veiculo_tem_modelo(self):
        self.assertTrue(hasattr(self.veiculo, "modelo"),"Veículo deve ter modelo")

    def test_veiculo_tem_preco_diaria(self):
        self.assertTrue(hasattr(self.veiculo, "preco_diaria"),"Veículo deve ter preço da diária")


if __name__ == '__main__':
    unittest.main()