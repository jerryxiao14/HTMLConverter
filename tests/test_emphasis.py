import pytest
from md2html import convert_emphasis

@pytest.fixture
def emphasis_cases():
    return [
        ("all that glitters is **not** gold",
         "all that glitters is <strong>not</strong> gold"),
        ("all that glitters is __not__ gold",
         "all that glitters is <strong>not</strong> gold"),
        ("all that g**litters** is not g**o**ld",
         "all that g<strong>litters</strong> is not g<strong>o</strong>ld"),
        ("all that g__litters__ is not g__o__ld",
         "all that g__litters__ is not g__o__ld"),
        ("*italic*", "<em>italic</em>"),
        ("_italic_", "<em>italic</em>"),
        ("***really important***",
         "<em><strong>really important</strong></em>"),
        ("___really important___",
         "<em><strong>really important</strong></em>"),
        ("really im***port***ant",
         "really im<em><strong>port</strong></em>ant"),
        ("really im___port___ant",
         "really im___port___ant"),
    ]


@pytest.mark.parametrize("markdown, expected", [
    ("**bold**", "<strong>bold</strong>"),
    ("__bold__", "<strong>bold</strong>"),
    ("*italic*", "<em>italic</em>"),
    ("_italic_", "<em>italic</em>"),
    ("***combo***", "<em><strong>combo</strong></em>"),
])
def test_convert_emphasis_parametrized(markdown, expected):
    assert convert_emphasis(markdown) == expected


def test_convert_emphasis_fixture(emphasis_cases):
    for markdown, expected in emphasis_cases:
        assert convert_emphasis(markdown) == expected
