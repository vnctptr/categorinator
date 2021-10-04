from langdetect import detect


class LanguageProcessingService:
    @staticmethod
    def detect_channel_language(channel):
        snip = channel.get("snippet")
        desc = snip.get("description")
        print(desc)
        lang = detect(desc)
        print(lang)
        return lang
