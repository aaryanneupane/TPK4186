from modules.parser import Parser
from modules.paragraph import Paragraph
from modules.list import List
from modules.figure import Figure
from modules.section import Section

markdown_text = """
# Sample Markdown Document 

## Lists
Here are some unordered and ordered lists:

## Unordered List
Here are a couple of items in an unordered list:
* Item 1
* Item 2
* Item 3
* Item 4

## Ordered List
Here are a couple of items in an ordered list:
1. First item
2. Second item


## Images (Not Supported yet)
![Link to example website](/user/tmp)
![Example Image](/user/tmp)
"""

parsed_document = Parser().parse(markdown_text)

print()
print(f"Document Title: {parsed_document.get_title()}\n")
for section in parsed_document.get_sections():
    print(f"Section Title: {section.get_title()}")
    for content in section.get_contents():
        if type(content) == Paragraph:
            print(f"{type(content)}: {content.get_text()}")
        elif type(content) == List:
            print(
                f"{type(content)}: {content.get_list_type()} list {content.get_items()}"
            )
        elif type(content) == Figure:
            print(
                f"{type(content)}: Name: {content.get_name()} Path: {content.get_path()}"
            )
        elif type(content) == Section:
            print(f"{type(content)}: {content.get_title()}")
print()
