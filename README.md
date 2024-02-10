# SmartRent2Nexts

Sistema para locação de automóveis em python.

## Funcionalidades
- Gestão de veículos
    - Listar veículos
    - Cadastrar veículo
    - Excluir veículo
    - Alterar preço da diária
- Gestão de clientes
    - Listar clientes
    - Cadastrar cliente
    - Excluir cliente
- Gestão de reservas
    - Cadastrar reserva
        - Selecionando carro
        - Selecionando cliente
        - Informar a data da reserva
        - Informar a quantidade de dias
        - Mostrar preço total ao final
        - *Verificar disponibilidade
    - Fazer checkin da reserva
    - Fazer checkout da reserva
    - Visualizar reservas em aberto
- Calendário
    - Visualizar reservas
        - Informar o dia
- Simulador de Preço
    - Informar o carro e a quantidade de dias para retornar o preço total.

## Entidades

### Veiculos
- Placa
- Marca
- Modelo
- Combustível (Gasolina, Alcool, Diesel, Flex, Elétrico)
- Preço Diária (R$)

##### Dados iniciais
| Placa   | Marca     | Modelo  | Combust. | R$ Diária |
|:-------:|:----------|:--------|----------|:---------:|
| ABC1D23 | FIAT      | UNO     | Alcool   | R$ 99,89  |
| QWE4R56 | CHEVROLET | PRISMA  | Flex     | R$ 105,89 |
| ASD7F89 | TESLA     | MODEL Y | Elétrico | R$ 159,89 |
| WWW8F88 | FORD      | RANGER  | Diesel   | R$ 189,89 |

### Clientes
- CNH
- Nome
- Dt. Nascimento
    
##### Dados iniciais
| CNH         | Nome              | Dt. Nasc.  |
|-------------|-------------------|------------|
| 00000000000 | Ada Lovelace      | 10/12/1815 |
| 55555555555 | Alan Turing       | 23/06/1912 |
| 44444444444 | Grace Hopper      | 09/12/1906 |
| 22222222222 | Guido van Rossum  | 31/01/1956 |
| 33333333333 | Margaret Hamilton | 17/08/1936 |
| 11111111111 | Tim Berners-Lee   | 08/06/1955 |

### Reservas
- Placa
- CNH
- Dt. Reserva
- Qt. Diárias
- Preço Diária
- Dt. Checkin *Data da retirada do veículo
- Dt. Checkout *Data da devolução do veículo

##### Dados iniciais
| Placa | CNH       | Dt. Reserva | Qt. Dia | R$ Dia  | Dt. Checkin | Dt. Checkout |
|-------|-----------|-------------|:-------:|---------|:-----------:|:------------:|
|ABC1D23|22222222222| 01/01/2024  | 4       |R$ 99,89 | 01/01/2024  | 04/01/2024   |
|ABC1D23|55555555555| 05/01/2024  | 1       |R$ 59,99 | 05/01/2024  | 06/01/2024   |
|WWW8F88|11111111111| 03/03/2024  | 5       |R$ 189,89|             |              |
|QWE4R56|44444444444| 10/02/2024  | 15      |R$ 99,89 | 10/02/2024  |              |
|ASD7F89|00000000000| 05/02/2024  | 3       |R$ 159,89| 05/02/2024  | 08/02/2024   |
|QWE4R56|33333333333| 26/02/2024  | 1       |R$ 105,89|             |              |

## Desafio
1. Procure pelos comentários com `# TODO:` e veja o que há para ser feito!

Exemplo:

1. Dentro da pasta _entidades_ no arquivo `veiculo.py` há uma classe Combustivel e deve ser retirada do arquivo:
    * Crie um arquivo `combustivel.py`
    * Recorte a classe _Combustivel_ e cole no arquivo
    * Importe a classe _Combustivel_ no script de `veiculo.py`
    * Execute os testes para conferir se tudo está Ok!
    * Execute o programa!
1. No aquivo de teste `test\model.veiculo.text.py` há o teste *test_pesquisa_com_parametro_deve_retornar_list_com_um_elemento* com varias validações, separe as validações deixando apenas uma em cada teste!

    
## Instruções

1. Crie um _branch_ deste repositório com o formato: *branch-[SEU NOME]*
2. Realize o _clone_ deste repositório na sua máquina (`git clone [URL]`), entre na pasta criada no clone (`cd [PASTA]`) e
3. Faça o _checkout_ para seu _branch_ (criado no passo 1) (`git checkout branch-[SEU NOME]`)
4. Faça o solicitado no tópico **Desafio**, quando finalizar
5. Realize o _commit_ das alterações (`git commit -a -m "[SUA MENSAGEM]"`)
6. Faça o _push_ para enviar as alterações (`git push`)
7. Crie o _pull request_ para o _branch_ principal (`main`)

## Obs:
* _CRUD: Create (Cadastro), Read(Leitura), Update(Alterar), Delete(Excluir)_
* Utilize as extensões informadas abaixo para melhorar a utilização do VsCode
* Execução dos testes:
    - `python test\[arquivo].test.py`

## Referências
1. venv— Criação de ambientes virtuais <https://docs.python.org/pt-br/3/library/venv.html>
1. Python String format() Tutorial <https://www.datacamp.com/tutorial/python-string-format>
1. enum — Suporte a enumerações <https://docs.python.org/pt-br/3/library/enum.html>
1. unittest — Framework de Testes Unitários <https://docs.python.org/pt-br/3/library/unittest.html>
1. SHEBANG: Declarar o compilador em Shell Script <https://mateusmuller.me/2019/08/14/shebang-declarar-o-compilador-em-shell-script/>
1. Python Tutorial <https://www.geeksforgeeks.org/python-programming-language/?ref=lbp>

## Extensões recomendadas para o VsCode
1. python <https://marketplace.visualstudio.com/items?itemName=ms-python.python>
1. isort <https://marketplace.visualstudio.com/items?itemName=ms-python.isort>
1. debugpy <https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy>
1. vscode-pylance <https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance>
1. todo-tree <https://marketplace.visualstudio.com/items?itemName=Gruntfuggly.todo-tree>
