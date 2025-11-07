import pytest
from md2html import convert

@pytest.mark.parametrize("markdown, expected", [
    # ---------------- Normal cases ----------------
    # 1. Heading and paragraph
    ("# Heading\n\nThis is a paragraph.",
     "<h1>Heading</h1>\n<p>This is a paragraph.</p>"),
    
    # 2. Paragraph with bold and italic text
    ("This is **bold** and *italic* text.",
     "<p>This is <strong>bold</strong> and <em>italic</em> text.</p>"),
    
    # 3. Unordered and ordered lists
    ("- Item1\n- Item2\n\n1. First\n2. Second",
     "<ul>\n    <li>Item1</li>\n    <li>Item2</li>\n</ul>\n<ol>\n    <li>First</li>\n    <li>Second</li>\n</ol>"),
    
    # ---------------- Basic edge cases ----------------
    # 4. Multiple blank lines between paragraphs
    ("First paragraph.\n\n\nSecond paragraph.",
     "<p>First paragraph.</p>\n<p>Second paragraph.</p>"),
    
    # 5. Heading using underline style
    ("Title\n======",
     "<h1>Title</h1>"),
    
    # 6. Inline code
    ("Use `code` in text.",
     "<p>Use <code>code</code> in text.</p>"),
    
    # 7. Link
    ("Visit [OpenAI](https://openai.com).",
     "<p>Visit <a href=\"https://openai.com\">OpenAI</a>.</p>"),
])
def test_convert_basic(markdown, expected):
    result = convert(markdown).strip()
    assert result == expected.strip()
