from app.conversation.conversation import Conversation


class ConversationBuilder:
    """
    Builds Conversation objects from an EvidenceIndex.
    """

    def build(self, evidence_index):
        conversations = []

        message_lookup = {}

        for message in evidence_index.messages:

            reply_to = message.header.in_reply_to

            if reply_to and reply_to in message_lookup:

                conversation = message_lookup[reply_to]

                conversation.messages.append(message)

                conversation.participants.add(message.header.sender)

                conversation.participants.add(message.header.recipient)

                conversation.end_date = message.header.date

                # Make the reply discoverable too
                message_lookup[message.header.message_id] = conversation

            else:

                conversation = Conversation()

                conversation.subject = message.header.subject.replace("Re: ", "")

                conversation.messages.append(message)

                conversation.participants.add(message.header.sender)
                conversation.participants.add(message.header.recipient)

                conversation.start_date = message.header.date
                conversation.end_date = message.header.date

                conversations.append(conversation)

                message_lookup[message.header.message_id] = conversation

        return conversations