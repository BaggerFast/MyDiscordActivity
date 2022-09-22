from time import sleep
from random import randrange, choice
from pypresence import Presence
from pypresence.exceptions import DiscordNotFound, InvalidID
from misc import Config, get_buttons, get_texts


class DiscordApp:

    def __init__(self):

        self.__discord = self.__get_client
        print('Client Found')

        self.__btn = get_buttons()
        self.__text = get_texts()

    @property
    def __get_client(self):
        while True:
            try:
                return Presence(client_id=Config.BOT_ID)
            except DiscordNotFound:
                sleep(Config.CLIENT_TIME_OUT)

    def update(self):
        self.__discord.connect()
        btn_index = randrange(len(self.__btn))

        while True:

            try:
                self.__discord.update(
                    state=choice(self.__text),
                    buttons=self.__btn[btn_index],
                )
            except InvalidID:
                main()
                break

            btn_index = (btn_index + 1) % len(self.__btn)
            sleep(Config.ANIM_TIME_OUT)


def main():
    app = DiscordApp()
    app.update()


if __name__ == '__main__':
    main()
