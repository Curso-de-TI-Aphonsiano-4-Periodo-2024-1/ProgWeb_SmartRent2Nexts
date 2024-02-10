import enum

class Combustivel(enum.Enum):
    GASOLINA = "Gasolina"
    ALCOOL = "Álcool"
    DIESEL = "Diesel"
    FLEX = "Flex"
    ELETRICO = "Elétrico"
# Classe Veículo
# Atributos de um veículo:
# | Placa | Marca | Modelo | Combust. | R$ Diária |
class Veiculo:
    def __init__(self, placa = "", marca = "", modelo = "", combustivel = Combustivel.FLEX, preco_diaria=0.00):
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.combustivel = combustivel
        self.preco_diaria = preco_diaria
    
    def __str__(self) -> str:
        return f"""_Veículo________________
    Placa: {self.placa}
    Marca: {self.marca}
    Modelo: {self.modelo}
    Combustivel: {self.combustivel.value}
    Preço Diária (R$): {self.preco_diaria}
    """