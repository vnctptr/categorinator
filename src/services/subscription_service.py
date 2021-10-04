import json


class SubscriptionService:
    @staticmethod
    def filter_subscriptions(channels: list, labels: list):

        filter_labels = set(labels)
        result = []
        for channel in channels:
            channel_labels = set(channel.labels)

            if filter_labels.issubset(channel_labels):
                result.append(channel)

        return result
