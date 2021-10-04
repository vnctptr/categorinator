from language_processing import LanguageProcessingService
from subscription_service import SubscriptionService


def main():
    response = SubscriptionService.get_subscription_list()
    lang = LanguageProcessingService.detect_channel_language(
        SubscriptionService.pop_channel(response)
    )


if __name__ == "__main__":
    main()
