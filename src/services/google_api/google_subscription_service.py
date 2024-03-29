from services.google_api.google_service import GoogleService
from schemas.subscription import Subscription

MAX_RESULTS_PER_PAGE = 50


class GoogleSubscriptionService:
    @staticmethod
    def get_activity_list():

        youtube = GoogleService().client

        nextPageToken = None
        finished_fetching = False

        subscriptions = []

        count = 0
        while not finished_fetching and count < 1:
            count += 1
            request = youtube.activities().list(
                part="snippet,contentDetails",
                channelId="UCRruIoWgGyCFTPp1FBY5CEw",
                maxResults=MAX_RESULTS_PER_PAGE,
                pageToken=nextPageToken,
            )
            response = request.execute()

            for channel in response.get("items"):
                subscriptions.append(Subscription(channel))

            nextPageToken = response.get("nextPageToken")
            finished_fetching = nextPageToken is None

        return subscriptions

    @staticmethod
    def get_subscription_list():

        youtube = GoogleService().client

        nextPageToken = None
        finished_fetching = False

        subscriptions = []
        subscriptions_json = {"subscriptions": []}

        while not finished_fetching:
            request = youtube.subscriptions().list(
                part="snippet,contentDetails",
                channelId="UCRruIoWgGyCFTPp1FBY5CEw",
                maxResults=MAX_RESULTS_PER_PAGE,
                pageToken=nextPageToken,
                order="unread",
            )
            response = request.execute()
            # print(json.dumps(response, indent=1))

            for channel in response.get("items"):
                subscriptions.append(Subscription(channel))
                subscriptions_json["subscriptions"].append(
                    Subscription(channel).__dict__
                )

            nextPageToken = response.get("nextPageToken")
            finished_fetching = nextPageToken is None

        return subscriptions, subscriptions_json
