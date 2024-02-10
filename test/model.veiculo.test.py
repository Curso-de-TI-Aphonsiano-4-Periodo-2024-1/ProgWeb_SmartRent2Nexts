#!\bin\python
# Ref: https://docs.python.org/pt-br/3/library/unittest.html#

import unittest
from src.entidades.veiculo import Veiculo
from src.model.model import VeiculoModel

class VeiculoModelTest(unittest.TestCase):
    def test_pesquisa_sem_parametro_deve_retornar_list(self):
        resultado = VeiculoModel().pesquisar()
        self.assertIsInstance(resultado, list, "Pesquisar sem parametro deve retornar uma lista")

    def test_pesquisa_com_parametro_deve_retornar_list_com_um_elemento(self):
        resultado = VeiculoModel().pesquisar(chave="placa",valor="ABC1D23")
        self.assertIsInstance(resultado, list , "Pesquisar com parametro deve retornar uma lista com um elemento")
        self.assertEqual(len(resultado), 1 , "Pesquisar com parametro deve retornar uma lista com um elemento")
        self.assertEqual(resultado[0].placa, "ABC1D23", "Pesquisar com parametro deve retornar uma lista com o elemento")

    def test_cadastro_deve_retornar_o_obj_cadastrado(self):
        veiculo = Veiculo()
        cadastrado = VeiculoModel().adicionar(veiculo)
        self.assertIs(veiculo,cadastrado,"Cadastrar deve retornar o objeto salvo!")

    def test_exclusao_deve_retornar_false_quando_nao_excluir(self):
        veiculo = Veiculo()
        model = VeiculoModel()
        self.assertFalse(model.excluir(veiculo), "Excluir deve retornar falso para não exclusão!")        

    def test_exclusao_deve_retornar_true_quando_excluir(self):
        veiculo = Veiculo()
        veiculo.placa = "QWE4R56"        
        self.assertTrue(VeiculoModel().excluir(veiculo), "Excluir deve retornar verdadeiro para exclusão!")

if __name__ == "__main__":
    unittest.main()