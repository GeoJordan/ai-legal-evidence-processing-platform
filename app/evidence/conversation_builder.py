from app.evidence.conversation_evidence import ConversationEvidence


class ConversationBuilder:
    """
    Builds ConversationEvidence objects.
    """

    def build(self, evidence):

        conversation = ConversationEvidence()

        for item in evidence:
            conversation.add(item)

        return conversation
