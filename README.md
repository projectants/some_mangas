# **Some-Mangas**

O projeto consiste em um e-reader de mangás, onde o backend irá prover fotos de páginas advindas de script de raspagem de dados, onde serão cadastrados diretamente na base de dados do projeto, por meio dos models do Django, o frontend será feito em React assim que todos os impecilhos do backend froem resolvidos, atualmente o projeto já lista todos os capítulos e cada página nesse capítulo, mas ao cadastrar na base de tem uma lentidão sem precedentes, e com o script de cadastro de dados ocorre a desordenação das páginas.

<br>

## Requisitos

Liste aqui os requisitos necessários para executar seu projeto. Por exemplo:

- Python >= 3.8
- pip

<br>

## Instalação

1. Clone o repositório:

   ```
   git clone https://github.com/projectants/some_mangas
   ```

2. Entre na raíz do projeto:

   ```
   cd some_mangas
   ```

3. Crie um ambiente virtual python:

   ```
   python3 -m venv env
   ```

4. Ative o ambiente virtual e instale as dependências em requirements.txt:

   ```
   source env/bin/activate
   ```

   ```
   pip install -r requirements.txt`
   ```

5. Execute as migrações:

   ```
   python manage.py makemigrations
   ```

   ```
   python manage.py migrate
   ```

6. Execute o servidor de desenvolvimento:

   ```
   python manage.py runserver
   ```

7. Acesse o servidor em http://localhost:8000

<br>

## Página de Administração

1. Para acessar a página de administração, crie um super usuário:

   ```
   python manage.py createsuperuser
   ```

2. Acesse http://localhost:8000/admin

<br>


## Povoar o banco de dados

1. Para povoar o banco de dados, execute o script de raspagem de dados:

   ```
   python manage.py runscript shell
   ```

2. Como foi reportado no início o script de raspagem de dados está com problemas com relação a velocidade de cadastro e desordenação das páginas, por isso é necessário esperar um tempo considerável para que o script termine de cadastrar todos os dados.


<br>
<br>
<br>

# MIT License

Copyright (c) 2023 Naelson Fernandes da Fonsêca

[Leia a licença completa](https://github.com/projectants/some_mangas/blob/main/LICENSE)
