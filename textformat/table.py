class TableFormatter:
    """ Formats tables for CLI display """

    @staticmethod
    def generate(headers, data):
        """ Creates a formatted table for structured output """
        col_widths = [max(len(str(item)) for item in col) for col in zip(headers, *data)]
        border = "+".join("-" * (w + 2) for w in col_widths)

        def format_row(row):
            return "| " + " | ".join(f"{str(item).ljust(w)}" for item, w in zip(row, col_widths)) + " |"

        return f"{border}\n{format_row(headers)}\n{border}\n" + "\n".join(format_row(row) for row in data) + f"\n{border}"
