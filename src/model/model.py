from ..dados.database import veiculos, clientes, reservas
from ..entidades.veiculo import Veiculo

# Classe Model 
class Model:
    def __init__(self, dados):
        self.dados = dados

    def adicionar(self, obj):
        self.dados.append(obj)
        return obj

    def excluir(self, obj) -> bool:
        raise NotImplementedError("Implemente a função de excluir!")

    def pesquisar(self, chave = "", valor = ""):
        return self.dados


# Classe Model para Veículos
class VeiculoModel(Model):
    def __init__(self):
        super().__init__(veiculos)

    #TODO: Implementar regra validando se a placa existe
    def adicionar(self, obj):
        return super().adicionar(obj)

    def excluir(self, obj) -> bool:
        indice_veiculo = -1
        for indice in range(len(self.dados) - 1):
            if self.dados[indice].placa == obj.placa:
                indice_veiculo = indice
        if indice_veiculo >= 0:
            self.dados.pop(indice_veiculo)
            return True       
        return False

    def pesquisar(self, chave = "", valor = ""):
        if (chave == "") and (valor == ""):
            return super().pesquisar()
        else:
            if hasattr(Veiculo(), chave):
                for veiculo in self.dados:
                    if getattr(veiculo, chave) == valor:
                        return [veiculo]
            return []
        

# Classe Model para Cliente
class ClienteModel(Model):
    # TODO: Implementar ClientModel
    def __init__(self):
        super().__init__(clientes)


# Classe Model para Reserva
class ReservaModel(Model):
    #TODO: Implementar ReservaModel
    def __init__(self):
        super().__init__(reservas)

