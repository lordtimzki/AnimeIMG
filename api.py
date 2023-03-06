import json
import urllib.request
import sys


def get_random_anime_img(input):
    url = "https://api.waifu.im/search/?included_tags=" + input
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel \
    Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML,\
like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    request = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(request)
    response_data = response.read()
    response.close()
    details = json.loads(response_data)
    return details
