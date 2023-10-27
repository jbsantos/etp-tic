# etp-tic

Segue o passos para projeto funcionar 

#### Etapa 1

Instalar versão do Python 3.7 e configura a maquina para a versão.

Windows

Faca os procedimentos abaixo para configurar o python 
1. Abra o painel de controle e navegue até as configurações de sistema.
2. Selecione as configurações avançadas do sistema.
3. Clique em variáveis de ambiente.
4. Procure nas variáveis do sistema pela variável path .
5. Clique em Editar .
6. Veja se os valores C:\Python37 e C:\Python37\Scripts já estão no campo de valor da variável de ambiente; se não existirem, adicione-os ao final da linha separados por ponto e vírgula ( ; ). O python37 , neste exemplo, é referente à pasta onde o Python foi instalado no seu sistema, então este valor pode ser diferente caso esteja instalando outra versão.
Por exemplo, se for a versão 2.7.15 do Python, o valor será Python27 ; se for 3.7.0 , o valor será Python37 e assim por diante. Veja o caminho exato da sua instalação e substitua o valor acima.
7. Após isso, clique em OK .

---instalar o pip
python -m ensurepip
---apos termina, rodar o comanda 
python -m ensurepip --upgrade:

---Criando um virtualenv no Windows:
---Rode o comando a baixo lembrando de adaptar o caminho do python
\Python37\Scripts\pip.exe install virtualenv

---Em seguida coloque o caminho da pasta 
Python37\Scripts\virtualenv.exe venv

---Para ativar seu virtualenv rode o seguinte comando:
venv\Scripts\activate

Ubuntu

---Faca os procedimentos abaixo para configurar o python 
---rodando o comando e veja se ja existe algum python pre instalado 
which python

--- veja a versão do python3 instalado em sua máquina
python3 --version

---caso retorna, verifique a versão, caso não instale da seguinte maneira
sudo apt-get install python3.7.17

---Instalar o pip 
sudo apt-get install python3.7-pip

---Criando um virtualenv no Ubuntu:
---Para instalar um virtualenv no Ubuntu, rode o comando:
sudo pip3 install virtualenv

---Em seguida coloque o caminho da pasta
virtualenv -p python3 venv

---Para ativar seu virtualenv rode o seguinte comando:
source ./venv/bin/activate

#### Etapa 2 

No ambiente venv

---Rode o comando a seguir para instalar o Flask em seu virtualenv .
pip3.7 install flask

---conexão com o banco de dados MySQL :
sudo apt-get install python3.7-dev libmysqlclient-dev

---Instale o pacote que se encontra no projeto:
pip install -r requeriments_etp.txt

---caso ocorrer um erro durante a instalação, comente a linha que esta havendo e repita o processo.


#### Etapa 3
---Alterar o ambiente de visão para desenvolvimento 
export FLASK_ENV=development

E rodar o projeto 
python run.py

caso ocorrer um erro durante a execução, identifique qual o programa e faça colocando o nome do programa
pip install nome_programa 

