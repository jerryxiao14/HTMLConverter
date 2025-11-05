import pytest 
from md2html import *

@pytest.fixture
def heading_cases():
    """Provide sample input-output pairs for convert_headings."""
    return [
        # Normal cases
        ("# Heading 1", "<h1>Heading 1</h1>"),
        ("## Heading 2", "<h2>Heading 2</h2>"),
        ("###### Deep Heading", "<h6>Deep Heading</h6>"),
        ("Heading\n======", "<h1>Heading</h1>"),
        ("Heading\n------", "<h2>Heading</h2>"),

        # Edge cases
        ("#Heading without space", "#Heading without space"),  # no space → not a heading
        ("#   Extra spaces   ", "<h1>Extra spaces</h1>"),
        ("Heading\n=", "Heading\n="),  # single = should not count
        ("###", "###"),  # heading without text
    ]

@pytest.mark.parametrize("markdown, expected", [
    ("# Heading 1", "<h1>Heading 1</h1>"),
    ("## Heading 2", "<h2>Heading 2</h2>"),
    ("Heading\n======", "<h1>Heading</h1>"),
    ("Heading\n------", "<h2>Heading</h2>"),
])
def test_convert_headings_parametrized(markdown, expected):
    """Test various valid Markdown headings using parametrization."""
    assert convert_headings(markdown) == expected


def test_convert_headings_edge_cases(heading_cases):
    """Test both normal and edge cases using a fixture."""
    for markdown, expected in heading_cases:
        assert convert_headings(markdown) == expected