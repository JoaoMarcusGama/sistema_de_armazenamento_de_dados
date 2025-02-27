#!/bin/bash

# Verifica se o script está sendo executado como root
if [[ $EUID -ne 0 ]]; then
    echo "Este script deve ser executado como root ou com sudo."
    exit 1
fi

# Atualiza os pacotes e instala o MariaDB no Raspberry Pi OS
apt update
apt install -y mariadb-server mariadb-client

# Habilita e inicia o serviço do MariaDB
systemctl enable mariadb
systemctl start mariadb

# Exibe o status do serviço
systemctl status mariadb --no-pager

echo "Instalação do MariaDB concluída no Raspberry Pi OS!"

# Automatiza a configuração segura do MariaDB
echo "Configurando segurança do MariaDB..."
mysql -u root <<EOF
ALTER USER 'root'@'localhost' IDENTIFIED BY 'pico_central_hidro';
DELETE FROM mysql.user WHERE User='';  # Remove usuários anônimos
DROP DATABASE IF EXISTS test;  # Remove o banco de dados de teste
DELETE FROM mysql.db WHERE Db='test' OR Db='test\_%';  # Remove permissões associadas ao banco de teste
FLUSH PRIVILEGES;  # Recarrega os privilégios das tabelas
EOF

echo "Configuração do MariaDB concluída!"

# Baixa o repositório do GitHub
git clone https://github.com/JoaoMarcusGama/sistema_de_armazenamento_de_dados.git /opt/sistema_de_armazenamento_de_dados

# Executa o código SQL presente no repositório
mysql -u root -ppico_central_hidro < /opt/sistema_de_armazenamento_de_dados/Codes/script.sql

echo "Execução do script SQL concluída!"