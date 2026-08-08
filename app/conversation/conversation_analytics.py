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