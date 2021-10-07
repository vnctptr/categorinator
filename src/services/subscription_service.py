import json
from datetime import date


class SubscriptionService:
    @staticmethod
    def filter_by_labels(channels: list, labels: list):

        filter_labels = set(labels)
        result = []
        for channel in channels:
            channel_labels = set(channel.labels)

            if filter_labels.issubset(channel_labels):
                result.append(channel)

        return result

    @staticmethod
    def filter_by_date(channels: list, start_date: date, end_date: date):
        pass
