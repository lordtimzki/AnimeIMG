'''
Displays a generated anime girl.
'''

import visual
import file


def main():
    '''
    Contains the command list and the methods from other modules.
    '''
    print('Welcome to displaying random anime girls using python')
    print('*' * 40)
    print('waifu - an anime girl')
    print('maid - an anime girl but in a maid outfit')
    print('uniform - an anime girl but in a type of uniform')
    print('raiden-shogun - Raiden Shogun from Genshin Impact')
    print('marin-kitagawa - main heroine of My Dress-Up Darling')
    file.extract()
    visual.img('img.json')


if __name__ == "__main__":
    main()
