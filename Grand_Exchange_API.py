import requests
import time
import json
import pandas as pd

	# r = requests.get('https://secure.runescape.com/m=itemdb_oldschool/api/catalogue/detail.json?item=1')

colname = ['ID']
data = pd.read_csv('C:/Users/Michael Arena/Desktop/Runescape_Bot/osrs_id.csv', names=colname)
ids = data.ID.tolist()

URL_Values = []
results = [] 

for i in ids:

	# look for URL, if page not found, restart for loop.

	url = f'https://secure.runescape.com/m=itemdb_oldschool/api/catalogue/detail.json?item={i}'
	r = requests.get(url)
	if r.status_code == 404:
		continue
	else:

	

		item_package = r.json()

		#JSON file is a dict inside a dict, this retrieves the values of each item i want.
		item  = item_package['item']
		item_name = item_package['item']['name']
		item_id = item_package['item']['id']
		item_des = item_package['item']['description']
		item_current_price = item_package['item']['current']['price']
		item_1_day_change = item_package['item']['today']['price']
		item_30_day_change = item_package['item']['day30']['change']
		item_90_day_change = item_package['item']['day90']['change']
		item_180_day_change = item_package['item']['day180']['change']


		# new dictionary of items and areas of interest.
		data = {
			'name':item_name,
			'ID':item_id,
			'description': item_des,
			'current_price': item_current_price,
			'1_day_change': item_1_day_change,
			'30_day_change': item_30_day_change,
			'90_day_change': item_90_day_change,
			'180_day_change': item_180_day_change,

		}


		#append all data from API's json to results list
		results.append(data)

		# sleep for how long it takes to get a response
		time.sleep(r.elapsed.total_seconds())



for result in results:
	print(result['name'])
	print(result['ID'])

