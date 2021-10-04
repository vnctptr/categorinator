import json

from services.google_api.google_subscription_service import GoogleSubscriptionService


def main():
    channels, channels_json = GoogleSubscriptionService.get_subscription_list()
    print(json.dumps(channels_json, indent=3))
    # activities = SubscriptionService.get_activity_list()


if __name__ == "__main__":
    main()
