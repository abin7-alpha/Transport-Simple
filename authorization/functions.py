import json
import requests
import urllib

from TransportSimple import settings

def url_encode(word):
	new_word = urllib.parse.quote(word.encode('utf-8'), safe='')
	return new_word

def get_token(username, password, redirect_uri):
	output = {}
	url = f"{settings.TOKEN_SERVER_URL}/o/token/"

	client_info = f'client_id={settings.CLIENT_ID}&client_secret={settings.CLIENT_SECRET}&grant_type=password'
	redirect_uri = f'&redirect_uri={url_encode(redirect_uri)}'
	user_info = f'&username={url_encode(username)}&password={url_encode(password)}'
	payload = client_info + user_info + redirect_uri
	print(payload)

	headers = {
		'Cache-Control': 'no-cache',
		'Content-Type': 'application/x-www-form-urlencoded',
	}

	response = requests.request("POST", url, headers=headers, data=payload)
	data = json.loads(response.text)
	# output["access_token"] = response["accesstoken"]
	# output["expires_in"] = response["expires_in"]

	return data