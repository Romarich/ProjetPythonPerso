## mettre en place la connection au wallet
## faire l analyse du marche en regardant chaque crypto
## determiner si cela va monter ou descendre
## avoir la somme totale pour savoir cb mettre et sur quoi
## savoir quand il est temps de retirer la crypto
## voir les frais pour retirer ou mettre de l'argent

## si pas content de l api on peut prendre coingecko api

from alpha_vantage.timeseries import TimeSeries
import urllib3
import requests

apiKey1 = 'EL810PE25AVK5EZH'
apiKey2 = 'R0AP8WIQ562LB9LO'
apiKey3 = '5V5OEOEN5K98E697'

def chooseTheFiveFirstCryptoYahoo():
	response = requests.get('https://finance.yahoo.com/gainers')
	page_source = response.content
	print('inside function')
	print(page_source)

### apiKey1 honorez.romaric@yahoo.fr
### apiKey2 honorez.romaric@gmail.com
### apiKey3 test@test.com

#chooseTheFiveFirstCryptoYahoo()

ts = TimeSeries(key=apiKey1)
ts2 = TimeSeries(key=apiKey2)
ts3 = TimeSeries(key=apiKey3)


data, meta_data = ts.get_intraday('GOOGL')

##iterate on dict
for k in data.keys():
	print(data[k])

