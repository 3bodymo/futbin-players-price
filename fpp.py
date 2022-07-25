import sys
import requests
from bs4 import BeautifulSoup as bs
import re
import json

player_name = sys.argv[1]
player_rate = sys.argv[2]
platform = 'ps' #There is also 'xbox' and 'pc', if you want to change it.
year = '22'

def player_info():	
	url = 'https://www.futbin.com/search'
	headers = {
		"Host": "www.futbin.com",
		"User-Agent": "Mozilla/5.0",
	}
	params = {
		"year": year,
		"term": player_name
	}
	response = requests.get(url, headers=headers, params=params)
	response_json = re.sub("^b'|'", "", str(response.content))
	json_load = (json.loads(response_json))
	num_of_versions = 0
	for i in range(len(json_load)):
		try:
			if(json_load[i]['rating'] == player_rate):
				num_of_versions+=1
		except:
			not_found()
		
	player_list = [[] for _ in range(num_of_versions)]
	x = 0
	for i in range(len(json_load)):
		if(json_load[i]['rating'] == player_rate):
			player_id = json_load[i]['id']
			player_list[x].append(player_id)
			player_full_name = json_load[i]['full_name']
			player_list[x].append(player_full_name)
			player_version = json_load[i]['version']
			player_list[x].append(player_version)
			x+=1
			
	if(player_list == []):
		not_found()
	else:
		return player_list
	
def player_ID(player_info):
	d = dict(); 
	for i in range(len(player_info)):
		player_id = player_info[i][0]
		url = 'https://www.futbin.com/' + year + '/player/' + player_id
		headers = {
			"Host": "www.futbin.com",
			"User-Agent": "Mozilla/5.0",
		}
		response = requests.get(url, headers=headers)
		soup = bs(response.text,'lxml')
		div = soup.find_all("div", {"id":"page-info"})
		d[player_id] = div[0]['data-player-resource']
		
	return d

def player_price(d):
	d_to_list = list(d.items())
	d_price = dict(); 
	for i in range(len(d_to_list)):
		player_ID = d_to_list[i][1]
		url = 'https://www.futbin.com/' + year + '/playerPrices?player=' + player_ID
		headers = {
			"Host": "www.futbin.com",
			"User-Agent": "Mozilla/5.0",
		}
		response = requests.get(url, headers=headers)
		response_json = re.sub("^b'|'", "", str(response.content))
		json_load = (json.loads(response_json))
		player_price = json_load[player_ID]['prices'][platform]['LCPrice']
		d_price[d_to_list[i][0]] = player_price
		
	return d_price
	
def not_found():
	print('Sorry, there is no results!')
	exit()
	
def main():
	_player_info = player_info()
	_player_id_ID = player_ID(_player_info)
	_player_price = player_price(_player_id_ID)
	
	for i in range(len(_player_info)):
		Player_ID = _player_info[i][0]
		print("Player Name:", _player_info[i][1])
		print("Player Price:", '${}'.format(_player_price[Player_ID]))
		print("Player Version:", _player_info[i][2], "\n")

if __name__ == "__main__":
    main()
