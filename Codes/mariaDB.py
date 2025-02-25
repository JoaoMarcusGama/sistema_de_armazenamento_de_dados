# Bibliotecas que usaremos para funcionar o código
import mysql.connector
import time
import random

# Conectando à base de dados
## Esses valores mudam conforme a configuração do banco de dados
base = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Athos1324',
    database='chapada_imperial'
)

# Pegando as variáveis
cur = base.cursor()

while True:
    try:
        t_media = []
        c_media = []

        datahora_ini = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        start_time = time.time()

        # Coletando dados por um intervalo de tempo de 1 segundo
        while time.time() - start_time < 1:
            tensão = random.randrange(20, 220)
            corrente = random.randrange(2, 100)
            t_media.append(tensão)
            c_media.append(corrente)

        # Calculando a média dos valores coletados
        tensão_media = sum(t_media) / len(t_media)
        corrente_media = sum(c_media) / len(c_media)
        fase = '1'

        # Salvando os valores
        query = "INSERT INTO medidor1 (datahora, tensao, corrente, fase) VALUES (%s, %s, %s, %s)"
        data = (datahora_ini, tensão_media, corrente_media, fase)
        cur.execute(query, data)

        # Salvando no banco de dados
        base.commit()

        # Lendo a base
        cur.execute('SELECT * FROM medidor1')

        for (data, tensão, corrente, fase) in cur:
            print(f'{data}, {tensão} V, {corrente} A, {fase}')

    except KeyboardInterrupt:
        break