from datetime import date, datetime

class ConversationAnalytics:
    """
    Calculates statistics for a Conversation.
    """

    def statistics(self, conversation):

        duration = None

        if (
            conversation.start_date is not None
            and conversation.end_date is not None
        ):
            duration = (
                conversation.end_date - conversation.start_date
            ).days

        return {
            "messages": conversation.message_count,
            "participants": len(conversation.participants),
            "start_date": conversation.start_date,
            "end_date": conversation.end_date,
            "duration_days": duration,
        }

    def participants(self, conversation):

        stats = {}

        for message in conversation.messages:

            sender = message.header.sender
            recipient = message.header.recipient

            stats.setdefault(
                sender,
                {"sent": 0, "received": 0},
            )

            stats.setdefault(
                recipient,
                {"sent": 0, "received": 0},
            )

            stats[sender]["sent"] += 1
            stats[recipient]["received"] += 1

        return stats

    def _to_date(self, value):
        """
        Convert either a string or datetime.date into a date object.
        """

        if isinstance(value, date):
            return value

        if isinstance(value, str):
            return datetime.strptime(value, "%Y-%m-%d").date()

        raise TypeError(f"Unsupported date type: {type(value)}")

    def response_times(self, conversation):

        messages = sorted(
            conversation.messages,
            key=lambda message: self._to_date(message.header.date),
        )

        response_times = []

        for previous, current in zip(messages, messages[1:]):

            previous_date = self._to_date(previous.header.date)
            current_date = self._to_date(current.header.date)

            response_times.append(
                (current_date - previous_date).days
            )

        return response_times

    def summary(self, conversation):

        return {
            "statistics": self.statistics(conversation),
            "participants": self.participants(conversation),
            "response_times": self.response_times(conversation),
        }
