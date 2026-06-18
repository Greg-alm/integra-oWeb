#Import do framework
#Import do render_template para leitura HTML
#request para capturar de dados
from flask import Flask, render_template, request
#biblioteca para criar conexão com mysql
import mysql.connector 

app = Flask(__name__)

#Cria conexão com MySQL
bd_config = {
    'host':'localhost',
    'user':'root',
    'password':'',
    'database':'cadastro1'
}

#Criação de rota para arquivo HTML principal
@app.route('/')
def index():
    return render_template('sla.html')

@app.route('/cadastrar',methods=['POST'])
def criar_cadastro():

#recebe os dados do formulario
    cpf = request.form['cpf']
    primeiro_nome = request.form['primeiro_nome']
    sobrenome= request.form['sobrenome']
    idade = request.form['idade']

#CRIAR CONEXÃO COM O BANCO DE DADOS
    connect = mysql.connector.connect(**bd_config)

#leva instruções SQL do python até o banco de dados
    caminho = connect.cursor()

    query = "INSERT INTO cliente1 (CPF, PRIMEIRO_NOME,SOBRENOME,IDADE)"