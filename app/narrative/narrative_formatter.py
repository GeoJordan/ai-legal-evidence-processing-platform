class NarrativeFormatter:

    def format(self, narrative):
        sections = narrative.sections()

        if not sections:
            return ""

        formatted_sections = []

        for section in sections:
            
            text = section.heading

            if section.content:
                text += "\n" + section.content

            if section.sources:
                text += "\n\nEvidence:"

                for source in section.sources:
                    text += f"\n- {source.evidence_id}"

            formatted_sections.append(text)

        return "\n\n".join(formatted_sections)

