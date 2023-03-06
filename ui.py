#visualization
#matplotlib
import api
import json

def main():
    user_input = input('Please select one tag (maid, waifu): ')
    img_details = api.get_random_anime_img(user_input)
    with open('img.json', 'w') as image:
        json.dump(img_details, image)
