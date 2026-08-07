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

        return "\n".join(lines)