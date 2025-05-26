# Sistema de Armazenamento de Dados para Usina de Geração de Energia Elétrica

Este repositório tem como intuito documentar o processo de instalação e configuração do Raspberry PI e seus códigos, ambos utilizados para armazenar os dados coletados por um multimedidor instalado em uma pico-central hidrelétrica de uma comunidade isolada do sistema de distribuição de energia elétrica.
# 1. Código do Banco de Dados
O código do banco de dados que será utilizado é o que está na pasta "Codes" e se chama [script.sql](Codes/script.sql). Os valores das colunas que estão no banco de dados serão as necessárias para o estudo de carga proposto no TCC. Para adesão de qualquer outra coluna, basta olhar no manual do multimedidor que estiver usando. No caso deste trabalho [o link do manual em português é esse aqui](https://cache.industry.siemens.com/dl/files/976/37881976/att_834838/v1/sentron_pac3100_manual_pt_03_pt-BR.pdf).

As variáveis e seus respectivos *offsets* e unidades de medida são:

| Variável                        | Offset | Unidade de medida |
|----------------------------------|--------|-------------------|
| Tensão L1 - N                   | 1      | V                 |
| Tensão L2 - N                   | 3      | V                 |
| Tensão L3 - N                   | 5      | V                 |
| Tensão L1 - L2                  | 7      | V                 |
| Tensão L2 - L3                  | 9      | V                 |
| Tensão L3 - L1                  | 11     | V                 |
| Corrente L1                     | 13     | A                 |
| Corrente L2                     | 15     | A                 |
| Corrente L3                     | 17     | A                 |
| Potência Aparente L1            | 19     | VA                |
| Potência Aparente L2            | 21     | VA                |
| Potência Aparente L3            | 23     | VA                |
| Potência Ativa L1               | 25     | W                 |
| Potência Ativa L2               | 27     | W                 |
| Potência Ativa L3               | 29     | W                 |
| Potência Reativa L1 (Q1)        | 31     | var               |
| Potência Reativa L2 (Q2)        | 33     | var               |
| Potência Reativa L3 (Q3)        | 35     | var               |
| Corrente do condutor neutro     | 37     | A                 |
| Frequência                      | 39     | Hz                |


Os códigos seguintes ainda não foram implementados.
# 2. Códigos e funções que obtém e armazenam os dados do multimedidor (.py)

Como o sistema ficara instalado para outras análises, buscando facilitar qualquer futura alteração no código, optou-se por criar uma função que facilita as configurações do offset do multimedidor ([script_modbus.py](Codes/script_modbus.py)) e outro que junta essa configuração e salva os dados coletados no banco de dados SQL ([script_banco_dados.py](Codes/script_banco_dados.py)). Executando esses dois, o sistema pega os dados e os armazena no banco de dados, permitindo adição de novos parâmetros ou exclusão de outros.

# 3. Código que configura e instala tudo quase que de forma automática (.sh)
## 3.1 Instalando o MariaDB e configurando o banco de dados.

O código intitulado [install_and_config.sh](Codes/install_and_config.sh) instala do banco de dados que será utilizado (MariaDB), configura o mesmo e o *database* utilizado [script.sql](Codes/script.sql) chamado "chapada_imperial", que foi melhor explicado no tópico [1. Código do Banco de Dados](README#1. Código do Banco de Dados).

As configurações pré configuradas são:

| Variável              | Como foi configurado                                                                           |
| --------------------- | ---------------------------------------------------------------------------------------------- |
| Nome do usuário       | root                                                                                           |
| Senha                 | pico_central_hidro                                                                             |
| Usuários anônimos     | Todos foram removidos                                                                          |
| Bancos de Teste       | Todos foram removidos                                                                          |
| Login Remoto          | Ativado (Poder acessar o banco de dados por meio de outro computado por meio do protocolo ssh) |
| Privilégios de tabela | Recarregado                                                                                    |

Configurado desse jeito, para acessar o banco de dados pelo terminal basta rodar o comando ``` mysql -u root -ppico_central_hidro ```para acessar o banco de dados.

```Precisa escrever '-ppico_central_hidro' de forma junta para entender que é a senha. Se colocar separado, ele entende 'pico_central_hidro' como sendo o nome do banco de dados```

# 4. Dos códigos python

Para rodar os códigos, é necessário criar um ```.venv``` na raspberry. No nosso caso, foi criado esse venv por meio do comando ```python -m venv monitoramento``` e, após criado, para permitir a execução do código e das bibliotecas necessárias, usa-se o comando ```source /opt/sistema_de_armazenamento_de_dados/Codes/monitoramento/bin/activate```.

Com isso, foi criado o ambiente virtual que rodará o código e as bibliotecas necessárias para funcionar o sistema. 

As bibliotecas necessárias se encontram na pasta Codes com o nome de ```requirements.txt``` e que podem ser instalados de forma automática por meio do comando ```pip3 install -r requirements.txt```. Com isso, pode-se ir para a autoinicialização.

# 4. Iniciando o código python ao iniciar o sistema

Com o código localizado no caminho */opt/sistema_de_armazenamento_de_dados/Codes/script_banco_dados.py*, para que o mesmo possa ser iniciado na hora que o sistema é ligado, precisa-se seguir o seguinte passo a passo:

1. Como o usuário pico_central_hidrelétrica, digitar no terminal o comando ```crontab -e```. Com isso, abrirá opções de editores de terminal. Selecione o editor nano.

2. Com o documento aberto, vá até o final do mesmo e, em uma linha nova, coloque o comando ```@reboot /opt/sistema_de_armazenamento_de_dados/Codes/monitoramento/bin/python /opt/sistema_de_armazenamento_de_dados/Codes/script_banco_dados.py &```. Com isso, clique ***Ctrl + X***, depois ***Y*** e depois ***Enter***.

3. Após isso, reinicie o sistema com o comando ```sudo reboot```.