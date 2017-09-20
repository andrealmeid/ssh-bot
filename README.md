# ssh-bot

_ssh-bot_ é um programa de comando e controle de uma botnet baseada em comunicação por SSH.
SSH é um protocolo de comunicação entre dois computadores, muito utilizado para usuários acessarem remotamente outros computadores ou servidores.
Essa botnet não contém um suporte a propagação do malware, mas os requisitos para acessar uma vítima são:
- O computador da vítima precisa ter um servidor ssh operando;
- Ter o nome de usuário e senha da vítima para autentificação.

### Tutorial
Nesse tutorial, testaremos em um mesmo computador o _bot_ e o _C&C_.

#### Criando o usuário do bot
Primeiro, vamos criar um usuário para o bot no computador:
```bash
$ sudo useradd -m -g users -G wheel -s /bin/bash user
```
Adicione uma senha:
```bash
$ sudo passwd user
```
Agora, para testar, vamos acessar seu usuário:
```bash
$ su user
```
Se a criação foi bem sucedida, você estará na pasta `home` do nosso usuário "vítma".

#### Ligando o servidor ssh
Verifique se você tem um servidor ssh instalado e rodando no seu computador. [Aqui](https://www.howtogeek.com/howto/ubuntu/setup-openssh-server-on-ubuntu-linux/) está um exemplo de como fazer isso no Ubuntu. Para testar se está funcionando, tente acessar o novo usuário:
```bash
ssh user@localhost
```
Como você nunca acessou esse host antes, você precisa aceitar a conexão. Digite a senha que você escolheu no passo anterior.

#### Usando o ssh-bot
Agora que já temos um usuário para testar, vamos usar o programa de comando e controle.
As dependências do programa são:
- Python 3;
- paramiko, para conexão ssh;
- tabulate, para impressão de texto na tela.

Inserimos as credencias dos bots em `bots.txt`, desta forma:
```
user@host password
```
Agora executamos o programa:
```bash
$ python command.py
```
O programa vai abrir e vai automaticamente verificar o arquivo bots.txt em busca dos hosts e mostrar o estado de cada um. O programa já vem com algumas opções instaladas, incluindo o `cmd`, onde você pode executar qualquer comando shell nos hosts e o comando `Ares`, onde você pode infectar o host com a botnet [Ares](https://github.com/andrealmeid/Ares).

#### Referências
https://github.com/mh4x0f/botdr4g0n

http://www.paramiko.org/
