import os
from typing import Final


class Config:
    BOT_TOKEN: Final = os.getenv('BOT_TOKEN', 'define_me')