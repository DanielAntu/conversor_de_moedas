import yfinance as yf


def get_coin_quote(currency1, currency2):
    try:
        ticker = f'{currency1}{currency2}=X'
        data = yf.Ticker(ticker)
        info = data.history(period="1d")
        
        if not info.empty:
            last_quote =  info['Close'].iloc[-1]
            return last_quote
        else:
            raise ValueError("Não foi possível obter informações da moeda.")
        
    except Exception as e:
        print(f'Erro ao obter cotação: {e}')
        return None
    
def convert_value(value, quote):
    return value * quote

if __name__ == '__main__':
    quote = get_coin_quote('USD', 'BRL')
    value = 100
    print(convert_value(value, quote), quote)
    print(convert_value(value, quote), quote)
