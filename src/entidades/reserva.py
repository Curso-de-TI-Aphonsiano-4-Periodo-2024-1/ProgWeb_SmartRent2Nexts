from datetime import datetime
# Classe Reserva
# Atributos de uma reserva:
# | Placa | CNH | Dt. Reserva | Qt. Dia | R$ Dia  | Dt. Checkin | Dt. Checkout |
class Reserva:
    def __init__(self, cnh = "", placa = "", preco_diaria = 0.00, qt_dias = 0, dt_reserva = datetime.now(), dt_checkin=None, dt_checkout = None):
        self.cnh = cnh
        self.placa = placa
        self.preco_diaria = preco_diaria
        self.qt_dias = qt_dias
        self.dt_reserva = dt_reserva
        self.dt_checkin = dt_checkin
        self.dt_checkout = dt_checkout
    
    #TODO: Implementar __str__
    def __str__(self) -> str:
        pass