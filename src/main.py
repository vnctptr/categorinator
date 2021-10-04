from services.subscription_service import SubscriptionService


def main():
    channels = SubscriptionService.get_subscription_list()
    # activities = SubscriptionService.get_activity_list()


if __name__ == "__main__":
    main()
