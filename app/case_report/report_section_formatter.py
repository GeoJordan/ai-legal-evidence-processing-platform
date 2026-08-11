class ReportSectionFormatter:

    def format_heading(self, heading):
        return (
            "============================================================\n"
            + heading.upper()
            + "\n"
            + "============================================================"
        )