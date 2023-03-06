'''
Handles the API part of the program.
'''
import json
import urllib.request


def get_random_anime_img(tag):
    '''
    Uses the api to return json data.
    '''
    url = "https://api.waifu.im/search/?included_tags=" + tag
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel \
    Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML,\
like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    request = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(request) as response:
        response_data = response.read()
    details = json.loads(response_data)
    return details
