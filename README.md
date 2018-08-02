# Back-End Magalu-Finder

---
## Preparando o ambiente no linux (ubuntu)

* Instale o python 3.6

* Instale o pip

* Instale as dependêcias do python para dev

* Instale as libs do mysql

* Instale a virtualenv

## Instalação

```sh

$ sudo apt-get update

$ sudo apt-get install python3.6

$ sudo apt-get install python3-pip

$ sudo apt-get install python3.6-dev

$ sudo apt-get install libmysqlclient-dev

$ sudo apt-get install python3.6-venv
```

## Com a instalação feita

```sh

* Na sua pasta de projetos crie a sua virtualenv

$ python3.6 -m venv [nome da sua venv]

* Abra sua venv e clone o repositorio

* Inicie a sua venv

$ source bin/activate

* Entre no diretorio instale as dependências

$ pip3 install requirements-dev.txt 
```

## Para conectar com o banco

```sh

* Crie na raiz do projeto um arquivo com o nome my.cnf com o conteudo

[client]
database = [seu database]
user = [user]
password = [password]
default-character-set = utf8
```

## Para executar o prodjeto

```sh

* Acesse a raiz do projeto

$ python manager.py runserver
```
