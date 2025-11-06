import pytest
from md2html import convert_ordered_list, convert_unordered_list

# ----------------------------
# Fixtures for repeated test data
# ----------------------------
@pytest.fixture
def ordered_list_cases():
    return [
        # Normal cases
        ("1. First item\n2. Second item\n3. Third item",
         "<ol>\n    <li>First item</li>\n    <li>Second item</li>\n    <li>Third item</li>\n</ol>"),
        ("1. First item\n1. Second item\n1. Third item",
         "<ol>\n    <li>First item</li>\n    <li>Second item</li>\n    <li>Third item</li>\n</ol>"),

        # Edge cases
        ("1.First item\n2.Second item",  # missing space → should not convert
         "1.First item\n2.Second item"),
        ("No list here", "No list here"),
        ("1. Single item", "<ol>\n    <li>Single item</li>\n</ol>"),
    ]

@pytest.fixture
def unordered_list_cases():
    return [
        # Normal cases
        ("- First item\n- Second item\n- Third item",
         "<ul>\n    <li>First item</li>\n    <li>Second item</li>\n    <li>Third item</li>\n</ul>"),
        ("* Apple\n+ Banana\n- Cherry",
         "<ul>\n    <li>Apple</li>\n    <li>Banana</li>\n    <li>Cherry</li>\n</ul>"),

        # Edge cases
        ("-No space after dash\n*No space after asterisk",
         "-No space after dash\n*No space after asterisk"),
        ("Just some text", "Just some text"),
        ("+ Single item", "<ul>\n    <li>Single item</li>\n</ul>"),
    ]

# ----------------------------
# Parametrized tests
# ----------------------------
@pytest.mark.parametrize("markdown, expected", [
    ("1. First\n2. Second\n3. Third",
     "<ol>\n    <li>First</li>\n    <li>Second</li>\n    <li>Third</li>\n</ol>"),
    ("1. A\n1. B\n1. C",
     "<ol>\n    <li>A</li>\n    <li>B</li>\n    <li>C</li>\n</ol>"),
])
def test_convert_ordered_list_param(markdown, expected):
    assert convert_ordered_list(markdown) == expected


@pytest.mark.parametrize("markdown, expected", [
    ("- A\n- B\n- C",
     "<ul>\n    <li>A</li>\n    <li>B</li>\n    <li>C</li>\n</ul>"),
    ("* X\n+ Y\n- Z",
     "<ul>\n    <li>X</li>\n    <li>Y</li>\n    <li>Z</li>\n</ul>"),
])
def test_convert_unordered_list_param(markdown, expected):
    assert convert_unordered_list(markdown) == expected

# ----------------------------
# Fixture-based tests for multiple cases
# ----------------------------
def test_ordered_list_fixture(ordered_list_cases):
    for markdown, expected in ordered_list_cases:
        assert convert_ordered_list(markdown) == expected

def test_unordered_list_fixture(unordered_list_cases):
    for markdown, expected in unordered_list_cases:
        assert convert_unordered_list(markdown) == expected
