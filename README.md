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
# 3. Código que configura e instala tudo quase que de forma automática (.sh)
