#!/usr/bin/python3
# -*- coding: utf-8 -*- 

# Saiba mais sobre a linha 1: https://mateusmuller.me/2019/08/14/shebang-declarar-o-compilador-em-shell-script/
# Saiba mais sobre a linha 2: https://peps.python.org/pep-0263/

from datetime import datetime
from enum import Enum

from ..model.model import VeiculoModel, ClienteModel, ReservaModel
from ..entidades.veiculo import Veiculo, Combustivel
from ..utils.mensagem import Log

# Enumarator (enum) para opções do menu
class OpcoesMenuPrincipal(Enum):
    NONE = -1 # Valor invalido
    SAIR = 0 # Sair
    LISTA_VEICULOS = 1 # Listar Veículos"
    CADASTRAR_VEICULO = 2 # Cadastrar Veículo"
    EXCLUIR_VEICULO = 3 # Excluir Veículo"
    ALTERAR_PRECO_DIARIA = 4 # Alterar preço R$ da diária"
    LISTA_CLIENTES = 5 # Listar Clientes"
    CADASTRAR_CLIENTE = 6 # Cadastrar Cliente"
    EXCLUIR_CLIENTE = 7 # Excluir Cliente"
    LISTA_RESERVAS = 8 # Listar Reservas"
    CADASTRAR_RESERVA = 9 # Nova Reserva"
    ALTERAR_CHECKIN = 10 # Fazer Check-in"
    ALTERAR_CHECKOUT = 11 # Fazer Check-out"

def resize_texto(texto, tamanho):
    if tamanho > 0:
        return (texto+" "*tamanho)[0:tamanho]
    else:
        return ""

# TODO: Enviar função show_opcoes_combustivel para o contexto do Combustível
def show_opcoes_combustivel():
    i = 1
    for combustivel in Combustivel:
        print(f"\t{i} - {combustivel.value}")
        i += 1

# TODO: Enviar função indice_para_combustivel para o contexto do Combustível
def indice_para_combustivel(indice):
    i = 1
    for combustivel in Combustivel:
        if i == indice:
            return combustivel
        i += 1
    return None

# Função para listar veículos 
def show_lista_veiculos():
    model = VeiculoModel()
    lista_de_veiculos = model.pesquisar();
    if len(lista_de_veiculos) == 0:
        Log.alerta("Não há veículos cadastrados!")
    else:
        # Cabeçalho da tabela
        print(f"+-------+{"-"*10                   }+{"-"*15                    }+{"-"*10                     }+{"-"*10  }+")
        print(f"| Placa |{resize_texto("Marca", 10)}|{resize_texto("Modelo", 15)}|{resize_texto("Combust.",10)}|Pr. Diária|")
        print(f"+-------+{"-"*10                   }+{"-"*15                    }+{"-"*10                     }+{"-"*10  }+")
        # Dados da tabela
        for v in lista_de_veiculos:
            print(f"|{resize_texto(v.placa,7)}|{resize_texto(v.marca,10)}|{resize_texto(v.modelo, 15)}|{resize_texto(v.combustivel.value, 10)}|{resize_texto(f"R$ {v.preco_diaria:.2f}",10)}|")
        print(f"+-------+{"-"*10                   }+{"-"*15                    }+{"-"*10                     }+{"-"*10  }+")

def show_lista_clientes():
    model = ClienteModel()
    lista_de_clientes = model.pesquisar()
    if len(lista_de_clientes) == 0:
        Log.alerta("Não há clientes cadastrados!")
    else:
        # Cabeçalho da tabela
        print(f"+{"-"*15                 }+{"-"*25                  }+{"-"*10                      }+-----+")
        print(f"|{resize_texto("CNH", 15)}|{resize_texto("Nome", 25)}|{resize_texto("Dt.Nasc.", 10)}|Anos |")
        print(f"+{"-"*15                 }+{"-"*25                  }+{"-"*10                      }+-----+")
        # Dados da tabela
        for c in lista_de_clientes:
            print(f"|{resize_texto(c.cnh,15)}|{resize_texto(c.nome,25)}|{resize_texto(c.dt_nasc.strftime("%d/%m/%Y"), 10)}|{resize_texto(str(c.obter_idade()),5)}|")
        print(f"+{"-"*15                 }+{"-"*25                  }+{"-"*10                     }+-----+")

def show_lista_reservas():
    model = ReservaModel()
    lista_de_reservas = model.pesquisar()
    if len(lista_de_reservas) == 0:
        Log.alerta("Não há reservas cadastradas!")
    else:
        # TODO: Implementar visão de tabela para reservas
        pass

