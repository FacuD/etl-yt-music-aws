from yt_api import YTApi
from cfg import BRAND_ACCOUNT_NUMBER
from models import upload_songs
import pandas as pd


def get_today_played_songs(songs_df):
    return songs_df.query("played_at == 'Today'")


def validate_data(df):
    if not df["song_id"].is_unique:
        raise Exception("A value from id is not unique")

    if df.isnull().values.any():
        raise Exception("A value in the df is null")


def transform(raw_songs):
    clean_lst = [
        {
            "song_id": song["videoId"],
            "title": song["title"],
            "artist": song["artists"][0]["name"],
            "played_at": song["played"],
        }
        for song in raw_songs
    ]

    clean_df = pd.DataFrame(clean_lst)

    filtered_df = get_today_played_songs(clean_df)

    validate_data(filtered_df)

    return filtered_df


def load(songs_df):
    print(f"Uploading {len(songs_df)} songs to the db")
    upload_songs(songs_df)


# if __name__ == "__main__":
def handler(event, context):
    yt_music = YTApi(BRAND_ACCOUNT_NUMBER)

    # Extract
    raw_songs = yt_music.get_played_songs()
    print(f"Extracted {len(raw_songs)} songs")

    # # Transform
    songs_df = transform(raw_songs)

    # Load
    load(songs_df)

    print("Done.")
