import json 
import requests

#no mas de 6 get por minuto.

URL = "https://poloniex.com/public?command=returnTicker"

def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content


def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js
	
def main():
	decojson = get_json_from_url(URL)
	print decojson["USDT_BTC"]
	

if __name__ == '__main__':
    main()
	