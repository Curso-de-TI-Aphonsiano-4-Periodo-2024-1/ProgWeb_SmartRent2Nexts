from datetime import datetime

from ..entidades.veiculo import Veiculo, Combustivel
from ..entidades.cliente import Cliente
from ..entidades.reserva import Reserva

# TODO: Extrair função para pasta utils
d = lambda data: datetime.strptime(data, "%d/%m/%Y")

# TODO: Gravar em aquivo ou banco de dados os dados!
""""
| Placa   | Marca     | Modelo  | Combust. | R$ Diária |
|:-------:|:----------|:--------|----------|:---------:|
| ABC1D23 | FIAT      | UNO     | Alcool   | R$ 99,89  |
| QWE4R56 | CHEVROLET | PRISMA  | Flex     | R$ 105,89 |
| ASD7F89 | TESLA     | MODEL Y | Elétrico | R$ 159,89 |
| WWW8F88 | FORD      | RANGER  | Diesel   | R$ 189,89 |
"""
veiculos = [
    Veiculo("ABC1D23","FIAT","UNO", Combustivel.ALCOOL, 99.89),
    Veiculo("QWE4R56","CHEVROLET", "PRISMA",  Combustivel.FLEX, 105.89),
    Veiculo("ASD7F89","TESLA", "MODEL Y", Combustivel.ELETRICO, 159.89),
    Veiculo("WWW8F88","FORD","RANGER", Combustivel.DIESEL, 189.89)
]

"""
| CNH         | Nome              | Dt. Nasc.  |
|-------------|-------------------|------------|
| 00000000000 | Ada Lovelace      | 10/12/1815 |
| 55555555555 | Alan Turing       | 23/06/1912 |
| 44444444444 | Grace Hopper      | 09/12/1906 |
| 22222222222 | Guido van Rossum  | 31/01/1956 |
| 33333333333 | Margaret Hamilton | 17/08/1936 |
| 11111111111 | Tim Berners-Lee   | 08/06/1955 |
"""
clientes = [   
    Cliente("00000000000", "Ada Lovelace", d("10/12/1815")),
    Cliente("55555555555", "Alan Turing", d("23/06/1912")),
    Cliente("44444444444", "Grace Hopper", d("09/12/1906")),
    Cliente("22222222222", "Guido van Rossum", d("31/01/1956")),
    Cliente("33333333333", "Margaret Hamilton", d("17/08/1936")),
    Cliente("11111111111", "Tim Berners-Lee", d("08/06/1955"))
]

"""
|ABC1D23|22222222222| 01/01/2024  | 4       |R$ 99,89 | 01/01/2024  | 04/01/2024   |
|ABC1D23|55555555555| 05/01/2024  | 1       |R$ 59,99 | 05/01/2024  | 06/01/2024   |
|WWW8F88|11111111111| 03/03/2024  | 5       |R$ 189,89|             |              |
|QWE4R56|44444444444| 10/02/2024  | 15      |R$ 99,89 | 10/02/2024  |              |
|ASD7F89|00000000000| 05/02/2024  | 3       |R$ 159,89| 05/02/2024  | 08/02/2024   |
|QWE4R56|33333333333| 26/02/2024  | 1       |R$ 105,89|             |              |
"""
reservas = [    
    Reserva("22222222222","ABC1D23", 99.89,  4, d("01/01/2024"), d("01/01/2024"), d("04/01/2024")),
    Reserva("55555555555","ABC1D23", 59.99,  1, d("05/01/2024"), d("05/01/2024"), d("06/01/2024")),
    Reserva("11111111111","WWW8F88", 189.89, 5, d("03/03/2024")),
    Reserva("44444444444","QWE4R56", 99.89,  15, d("10/02/2024"), d("10/02/2024")),
    Reserva("00000000000","ASD7F89", 159.89, 3, d("05/02/2024"), d("05/02/2024"), d("08/02/2024")),
    Reserva("33333333333","QWE4R56", 105.89, 1, d("26/02/2024"))
]