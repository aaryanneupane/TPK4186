from modules.docx_compiler import DocxCompiler
from modules.parser import Parser

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
3. Third item
"""

test_document = Parser().parse(markdown_text)

docx_compiler = DocxCompiler()

docx_compiler.exportDocument(test_document, "Docx_test_1")