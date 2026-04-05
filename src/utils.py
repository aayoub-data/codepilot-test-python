"""String utility functions."""


def reverse(s: str) -> str:
    """Reverse a string."""
    return s[::-1]


def capitalize_words(s: str) -> str:
    """Capitalize each word in a string."""
    return " ".join(word.capitalize() for word in s.split())


def truncate(s: str, max_length: int = 50) -> str:
    """Truncate string to max_length, adding '...' if truncated."""
    if len(s) <= max_length:
        return s
    return s[: max_length - 3] + "..."
