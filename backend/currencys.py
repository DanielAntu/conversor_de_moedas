currencys = [
    {"code": "USD", "name": "Dólar Americano", "symbol": "$"},
    {"code": "EUR", "name": "Euro", "symbol": "€"},
    {"code": "BRL", "name": "Real Brasileiro", "symbol": "R$"},
    {"code": "JPY", "name": "Iene Japonês", "symbol": "¥"},
    {"code": "GBP", "name": "Libra Esterlina", "symbol": "£"},
    {"code": "AUD", "name": "Dólar Australiano", "symbol": "A$"},
    {"code": "CAD", "name": "Dólar Canadense", "symbol": "CA$"},
    {"code": "CHF", "name": "Franco Suíço", "symbol": "CHF"},
    {"code": "CNY", "name": "Yuan Chinês", "symbol": "¥"},
    {"code": "INR", "name": "Rúpia Indiana", "symbol": "₹"},
]

if __name__ == '__main__':
    for currency in currencys:
        print(currency['code'])
