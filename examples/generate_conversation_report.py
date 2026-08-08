"""
AI Legal Evidence Processing Platform

Sprint 7 End-to-End Demonstration

This example demonstrates the complete Conversation Intelligence workflow:

1. Create sample email evidence
2. Build an Evidence Index
3. Reconstruct conversations
4. Generate conversation analytics
5. Produce an investigator-ready conversation report
"""

from app.conversation.conversation_builder import ConversationBuilder
from app.conversation.conversation_analytics import ConversationAnalytics
from app.conversation.conversation_report import ConversationReport

from app.evidence.evidence_index import EvidenceIndex
from app.models.email_header import EmailHeader
from app.models.email_message import EmailMessage

REPORT_WIDTH = 60


def divider(char="="):
    print(char * REPORT_WIDTH)


def print_banner():

    divider()

    print("AI Legal Evidence Processing Platform")
    print("Version 0.7.0")
    print()
    print("Sprint 7 Demonstration")
    print("Conversation Intelligence")

    divider()

    print()


def stage(title):

    print()

    divider()

    print(title)

    divider()

    print()

def create_sample_messages():

    messages = []

    first = EmailMessage(
        header=EmailHeader(
            sender="alice@example.com",
            recipient="bob@example.com",
            subject="Passport Request",
            date="2026-08-01",
            message_id="<1>",
        ),
        body="Please send the passport for the upcoming trip.",
    )

    second = EmailMessage(
        header=EmailHeader(
            sender="bob@example.com",
            recipient="alice@example.com",
            subject="Re: Passport Request",
            date="2026-08-02",
            message_id="<2>",
            in_reply_to="<1>",
        ),
        body="The passport has been sent.",
    )

    third = EmailMessage(
        header=EmailHeader(
            sender="alice@example.com",
            recipient="bob@example.com",
            subject="Re: Passport Request",
            date="2026-08-03",
            message_id="<3>",
            in_reply_to="<2>",
        ),
        body="Thank you for confirming.",
    )

    messages.extend([first, second, third])

    return messages

def main():

    print_banner()

    stage("Stage 1 — Creating Sample Evidence")

    messages = create_sample_messages()

    print(f"✓ Created {len(messages)} sample email messages")

    stage("Stage 2 — Building Evidence Index")

    print("Adding email messages to the central Evidence Index...")
    print()

    index = EvidenceIndex()

    for message in messages:
        index.add_message(message)

    print(f"✓ Indexed {index.message_count()} email messages")

    stage("Stage 3 — Reconstructing Conversations")

    print("Grouping related email messages into conversation threads...")
    print()

    builder = ConversationBuilder()

    conversations = builder.build(index)

    print(f"✓ Built {len(conversations)} conversation(s)")

    if conversations:

        conversation = conversations[0]

        print()

        print("Subject:")
        print(conversation.subject)

        print()

        print("Participants:")
        print(len(conversation.participants))

        print()

        print("Messages:")
        print(conversation.message_count)  

        stage("Stage 4 — Conversation Analytics")

        print("Calculating conversation statistics and participant activity...")
        print()

        analytics = ConversationAnalytics()

        summary = analytics.summary(conversation)

        stats = summary["statistics"]

        print("Conversation Statistics")
        print("-")

        print(f"Messages      : {stats['messages']}")
        print(f"Participants  : {stats['participants']}")
        print(f"Duration      : {stats['duration_days']} day(s)")

        print()

        print("Response Times")
        print("-")

        print(summary["response_times"])

        print()

        print("Participant Activity")
        print("-")

        for participant, activity in summary["participants"].items():

            print()

            print(participant)
            print(f"  Sent     : {activity['sent']}")
            print(f"  Received : {activity['received']}")

        stage("Stage 5 — Investigator Report")

        print("Generating an investigator-ready conversation report...")
        print()

        report = ConversationReport()

        text = report.generate(conversation)

        print(text)

        print()

        divider()

        print("Sprint 7 Demonstration Complete")

        divider()

        print()

        print("✓ Sample Evidence Created")
        print("✓ Evidence Indexed")
        print("✓ Conversations Reconstructed")
        print("✓ Analytics Generated")
        print("✓ Investigator Report Produced")

        print()

        print("AI Legal Evidence Processing Platform")
        print("Built with Python • Test-Driven Development • Modular Architecture")

if __name__ == "__main__":
    main()