class ConversationReport:
    """
    Generates formatted reports for a Conversation.
    """

    REPORT_WIDTH = 60

    SECTION_DIVIDER = "=" * REPORT_WIDTH

    def generate(self, conversation):

        lines = []

        lines.append(self.SECTION_DIVIDER)
        lines.append("Conversation Report")

        lines.append(self.SECTION_DIVIDER)
        lines.append("")

        lines.append(f"Subject: {conversation.subject}")
        lines.append("")

        lines.append(f"Participants: {len(conversation.participants)}")
        lines.append(f"Messages: {conversation.message_count}")
        lines.append("")

        timeline = sorted(
            conversation.messages,
            key=lambda message: message.header.date,
        )

        for message in timeline:

            lines.append(message.header.date)
            lines.append("")

            lines.append(
                f"{message.header.sender} → {message.header.recipient}"
            )
          
            lines.append(message.header.subject)
            lines.append("")

            lines.append(message.body)
            lines.append("")

            lines.append("-" * self.REPORT_WIDTH)

        return "\n".join(lines)