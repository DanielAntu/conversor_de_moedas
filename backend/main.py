from flask import Flask, jsonify, request
from flask_cors import CORS

from converter import convert_value, get_coin_quote
from currencys import currencys
from utils import validate

app = Flask(__name__)
CORS(app)

def is_list(currency):
    is_code = False
    for code in currencys:
        if currency == code['code']:
            is_code = True
            break

    return is_code

@app.route('/currencys')
def get_currencys():
    return jsonify(currencys)

@app.route('/brlusd')
def get_quote_eur_usd():
    quote = get_coin_quote('BRL', 'USD')
    value = convert_value(1, quote)
    return jsonify({
        'currency_pair1': 'BRL',
        'currency_pair2': 'USD',
        'symbol': '$',
        'quote': quote,
        'value': 1,
        'value_converting': value
    })

@app.route('/convert', methods=['POST'])
def convert():
    data = request.get_json()
    currency1 = validate(data, 'currency1')
    currency2 = validate(data, 'currency2')
    value = validate(data, 'value', type='float')

    if currency1 == '':
        return jsonify({'error': 'O campo moeda 1 esta com erro ou vazio'}), 400
    
    if currency2 == '':
        return jsonify({'error': 'O campo moeda 2 esta com erro ou vazio'}), 400
    
    if not value:
        return jsonify({'error': 'O campo valor a ser convertido esta com erro ou vazio'}), 400
    
    is_code1 = is_list(currency1)
    is_code2 = is_list(currency2) 

    if not is_code1 or not is_code2:
        return jsonify({'error': 'Essa moeda não exite no nosso sistema.'}), 400
    
    if currency1 == currency2:
        return jsonify({'error': 'As moedas não pode ser iguais.'}), 400

    quote = get_coin_quote(currency1, currency2)
    value_convert = convert_value(value, quote)

    symbol = ''
    for currency in currencys:
        if currency2 == currency['code']:
            symbol = currency['symbol']
            break

    obj = {
        'currency_pair1': currency1,
        'currency_pair2': currency2,
        'symbol': symbol,
        'quote': quote,
        'value': value,
        'value_converting': value_convert
    }

    return jsonify(obj)

if __name__ == '__main__':
    app.run(debug=True)