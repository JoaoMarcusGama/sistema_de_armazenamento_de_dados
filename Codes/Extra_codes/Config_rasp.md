# Configuração do Rasp e funcionamento dos arquivos

___

## Raspberry

A configuração do Raspberry se deu da forma padrão de instalação [presente neste link](https://www.raspberrypi.com/documentation/computers/getting-started.html#install-an-operating-system).
Com esse passo inicial, basta instalar o **mariadb** por meio do terminal. Vale lembrar que o Rapberry que estamos utilizando se trata de um mini computador e o *Raspibian* (sistema operacional que roda nele) é um sistema Linux derivado da distibuição debian. Primeiro, vamos configurar o acesso ao rasp.

### Acesso por meio do ssh

Com a instalação do Raspberry feita, para acessar a mesma de forma remota (outro computador), é necessário uma série de configurações, permitindo o acesso por meio do protocolo SSH. a configuração se dá por meio [desse passo-a-passo](https://www.raspberrypi.com/documentation/computers/remote-access.html#enable-the-ssh-server).

Feito isso, consegue-se acessar o rasp por meio do terminal e, com isso, configurar o mini computador. Com acesso remoto ao mesmo, consegue-se instalar o restante dos softwares.

___

## Maria DB

É um software derivado do **mysql** e que pode ser instalado por meio do terminal seguindo os seguintes passos:

1. Abrir o terminal;
2. Digitar o comando 'sudo apt install mariadb-server';
	Feita a instalação, pode-se olhar o status por meio do comando 'sudo systemctl status mariadb.
3. Para iniciar o mariaDB, use o comando 'sudo systemctl start mariadb';
4. Com a instalação feita, basta configurar por meio do comando 'sudo mysql_secure_installation'. Com isso, será pedido a configuração do:
	1. **Senha do root**: recomenda-se **a mesma senha do computador**
	2. **Remover usuários anônimos**: Como será acessado por apenas uma pessoa, aconselha-se **remover** (para remover, basta colocar '**sim**').
	3. **Desativar login root remotamente**:**Não** (acessaremos por meio do ssh).
	4. **Remover banco de dados de teste**: **Sim** (criaremos o nosso banco de dados).
	5. **Recarregar privilégios de tabela**: **Sim.**
5. Com a configuração feita, usa-se o comando 'sudo mariadb -u root -p'. Nesse caso, o usuário em questão é o 'root' e a senha será colocada depois de clicado o enter. (colocar a mesma senha de cadastrada anteriormente).
<<<<<<< HEAD
Com esses pontos, consegue-se acessar o banco de dados e fazer as alterações que bem entender
___

## Conectando o cabo Ethernet ao Raspberry por meio do GPIO

A comunicação entre o computador central e a rasp será feita por meio de um cabo ethernet. Como a pi zero w não tem essa entrada, a mesma será instalada por meio dos pinos GPIO. 
A pinagem se encontra [neste vídeo aqui](https://www.youtube.com/watch?app=desktop&v=Js5KRZSJ2co), enquanto a fixação do IP entre a rasp e o computador central, por meio [deste aqui](https://www.trendnet.com/press/resource-library/how-to-set-static-ip-address).

Com esses pontos, consegue-se acessar o banco de dados e fazer as alterações que bem entender.

___

## Código Python

O código que roda no rasp é o código chamado [mariaDB.py]. Nesse código pegamos os dados enviados pelo multimedidor e salvamos no servidor SQL que criamos anteriormente.
