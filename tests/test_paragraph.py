import pytest
from md2html import convert_paragraph


@pytest.fixture
def paragraph_cases():
    return [
        ("This is a single line.", "<p>This is a single line.</p>"),
        ("This is a single line.\nIt is the first paragraph in this example.",
         "<p>This is a single line.<br>It is the first paragraph in this example.</p>"),
        ("This is the first paragraph.\n\nThis is the second paragraph.",
         "<p>This is the first paragraph.</p>\n<p>This is the second paragraph.</p>"),
        ("First paragraph.\n\n\nSecond paragraph after two blank lines.",
         "<p>First paragraph.</p>\n<p>Second paragraph after two blank lines.</p>"),
        ("   Leading spaces are fine.\nStill same paragraph.   ",
         "<p>Leading spaces are fine.<br>Still same paragraph.</p>"),
        ("Line one\nLine two\nLine three",
         "<p>Line one<br>Line two<br>Line three</p>"),
        ("<h1>Heading</h1>\n\nHello paragraph.",
         "<h1>Heading</h1>\n<p>Hello paragraph.</p>"),
        ("<h1>Heading</h1> Hello",
         "<h1>Heading</h1>\n<p>Hello</p>"),
        ("<h1>Heading</h1>\nHello\n\n",
         "<h1>Heading</h1>\n<p>Hello</p>"),
        ("<h2>Title</h2>\n\nThis is **bold** text.\n\n<ul>\n<li>Item</li>\n</ul>\n\nAnother paragraph.",
         "<h2>Title</h2>\n<p>This is **bold** text.</p>\n<ul>\n<li>Item</li>\n</ul>\n<p>Another paragraph.</p>"),
    ]


def test_convert_paragraph_cases(paragraph_cases):
    for markdown, expected in paragraph_cases:
        result = convert_paragraph(markdown).strip()
        assert result == expected.strip(), f"\nInput:\n{markdown}\n\nGot:\n{result}\nExpected:\n{expected}"


@pytest.mark.parametrize("markdown, expected", [
    ("Hello\nWorld", "<p>Hello<br>World</p>"),
    ("Hello\n\nWorld", "<p>Hello</p>\n<p>World</p>"),
    ("<h1>Header</h1>\nText after heading\n\n", "<h1>Header</h1>\n<p>Text after heading</p>"),
    ("<p>Existing paragraph</p>\n\nNew paragraph", "<p>Existing paragraph</p>\n<p>New paragraph</p>"),
])
def test_convert_paragraph_parametrized(markdown, expected):
    assert convert_paragraph(markdown).strip() == expected.strip()
