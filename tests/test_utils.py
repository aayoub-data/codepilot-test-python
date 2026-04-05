"""Tests for utils module."""
from src.utils import reverse, capitalize_words, truncate


def test_reverse():
    assert reverse("hello") == "olleh"
    assert reverse("") == ""
    assert reverse("a") == "a"


def test_capitalize_words():
    assert capitalize_words("hello world") == "Hello World"
    assert capitalize_words("already Capital") == "Already Capital"


def test_truncate():
    assert truncate("hello", 10) == "hello"
    assert truncate("hello world this is long", 10) == "hello w..."
    assert truncate("short", 50) == "short"
