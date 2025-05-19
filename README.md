# PWBE-Formativa

## Esse é o passo a passo para que o projeto rode corretamente, siga-os!

- OBS.: Esses são os passos para rodar em um servidor Windows, caso seja outro, os comandos da aplicação podem ser um pouco diferentes.

### BANCO DE DADOS:
- É necessário que você tenha instalado na sua máquina o APP mysql Workbench, pois é por lá que você vai criar o banco de dados.
Abra o WorkBench;
1. Abra o Banco do projeto no APP
2. Vá no Settings.py e insira os dados corretos na linha 95 - 99 para que o projeto rode corretamente

### APLICAÇÃO:
- Para rodar o projeto é necessário fazer uma série de passos que estão listados abaixo:
1. Abra o projeto no Visual Studio Code
2. Dê CTRL + J ou abra o terminal manualmente
3. Crie a Env do Projeto: python -m venv env
4. Ative a Env do Projeto: .\env\Scripts\activate
5. Dê migrate para que tudo migre corretamente na máquina: python .\manage.py migrate
6. Instale os requirements que estão no arquivo kauan.txt: pip install -r kauan.txt
7. Crie o SuperUser: python manage.py createsuperuser
8. Por fim rode o projeto: python manage.py runserver

