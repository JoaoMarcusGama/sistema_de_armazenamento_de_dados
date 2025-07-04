# script_banco_dados.py
import subprocess
import sys
import math
import mysql.connector
from datetime import datetime
import time
from script_modbus import coletar_variaveis_modbus, cria_var

# Adiciona as variáveis dinamicamente
cria_var("tensao_L1_N", 1)
cria_var("tensao_L2_N", 3)
cria_var("tensao_L3_N", 5)
cria_var("tensao_L1_L2", 7)
cria_var("tensao_L2_L3", 9)
cria_var("tensao_L3_L1", 11)
cria_var("corrente_L1", 13)
cria_var("corrente_L2", 15)
cria_var("corrente_L3", 17)
cria_var("potencia_aparente_L1", 19)
cria_var("potencia_aparente_L2", 21)
cria_var("potencia_aparente_L3", 23)
cria_var("potencia_ativa_L1", 25)
cria_var("potencia_ativa_L2", 27)
cria_var("potencia_ativa_L3", 29)
cria_var("potencia_reativa_L1", 31)
cria_var("potencia_reativa_L2", 33)
cria_var("potencia_reativa_L3", 35)
cria_var("corrente_condutor_neutro", 37)
cria_var("frequencia", 39)

def tratar_nan(valor):
    """Converte valores NaN para 0, mantém outros valores inalterados"""
    if valor is None:
        return None
    try:
        # Verifica se é NaN (usando math.isnan para float ou string 'nan')
        if isinstance(valor, float) and math.isnan(valor):
            return 0.0
        if isinstance(valor, str) and valor.lower() == 'nan':
            return 0.0
        return valor
    except (TypeError, ValueError):
        return valor

def salvar_no_banco(valores):
    """
    Função para salvar os valores no banco de dados.
    """
    try:
        # Conectar ao banco de dados MariaDB
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="pico_central_hidro",
            database="chapada_imperial"
        )
        cursor = db.cursor()

        # Tratar todos os valores para converter NaN em 0
        valores_tratados = {k: tratar_nan(v) for k, v in valores.items()}

        # Inserir os valores no banco de dados
        query = """
        INSERT INTO multimedidor (
            datahora, tensao_L1_N, tensao_L2_N, tensao_L3_N, tensao_L1_L2, tensao_L2_L3, tensao_L3_L1,
            corrente_L1, corrente_L2, corrente_L3, potencia_aparente_L1, potencia_aparente_L2,
            potencia_aparente_L3, potencia_ativa_L1, potencia_ativa_L2, potencia_ativa_L3,
            potencia_reativa_L1, potencia_reativa_L2, potencia_reativa_L3, corrente_condutor_neutro, frequencia
        ) VALUES (
            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
        )
        """
        valores_db = (
            datetime.now(),  # Hora atual
            valores_tratados.get("tensao_L1_N", None),
            valores_tratados.get("tensao_L2_N", None),
            valores_tratados.get("tensao_L3_N", None),
            valores_tratados.get("tensao_L1_L2", None),
            valores_tratados.get("tensao_L2_L3", None),
            valores_tratados.get("tensao_L3_L1", None),
            valores_tratados.get("corrente_L1", None),
            valores_tratados.get("corrente_L2", None),
            valores_tratados.get("corrente_L3", None),
            valores_tratados.get("potencia_aparente_L1", None),
            valores_tratados.get("potencia_aparente_L2", None),
            valores_tratados.get("potencia_aparente_L3", None),
            valores_tratados.get("potencia_ativa_L1", None),
            valores_tratados.get("potencia_ativa_L2", None),
            valores_tratados.get("potencia_ativa_L3", None),
            valores_tratados.get("potencia_reativa_L1", None),
            valores_tratados.get("potencia_reativa_L2", None),
            valores_tratados.get("potencia_reativa_L3", None),
            valores_tratados.get("corrente_condutor_neutro", None),
            valores_tratados.get("frequencia", None)
        )

        cursor.execute(query, valores_db)
        db.commit()

        print("Dados inseridos no banco de dados com sucesso!")

        # Fechar a conexão com o banco de dados
        cursor.close()
        db.close()

    except mysql.connector.Error as err:
        print(f"Erro ao conectar ou inserir no banco de dados: {err}")

# Loop principal
if __name__ == "__main__":
    while True:
        # Coletar variáveis do Modbus
        valores = coletar_variaveis_modbus()

        if valores:
            # Salvar os valores no banco de dados
            salvar_no_banco(valores)

        # Aguardar 1 segundo antes da próxima leitura
        time.sleep(0.5)
