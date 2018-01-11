import json 
import requests
import time

TOKEN = "486097428:AAG39rsUixJx0zjQlky16jKOUQOfEv0rGDk"
URL = "https://api.telegram.org/bot{}/".format(TOKEN)
URLPOLONIEX="https://poloniex.com/public?command=returnTicker"

### exchange ####
def get_url_exchange(url):
	response = requests.get(url)
	content = response.content.decode("utf8")
	return content


def get_json_from_url_exchange(url,coin_pair):
	content = get_url_exchange(url)
	js = json.loads(content)
	return js[coin_pair]
	
def build_text(decojson):
	#print precio,high24,low24,change24 
	t =  "precio " + decojson["last"] + "\n"
	t = t +  "high24 " + decojson["high24hr"] + "\n"
	t = t + "low24 " + decojson["low24hr"] + "\n"
	t = t + "change24 " + decojson["percentChange"] + "\n"
	return t

### ROBOT ####
def make_message(t):
	coin_pair = ""
	if "USDT_BTC".find(t.upper()) > -1:
		decojson = get_json_from_url_exchange(URLPOLONIEX,"USDT_BTC")
		t = build_text(decojson)
	if "USDT_XRP".find(t.upper()) > -1:
		decojson = get_json_from_url_exchange(URLPOLONIEX,"USDT_XRP")
		t = build_text(decojson)
	return t
		

def get_url(url):
	response = requests.get(url)
	content = response.content.decode("utf8")
	return content


def get_json_from_url(url):
	content = get_url(url)
	js = json.loads(content)
	return js


def get_updates():
	url = URL + "getUpdates"
	js = get_json_from_url(url)
	return js


def get_last_chat_id_and_text(updates):
	num_updates = len(updates["result"])
	last_update = num_updates - 1
	text = updates["result"][last_update]["message"]["text"]
	chat_id = updates["result"][last_update]["message"]["chat"]["id"]
	return (text, chat_id)


def send_message(text, chat_id):
	url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
	get_url(url)
	
def main():
	last_textchat = (None, None)
	while True:
		text, chat = get_last_chat_id_and_text(get_updates())
		if (text, chat) != last_textchat:
			try:
				last_textchat = (text, chat)
				t = make_message(text)				
				send_message(t, chat)				
			except Exception as e:
				print(e, text)				
		time.sleep(0.5)


if __name__ == '__main__':
	main()
