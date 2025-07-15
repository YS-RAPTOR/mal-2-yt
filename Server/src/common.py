import os
import requests
from dotenv import load_dotenv
from typing import List, Literal
from mal import client
from mal.anime import AnimeListEntry
from mal.enums import AnimeListStatus

load_dotenv()
mal_client = client.Client(os.environ["MAL_CLIENT_ID"])


class YoutubeSong:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author


class AnimeSong:
    def __init__(self, title: str, author: str, anime: str):
        self.title = title
        self.author = author
        self.anime = anime

    def setup_youtube(self, youtube_songs: List[YoutubeSong]):
        self.youtube_songs = youtube_songs


class Error:
    def __init__(self, type: Literal["PrivateAnimeList"]):
        self.type = type


def get_animelist(username: str, filters: List[AnimeListStatus]) -> List[int] | Error:
    LIMIT = 100
    offset = 0
    animelist: List[AnimeListEntry] = []

    while True:
        try:
            animes = list(
                mal_client.get_anime_list(username, limit=LIMIT, offset=offset)
            )
            animelist.extend(animes)
            if len(animes) < LIMIT:
                break
            offset += 100
        except Exception as e:
            if "forbidden" in str(e).lower():
                return Error("PrivateAnimeList")

    return [
        anime.entry.id for anime in animelist if anime.list_status.status in filters
    ]


def get_playlist(playlist: str) -> List[YoutubeSong]:
    # Check if playlist exists, if it does not create it and return an empty list

    # If it exists, return a list of songs
    return []


def get_song_list(mal_ids: List[int]) -> List[AnimeSong]:
    URL = "https://api.animethemes.moe/anime?include=animethemes,resources,images&filter[has]=resources&filter[site]=MyAnimeList&filter[external_id]="

    for id in mal_ids:
        url = URL + str(id)
        anime_json = requests.get(url)
        print(anime_json.json())
        break

    return []


def filter_songs(
    anime_songs: List[AnimeSong],
    youtube_songs: List[YoutubeSong],
) -> List[AnimeSong]:
    return []


def search_youtube(songs: List[AnimeSong]):
    pass
