from currency_converter import CurrencyConverter

cc = CurrencyConverter('http://www.ecb.europa.eu/status/eurofxref/eurofxref.zip')

print(cc.convert(1, 'USD','KRW'))