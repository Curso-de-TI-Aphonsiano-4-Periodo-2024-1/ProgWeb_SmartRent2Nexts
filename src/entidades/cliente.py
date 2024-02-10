from datetime import datetime
# Classe CLiente
# Atributos de um cliente:
# | CNH | Nome | Dt. Nasc. |
class Cliente:
    # construtor da classe Cliente
    def __init__(self, cnh = "", nome = "", dt_nasc = datetime.now()):
        self.cnh = cnh
        self.nome = nome
        self.dt_nasc = dt_nasc

    def obter_idade(self) -> int:
        return datetime.now().year - self.dt_nasc.year

    # TODO: Implementar __str__
    def __str__(self) -> str:
        pass