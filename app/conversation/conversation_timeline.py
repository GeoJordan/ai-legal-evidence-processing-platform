class ConversationTimeline:
    """
    Generates timelines for a single Conversation.
    """

    def build(self, conversation):

        return list(conversation.messages)