# Função para cadastrar veículo
def show_cadastro_veiculo():
    print(f"{"-"*20} Cadastro de Veículo {"-"*20}")
    veiculo = Veiculo()
    try:
        # Solicita que informe a placa
        veiculo.placa =  input("Informe a Placa: ").upper()
        # Solicita que informe a marca
        veiculo.marca =  input("Informe a Marca: ").upper()
        # Solicita que informe o modelo
        veiculo.modelo =  input("Informe o Modelo: ").upper()
        # Solicita que informe o combustivel
        show_opcoes_combustivel()
        combustivel = None
        while combustivel == None:
            indice_combustivel = int(input("Informe o nº do Combustível: "))
            combustivel = indice_para_combustivel(indice_combustivel)                
        veiculo.combustivel =  combustivel
        # Solicita que informe a preço                                    
        veiculo.preco_diaria =  float(input("Informe o preço da diária (R$): ").replace(",","."))
    except:
        Log.error("Problema no cadastro de veículo!")
        return None

    model = VeiculoModel()
    try:
        model.adicionar(veiculo)
        Log.informacao("Veículo cadastrado com sucesso!")
        print(veiculo)        
    except:
        Log.error("Não foi possível cadastradar o veículo!")
    print("-"*61)

# Função para excluir veículo
def show_exclusao_veiculo():
    print(f"{"-"*20} Exclusão de Veículo {"-"*20}")
    placa = input("Informe a placa do veículo:").upper()
    veiculo = Veiculo(placa=placa)
    try:
        if not VeiculoModel().excluir(veiculo):
            raise
        Log.informacao("Veículo excluído!")
    except:
        Log.error("Não foi possível excluir o veículo!")       
    print("-"*61)

# Função para mostrar opções
def show_menu_principal():
    print("\x1b[2J") #limpar tela
    print("*"*5,"SmartRent2Nexts v0.0.1","*"*5,)
    print("Dt: {:%d-%m-%Y}".format(datetime.now()))

    operacao = OpcoesMenuPrincipal.NONE
    while operacao != OpcoesMenuPrincipal.SAIR:       
        print("Opções para veículos:")
        print("\t1 - Listar Veículos")
        print("\t2 - Cadastrar Veículo")
        print("\t3 - Excluir Veículo")
        print("\t4 - Alterar preço R$ da diária")
        print("Opções para clientes:")
        print("\t5 - Listar Clientes")
        print("\t6 - Cadastrar Cliente")
        print("\t7 - Excluir Cliente")
        print("Opções para reservas:")
        print("\t8 - Listar Reservas")
        print("\t9 - Nova Reserva")
        print("\t10 - Fazer Check-in")
        print("\t11 - Fazer Check-out")
        print("Opções da aplicação:")
        print("\t0 - Sair")

        try:
            operacao = OpcoesMenuPrincipal(int(input("Informe o número da opção: ")))
        except:
            operacao = OpcoesMenuPrincipal.NONE
            print("Error: Opção inválida!")
            continue
        
        match operacao:
            case OpcoesMenuPrincipal.LISTA_VEICULOS:
                show_lista_veiculos()                   
            case OpcoesMenuPrincipal.CADASTRAR_VEICULO:
                show_cadastro_veiculo()
            case OpcoesMenuPrincipal.EXCLUIR_VEICULO:
                show_exclusao_veiculo()
            case OpcoesMenuPrincipal.ALTERAR_PRECO_DIARIA:
                Log.error("Opção não implementada - Em desenvolvimento!")
            case OpcoesMenuPrincipal.LISTA_CLIENTES:
                show_lista_clientes()
            case OpcoesMenuPrincipal.CADASTRAR_CLIENTE:
                Log.error("Opção não implementada - Em desenvolvimento!")
            case OpcoesMenuPrincipal.EXCLUIR_CLIENTE:
                Log.error("Opção não implementada - Em desenvolvimento!")
            case OpcoesMenuPrincipal.LISTA_RESERVAS:
                show_lista_reservas()
            case OpcoesMenuPrincipal.CADASTRAR_RESERVA:
                Log.error("Opção não implementada - Em desenvolvimento!")
            case OpcoesMenuPrincipal.ALTERAR_CHECKIN:
                Log.error("Opção não implementada - Em desenvolvimento!")
            case OpcoesMenuPrincipal.ALTERAR_CHECKOUT:
                Log.error("Opção não implementada - Em desenvolvimento!")

# Condição para não executar como script
# quando ser importado por outro script.
# - Executará quando script: `python SmartRent2Nexts.py`
# - Não executará como biblioteca: `import SmartRent2Nexts`
if(__name__ == '__main__'):
    show_menu_principal()
