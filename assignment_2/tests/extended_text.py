from tests.sample_text import sample_text, sample_text_2
from modules.parser import Parser
from modules.html_compiler import HTMLcompiler
from modules.docx_compiler import DocxCompiler

new_document = Parser().parse(sample_text)
new_document_2 = Parser().parse(sample_text_2)
html_compiler = HTMLcompiler()
docx_compiler = DocxCompiler()

html_compiler.export(new_document, "My Travel Blog")
docx_compiler.exportDocument(new_document_2, "My Travel Blog")