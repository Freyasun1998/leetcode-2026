"""Smoke tests so CI can verify solutions import and run."""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

# LeetCode-style layout: solutions live under Array_String/, not as installable packages.
_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_ROOT / "Array_String"))

from Merge_Strings_Alternately import Solution  # noqa: E402


@pytest.mark.parametrize(
    ("word1", "word2", "want"),
    [
        ("abc", "pqr", "apbqcr"),
        ("ab", "pqrs", "apbqrs"),
        ("abcd", "pq", "apbqcd"),
        ("a", "z", "az"),
    ],
)
def test_merge_alternately(word1: str, word2: str, want: str) -> None:
    assert Solution().mergeAlternately(word1, word2) == want
