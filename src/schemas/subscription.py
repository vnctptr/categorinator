import json
from typing import List

from langdetect import detect


class Labels:
    languages = ["pl", "fr", "en", "es", "cat", "it"]
    categories = ["languages", "tech", "science", "education", "entertainment", "other"]


class Subscription:
    def __init__(self, channel):
        self._title: str = channel["snippet"]["title"]
        self._description: str = channel["snippet"]["description"]
        self._thumbnails: dict = channel["snippet"]["thumbnails"]
        self._channel_id: str = channel["snippet"]["resourceId"]["channelId"]
        self._language: str = (
            "" if self._description == "" else detect(self._description)
        )
        self._labels: List = []
        self._labels.append(self._language)
        self._last_watched = None

    def __str__(self):
        s = ""
        s += "title: " + self._title + "\n"
        s += "description: " + self._description[0:100] + "...\n"
        s += "language: " + self._language + "\n"
        s += "channel id: " + self._channel_id + "\n"
        return s

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    @property
    def title(self) -> str:
        return self._title

    @property
    def description(self) -> str:
        return self._description

    @property
    def thumbnails(self) -> dict:
        return self._thumbnails

    @property
    def labels(self) -> List:
        return self._labels

    # TODO
    def _update_last_watched(self):
        pass
