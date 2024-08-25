import pytest
from main import count_vowels

def test_only_vowels():
    assert count_vowels("aeiou") == 5
    assert count_vowels("AEIOU") == 5

def test_no_vowels():
    assert count_vowels("bcdfghjklmnpqrstvwxyz") == 0
    assert count_vowels("BCDFGHJKLMNPQRSTVWXYZ") == 0

def test_mixed_string():
    assert count_vowels("Hello, World!") == 3  # 'e', 'o', 'o'
    assert count_vowels("PyThOn ProGrAmMiNg") == 4  # 'o', 'o', 'A', 'i'

def test_empty_string():
    assert count_vowels("") == 0