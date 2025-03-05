# script_modbus.py
import subprocess
import sys

# Verifica e instala as bibliotecas necessárias
def instalar_bibliotecas():
    bibliotecas = ["pymodbus", "mysql-connector-python"]
    for biblioteca in bibliotecas:
        try:
            __import__(biblioteca.replace("-", "_"))  # mysql-connector-python usa underline no import
        except ImportError:
            print(f"Instalando {biblioteca}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", biblioteca])

# Instala as bibliotecas necessárias
instalar_bibliotecas()

from pymodbus.client.sync import ModbusSerialClient as ModbusClient # type: ignore
from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadDecoder

# Lista para armazenar as variáveis
variaveis = []

def cria_var(nome, offset):
    """
    Função para adicionar uma variável à lista de variáveis.
    :param nome: Nome da variável (string).
    :param offset: Offset do registrador (int).
    """
    variaveis.append({"nome": nome, "offset": offset})

def coletar_variaveis_modbus():
    """
    Função para coletar as variáveis do dispositivo Modbus.
    Retorna um dicionário com os valores lidos.
    """
    # Configuração do cliente Modbus RTU
    client = ModbusClient(method='rtu', port='/dev/ttyUSB0', baudrate=9600, stopbits=1, bytesize=8, parity='N', timeout=1)

    # Conectar ao dispositivo Modbus
    connection = client.connect()

    if connection:
        print("Conexão estabelecida com sucesso!")
        
        # Dicionário para armazenar os valores lidos
        valores = {}

        # Loop para ler cada variável
        for var in variaveis:
            # Ler o valor do registrador (assumindo que cada valor ocupa 2 registradores)
            response = client.read_holding_registers(address=var["offset"], count=2, unit=1)
            
            if response.isError():
                print(f"Erro ao ler o registrador {var['offset']}: {response}")
            else:
                # Decodificar o valor lido
                decoder = BinaryPayloadDecoder.fromRegisters(response.registers, byteorder=Endian.Big, wordorder=Endian.Big)
                valor = decoder.decode_32bit_float()
                
                # Armazenar o valor no dicionário
                valores[var["nome"]] = valor
                print(f"{var['nome']}: {valor}")

        # Fechar a conexão Modbus
        client.close()
        return valores

    else:
        print("Falha ao conectar ao dispositivo Modbus.")
        return None