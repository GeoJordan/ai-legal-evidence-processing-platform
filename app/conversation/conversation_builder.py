from app.conversation.conversation import Conversation


class ConversationBuilder:
    """
    Builds Conversation objects from an EvidenceIndex.
    """

    def build(self, evidence_index):

        conversations = []

        for message in evidence_index.messages:

            conversation = Conversation()

            conversation.subject = message.header.subject

            conversation.messages.append(message)

            conversation.participants.add(message.header.sender)

            conversation.participants.add(message.header.recipient)

            conversation.start_date = message.header.date

            conversation.end_date = message.header.date

            conversations.append(conversation)

        return conversations