# Importing the yfinance package
import yfinance as yf
from datetime import date
from flask import Flask, jsonify, request
#
# Este metodo retorna un pandas dataframe con datos economicos relacionados
# con un 'stock' (e.g. GOOGL, AMZN) entre una fecha inicial (sd) y una fecha
# final (ed). Las fechas pueden estar en formato 'YYYY-MM-DD'.
#
# sd: fecha inicial
# stock: nombre código de la acción
# ed: fecha final. En caso que el usuario no lo indique, se tomara la fecha 
# del dia de hoy
#
import sys


# jsonify sirve para convertir un objeto a formato JSON
#La sgte función nos va a obtener los datos de un JSON y devolverá un JSON con la respuesta de los datos de Yahoo Finance
app = Flask(__name__)

@app.route('/data', methods=['POST'])
def get_stock_data():

    #parsea el contenido a JSON
    data = request.get_json()

    stock = data['stock']
    sd = data['sd']
    ed = data['ed']

    #yf.download obtiene los datos de yahoo finance

    #guardamos la información de yahoo finance en la variable info
    info = yf.download(stock, sd, ed)
    info.index = info.index.strftime('%Y-%m-%d %H:%M:%S')
    #como se nos pide, devolvemos los datos en formato JSON
    return jsonify(info.to_dict())


if __name__ == "__main__":
    app.run()
