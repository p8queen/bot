import json 
import requests

#no mas de 6 get por minuto.

URL = "https://poloniex.com/public?command=returnTicker"

def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content


def get_json_from_url(url,coin_pair):
    content = get_url(url)
    js = json.loads(content)
    return js[coin_pair]
	
def main():
	decojson = get_json_from_url(URL,"USDT_XRP")
        #print precio,high24,low24,change24 
	print "precio", decojson["last"]
	print "high24", decojson["high24hr"]
	print "low24", decojson["low24hr"]
	print "chage24", decojson["percentChange"]
	

if __name__ == '__main__':
    main()
	
