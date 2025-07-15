from dotenv import load_dotenv
from typing import List, Literal
from mal import client
from mal.anime import AnimeListEntry
from mal.enums import AnimeListStatus
import os

load_dotenv()
mal_client = client.Client(os.environ["MAL_CLIENT_ID"])


class AnimeSong:
    def __init__(self, title: str, author: str, anime: str, song_type: str):
        self.title = title
        self.author = author
        self.anime = anime
        self.song_type = song_type  # 'OP1', 'ED1', etc.

    def setup_youtube(self, youtube_links: List[str]):
        self.youtube_links = youtube_links


class YoutubeSong:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author


class Error:
    def __init__(self, type: Literal["PrivateAnimeList"]):
        self.type = type


def get_animelist(username: str, filters: List[AnimeListStatus]) -> List[int] | Error:
    offset = 0
    limit = 100
    animelist: List[AnimeListEntry] = []

    while True:
        try:
            animes = list(
                mal_client.get_anime_list(username, limit=limit, offset=offset)
            )
            animelist.extend(animes)
            if len(animes) < limit:
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
    return []


def filter_songs(
    anime_songs: List[AnimeSong],
    youtube_songs: List[YoutubeSong],
) -> List[AnimeSong]:
    return []


def search_youtube(songs: List[AnimeSong]):
    pass
