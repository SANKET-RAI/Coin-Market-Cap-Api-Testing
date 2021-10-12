import requests
from requests import Session
import secrets
from pprint import pprint as pp


class CMC:

    def __init__(self, token):
        self.apiurl = 'https://pro-api.coinmarketcap.com'
        self.headers = {'Accepts': 'application/json', 'X-CMC_PRO_API_KEY': token, }
        self.session = Session()
        self.session.headers.update(self.headers)

    def getAllCoinDetails(self):
        url = self.apiurl + '/v1/cryptocurrency/map'
        r = self.session.get(url)
        data = r.json()['data']
        return data

    def getCoinDetails(self, symbol):
        url = self.apiurl + '/v1/cryptocurrency/quotes/latest'
        parameters = {'symbol': symbol}
        r = self.session.get(url, params=parameters)
        data = r.json()['data']
        return data


cmc = CMC(secrets.API_KEY)


def getCoinStats(symbol):
        #stats = dict()
        temp_data = cmc.getCoinDetails(symbol)
        stats = temp_data[symbol]['quote']['USD']
        for attribute, values in stats.items():
            print(attribute, ":", values)


#pp(cmc.getAllCoinDetails())
print("---------------------------------------------------------------------------------------------------------------")
pp(cmc.getCoinDetails("BTC"))
print("---------------------------------------------------------------------------------------------------------------")
getCoinStats("ETH")