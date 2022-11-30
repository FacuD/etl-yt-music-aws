import json
from models import create_table
from constants import HEADERS_PATH
from cfg import HEADERS_AUTH_DICT
from ytmusicapi import YTMusic
import pandas as pd


class YTApi:
    def __init__(self, brand_account_number):
        if not HEADERS_PATH.exists():
            with open(str(HEADERS_PATH), "w") as auth_file:
                json.dump(HEADERS_AUTH_DICT, auth_file)
            create_table()

        self.ytmusic = YTMusic(auth=str(HEADERS_PATH), user=brand_account_number)

    def get_played_songs(self):
        songs_lst = self.ytmusic.get_history()
        return songs_lst
