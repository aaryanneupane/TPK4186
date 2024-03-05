import re
from .document import Document
from .section import Section

class Parser:
    def __init__(self):
        self.document = Document()

    def parse(self, text) -> Document:
        sections = re.split(
            r"\n##+\s+", text.strip()
        )  # Split text into sections based on headers
        # Add title
        self.document.set_title(sections[0].strip().split("# ")[1])
        # Add sections
        for section_text in sections[1:]:
            section = self.parse_section(section_text)
            self.document.add_section(section)
        return self.document

    def parse_section(self, section_text: str) -> Section:
        lines = section_text.split("\n")
        title = lines[0].strip()
        section = Section(title)

        # Add paragraphs and lists to section
        current_list_type = None
        current_list_items = []
        for line in lines[1:]:
            line = line.strip()
            if line.startswith('#'):
                # This line starts with '#', create a new section
                new_title = line.lstrip('#').strip()
                new_section = self.parse_section("\n".join([line] + lines[lines.index(line) + 1:]))
                section.add_section(new_section)
                break
            elif re.match(r"^\s*[*-]\s+", line):
                # This line is a list item for unordered list
                if not current_list_type or current_list_type == "ol":
                    # Start of a new list or switch from ordered to unordered list
                    if current_list_items:
                        section.add_list(current_list_type, current_list_items)
                    current_list_type = "uo"
                    current_list_items = [line.strip("*- ").strip()]
                else:
                    # Continue current unordered list
                    current_list_items.append(line.strip("*- ").strip())
            elif re.match(r"^\s*\d+\.\s+", line):
                # This line is a list item for ordered list
                if not current_list_type or current_list_type == "uo":
                    # Start of a new list or switch from unordered to ordered list
                    if current_list_items:
                        section.add_list(current_list_type, current_list_items)
                    current_list_type = "ol"
                    current_list_items = [line.strip("1234567890. ").strip()]
                else:
                    # Continue current ordered list
                    current_list_items.append(line.strip("1234567890. ").strip())
            elif re.match(r'^\s*!\[(.*?)\]\((.*?)\)', line):
                # This line is a figure
                figure_name = re.search(r'!\[(.*?)\]', line).group(1)
                figure_path = re.search(r'\((.*?)\)', line).group(1)
                section.add_figure(figure_path, figure_name)
            elif line:  # Skip fully blank lines
                # This line is a paragraph
                if current_list_items:
                    # Add previous list to section if exists
                    section.add_list(current_list_type, current_list_items)
                    current_list_type = None
                    current_list_items = []
                section.add_paragraph(line)
        # Add the last list if exists
        if current_list_items:
            section.add_list(current_list_type, current_list_items)

        return section