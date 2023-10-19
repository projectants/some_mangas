# some_mangas
Crie um ambiente virtual Python
python -m venv env

Ative o ambiente virtual e rode o seguinte comando para instalar dependências
pip install -r requirements.txt

Para rodar o projeto django execute 
python manage.py makemigrations
python manage.py makemigrations manga

python manage.py migrate

python manage.py runserver

Para criar um super usuário execute
python manage.py createsuperuser

Preencha os dados que for solicitado e acesse 127.0.0.1:8000/admin

Exceto o comando de criação, todos os outros precisam ser executados com o ambiente ativado e na pasta raíz do projeto.
