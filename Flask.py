import socket
from flask import Flask

empregados = [
    {'nome': 'fernandinho' , 'cargo':'empregada' , 'salario':250},
    {'nome': 'nick' , 'cargo':'pedreiro' , 'salario':500},
    {'nome': 'arthur' , 'cargo':'aero_moça' , 'salario':600}
]
app = Flask(__name__)

@app.route("/")

def hello():
    return "<h1> My first program </h1>"

@app.route("/empregados")

def get_empregados():
    return {'empregados':empregados}

@app.route("/empregados/<cargos>")

def get_empregados_cargos(cargo):
    array = list()
    
    for empregado in empregados:
        if cargo == empregado['cargo'].lower().strip():
            array.append(empregado)
    return {'empregados': array}

if __name__ == '__main__':
    v = socket.gethostbyname(socket.gethostname())
    print(f'\033[1;31mIp connected:{v}\033[m')
    app.run(debug=True)