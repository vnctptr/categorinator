import json
from pprint import PrettyPrinter as pprint
from google_service import GoogleService


class SubscriptionService:
    @staticmethod
    def get_subscription_list():

        youtube = GoogleService().client
        request = youtube.subscriptions().list(
            part="snippet,contentDetails", channelId="UCRruIoWgGyCFTPp1FBY5CEw"
        )
        response = request.execute()

        print(json.dumps(response, indent=2))

        return response

    @staticmethod
    def pop_channel(response):

        channel = response.get("items").pop()

        return channel
