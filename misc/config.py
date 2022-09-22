import os
from typing import Final


class Config:
    BOT_ID: Final = os.getenv('BOT_ID', 'define_me')
    ANIM_TIME_OUT: int = 2
    CLIENT_TIME_OUT: int = 30
