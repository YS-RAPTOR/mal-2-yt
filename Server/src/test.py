import common
import pickle
from mal.enums import AnimeListStatus


if __name__ == "__main__":
    mal_ids = common.get_animelist("Y_raptor_Y", [AnimeListStatus.completed])

    if isinstance(mal_ids, common.Error):
        print("The MAL list is private or the user does not exist.")
        exit(1)

    for mal_id in mal_ids:
        print(mal_id)

    with open("mal_ids.pkl", "wb") as f:
        pickle.dump(mal_ids, f)
