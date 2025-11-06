import pytest
from md2html import convert_link


@pytest.fixture
def link_cases():
    return [
        # Normal cases
        ("Go to [OpenAI](https://openai.com) for info.",
         "Go to <a href=\"https://openai.com\">OpenAI</a> for info."),
        ("Check [Google](https://google.com) and [GitHub](https://github.com).",
         "Check <a href=\"https://google.com\">Google</a> and <a href=\"https://github.com\">GitHub</a>."),

        # Edge cases
        ("[Home](https://example.com) is the page.", 
         "<a href=\"https://example.com\">Home</a> is the page."),
        ("[A](url1)[B](url2)", 
         "<a href=\"url1\">A</a><a href=\"url2\">B</a>"),
        ("Just plain text", "Just plain text"),  # no links
    ]


@pytest.mark.parametrize("markdown, expected", [
    ("Go to [OpenAI](https://openai.com) for info.",
     "Go to <a href=\"https://openai.com\">OpenAI</a> for info."),
    ("Check [Google](https://google.com) and [GitHub](https://github.com).",
     "Check <a href=\"https://google.com\">Google</a> and <a href=\"https://github.com\">GitHub</a>."),
    ("[Home](https://example.com) is the page.", 
     "<a href=\"https://example.com\">Home</a> is the page."),
])
def test_convert_link_parametrized(markdown, expected):
    assert convert_link(markdown) == expected

# ----------------------------
# Fixture-based test for multiple cases
# ----------------------------
def test_convert_link_fixture(link_cases):
    for markdown, expected in link_cases:
        assert convert_link(markdown) == expected
