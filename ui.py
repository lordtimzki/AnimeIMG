#visualization
#matplotlib
import api

def main():
    print('Hi welcome to the random anime image python program')
    user_input = input('Please select one tag (maid, waifu): ')
    api.get_random_anime_img(user_input)