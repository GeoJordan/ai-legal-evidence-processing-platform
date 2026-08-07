class ConversationTimeline:
    """
    Generates timelines for a single Conversation.
    """

    def build(self, conversation):

        return sorted(
            conversation.messages,
            key=lambda message: message.header.date,
        )
