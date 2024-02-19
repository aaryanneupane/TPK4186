from modules.parser import Parser

markdown_text = '''
# Sample Markdown Document

This is a sample Markdown document that contains various elements such as headers, lists, emphasis, links, images, and code blocks.

## Lists

### Unordered List
* Item 1
* Item 2
  * Subitem 1
  * Subitem 2

### Ordered List
1. First item
2. Second item

## Emphasis
*This text is italicized.*
**This text is bold.**

## Links and Images
[Link to example website](https://example.com)
![Example Image](https://example.com/image.jpg)

## Code Block"
'''

parsed_document = Parser().parse(markdown_text)

print(f"Document Title: {parsed_document.get_title()}")
for section in parsed_document.get_sections():
    print(f"Section Title: {section.get_title()}")
    for paragraph in section.get_paragraphs():
        print(f"Paragraph: {paragraph.get_text()}")
    print()