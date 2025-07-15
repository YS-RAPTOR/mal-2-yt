import common
import pickle
from mal.enums import AnimeListStatus


if __name__ == "__main__":
    with open("mal_ids.pkl", "rb") as f:
        mal_ids = pickle.load(f)

    common.get_song_list(mal_ids)
