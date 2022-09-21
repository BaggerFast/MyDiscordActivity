import random
from time import sleep
from pypresence import Presence
from misc.config import Config


def main():
    discord = Presence(client_id=Config.BOT_TOKEN)
    discord.connect()
    btns = [
        {'label': "Youtube", "url": "https://www.youtube.com/baggerfast"},
        {'label': "Server", "url": "https://discord.gg/GWZ3F2B5Ph"},
    ]
    texts = [
        'I love C#',
        'I love girls',
        'I love Python',
        'Python Youtuber',
        'Vim is the best',
        'Linux is the best',
        'It developer',
    ]
    while True:
        discord.update(
            state=random.choice(texts),
            buttons=btns,
        )
        sleep(2)


if __name__ == '__main__':
    main()