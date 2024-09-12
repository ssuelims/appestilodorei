from flask import Flask



app = Flask (__name__)




""" 
Item  Avaliar

1  Criar Ambientew virtual python
2 Instalar o Flas
3  Entender a imporytaçao do Flask
4  Criar um objeto Flask
5  Entender o que e um objeto
 """

@app.route('/')

def index():

    return "Estilo Rei Barbearia"


@app.route('/novofuncionario')
def adicionar_funcionario():
    return "funcionario adicionado"

@app.route('/novocliente')
def adicionar_cliente():
    return"cliente adicionado"

@app.route('/novoservico')
def adicionar_servico():
    return"servico adicionado"


@app.route('/novo agendamento')
def adicionar_agendamento():
    return"agendamento adicionado"

@app.route('/login')
def adicionar_login():
    return"adicionar login"

@app.route('/logout')
def adicionar_logout():
    return"adicionar logout"

app.run(debug=True)

