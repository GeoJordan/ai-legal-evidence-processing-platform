from app.case_report.report_section_formatter import ReportSectionFormatter


class CaseReportFormatter:

    def format(self, report):
        sections = report.sections()

        if not sections:
            return ""

        formatted_sections = []

        for section in sections:

            if hasattr(section, "title"):
                text = section.title

                if section.overview:
                    text += "\n" + section.overview

            else:
                text = section.__class__.__name__

            formatted_sections.append(text)

        header = (
            "AI LEGAL EVIDENCE PROCESSING PLATFORM\n"
            "CASE REPORT"
        )

        return (
        header
        + "\n\n"
        + "\n\n".join(formatted_sections)
        )
