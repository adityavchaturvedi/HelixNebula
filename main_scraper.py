""" Importing appropriate packages"""
import requests # Package to get raw data from websites.
import json
import urllib # Package to support requests
from bs4 import BeautifulSoup # For cleaning up HTML raw data.
#from Queue import Queue
#from threading import Thread
#from multiprocessing import Process, Lock


def get_client_id_from_json_file(file_name='client_id.json', json_key='client_id'):
	json_file = open(file_name,'r')
	unicode_map = json.loads(json_file.read())
	str_id = str(unicode_map[json_key])
	json_file.close()
	return str_id

def get_text_from_file(filename):
	text_file = open(filename,'r')
	text = text_file.read()
	text_file.close()
	return text

client_id = get_text_from_file('client_id.out')
client_secret = get_text_from_file('client_secret.out')
access_token = get_text_from_file('access_token.out')
redirect_url = get_text_from_file('redirect_url.out')

#print access_token

r1 = requests.get('https://api.instagram.com/oauth/authorize/?client_id=' + client_id + '&redirect_uri=' + redirect_url + '&response_type=token&scope=public_content')
print r1.status_code
print r1.url
#https://api.instagram.com/v1/tags/coffee/media/recent?access_token=ACCESS-TOKEN&callback=callbackFunction
#print https://api.instagram.com/oauth/authorize/?client_id=CLIENT-ID&redirect_uri=REDIRECT-URI&response_type=token
#r = requests.get('https://www.instagram.com/oauth/authorize/?client_id=33701fb6d05149d19443ba2103d55e5d&redirect_uri=https://github.com/adityavchaturvedi/HelixNebula&response_type=token&scope=public_content')

#https://api.instagram.com/v1/users/aditya_v_c/?access_token=

#print get_client_id_from_text_file()


#https://www.instagram.com/oauth/authorize/?client_id=33701fb6d05149d19443ba2103d55e5d&redirect_uri=https://github.com/adityavchaturvedi/HelixNebula&response_type=token&scope=public_content