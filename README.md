# PWBE-Formativa

## ESSE É O PASSO A PASSO PARA QUE O PROJETO RODE CORRETAMENTE, SIGA-OS!!

### PRÉ-REQUISITOS:
- Deve ser um servidor Windows para que todos os comandos da aplicação funcione corretamente, caso seja outro, eles podem necessitar de alterações.
- O Python deve estar instalado na máquina para funcionar;
- O Python deve estar instalado no Visual Studio Code para funcionar;
- É necessário que você tenha instalado na sua máquina o APP mysql Workbench, pois é por lá que você vai criar o banco de dados.

### BANCO DE DADOS:
1. Abra o WorkBench
2. Abra o Banco do projeto no APP
3. Vá no Settings.py e insira os dados corretos na linha 95 - 99 para que o projeto rode corretamente

### APLICAÇÃO:
- Para rodar o projeto é necessário fazer uma série de passos que estão listados abaixo:
1. Abra o projeto no Visual Studio Code
2. Dê CTRL + J ou abra o terminal manualmente
3. Crie a Env do Projeto: python -m venv env
4. Ative a Env do Projeto: .\env\Scripts\activate
5. Instale os requirements que estão no arquivo kauan.txt: pip install -r kauan.txt
6. Cria o banco, colocando ele para rodar no WorkBench
7. Volte para o projeto
8. Dê makemigration no terminal do projeto: python .\manage.py makemigration
9. Dê migrate para que tudo migre corretamente na máquina: python .\manage.py migrate
10. Crie o SuperUser: python manage.py createsuperuser
11. Por fim rode o projeto: python manage.py runserver

