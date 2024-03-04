from modules.parser import Parser
from modules.html_compiler import HTMLcompiler

markdown_text = """
# Sample Markdown Document 

## Lists
Here are some unordered and ordered lists:

### Unordered List
Here are a couple of items in an unordered list:
* Item 1
* Item 2
* Item 3
* Item 4

### Ordered List
Here are a couple of items in an ordered list:
1. First item
2. Second item
3. Thirds item
"""

test_document = Parser().parse(markdown_text)

html_compiler = HTMLcompiler()

html_compiler.export(test_document, "HTML_test_1.html")