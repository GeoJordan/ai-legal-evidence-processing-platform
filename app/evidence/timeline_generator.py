class TimelineGenerator:
    """
    Generates a chronological timeline of evidence.
    """

    def generate(self, evidence):

        return sorted(
            evidence,
            key=lambda item: item.collected_at,
        )

    