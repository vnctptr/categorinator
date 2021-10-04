from langdetect import detect


class Subscription:
    def __init__(self, channel):
        self._title: str = channel["snippet"]["title"]
        self._description: str = channel["snippet"]["description"]
        self._thumbnails: dict = channel["snippet"]["thumbnails"]
        self._channel_id: str = channel["snippet"]["resourceId"]["channelId"]
        self._language: str = (
            "" if self._description == "" else detect(self._description)
        )

        print(self)

    def __str__(self):
        s = ""
        s += "title: " + self._title + "\n"
        s += "description: " + self._description[0:100] + "...\n"
        s += "language: " + self._language + "\n"
        s += "channel id: " + self._channel_id + "\n"
        return s

    @property
    def title(self):
        return self._title

    @property
    def description(self):
        return self._description

    @property
    def thumbnails(self):
        return self._thumbnails
