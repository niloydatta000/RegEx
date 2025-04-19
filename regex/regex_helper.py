# regex_helper.py
# This module provides a quick reference for regex patterns and their descriptions.
# It also includes functions to explain a regex pattern and search for patterns by description.


import re
from typing import List

regex_patterns = {
    r"\d": "Digit (0–9)",
    r"\w": "Word, alphanumeric character, underscore (a-z, A-Z, 0-9, _)",
    r"\s": "Whitespace character",
    r".": "Any character except newline",
    r"^": "Start of string",
    r"$": "End of string",
    r"\D": "Not a digit",
    r"\W": "Not a word character",
    r"\S": "Not whitespace",
    r"*": "0 or more repetitions",
    r"+": "1 or more repetitions",
    r"?": "0 or 1 repetition",
    r"{n}": "Exactly n times",
    r"{n,}": "At least n times",
    r"{n,m}": "Between n and m times",
    r"[abc]": "Any character a, b, or c",
    r"[^abc]": "Any character except a, b, or c",
}



def explain(pattern: str) -> str:
    """
    Explain a regex pattern using the quick reference dictionary.
    Args:
        pattern (str): The regex pattern to explain.
    Returns:
        str: A description of the regex pattern.
        """
    
    for key, desc in regex_patterns.items():
        if pattern == key:
            return f"{pattern} → {desc}"
    return "Pattern not found in quick reference."



def search_by_description(keyword: str) -> List[str]:
    """
    Search for regex patterns by description.
    Args:
        keyword (str): The keyword to search for in the descriptions.
    Returns:
        list: A list of regex patterns that match the keyword.
        """
    
    words = re.findall(r'\w+', keyword.lower())
    results = [f"{pattern} → {desc}" for pattern, desc in regex_patterns.items() if all(re.search(re.escape(word), desc.lower()) for word in words)]
    
    return results if results else ["No matches found."]
    
