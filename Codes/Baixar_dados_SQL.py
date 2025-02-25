import mysql.connector
import subprocess
import datetime

hoje = datetime.datetime.now().strftime('%Hh%Mm%Ss-%d-%m-%Y')

# Configurações do banco de dados
db_config = {
    'user': 'root',
    'password': 'Athos1324',
    'host': 'localhost',
    'database': 'chapada_imperial'
}

# Conexão com o banco de dados
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

# Consulta SQL
#'/home/gama/Documentos/Faculdade/Rudi/Documentos TCC/Dados Extraidos/{hoje}.csv'
query = f"SELECT * INTO OUTFILE '/tmp/{hoje}.csv' FIELDS TERMINATED BY '\;' ENCLOSED BY '\"' LINES TERMINATED BY '\\n' FROM medidor1;"
cursor.execute(query)
try:
    subprocess.run(['cp', f'/tmp/{hoje}.csv', f'/home/gama/Documentos/1.Projeto/TCC\ 01/Documentos\ TCC/{hoje}.csv'])

    # Apagando o arquivo temporário .csv
    subprocess.run(['rm', f'/tmp/{hoje}.csv'])

    print('Dados extraídos com sucesso!')

except:
    print("Não conseguiu baixar os dados")

#output_file = '/home/gama/Documentos/Faculdade/Rudi/dados_banco.csv'


# Fechando a conexão
cursor.close()
conn.close()
