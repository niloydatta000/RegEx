# Regex Helper 🧠🔍

## Overview

A quick reference and explanation tool for common regular expression (regex) patterns, written in **Python**.

## Features

- 📘 **Explain Patterns:** Get instant explanations for popular regex symbols (like `\d`, `\w`, `+`, etc.)
- 🔎 **Search by Description:** Search patterns based on what they *do* (e.g., search "digit" to find `\d`).

## Usage

### Explain a pattern

```python
from regex.regex_helper import explain

print(explain(r"\d"))  # Output: \d → Digit (0–9)
```

## Advantages

- 🚀 Fast Lookups: Quickly reference regex symbols without Googling every time.

- 🧠 Learn as You Code: Helps reinforce regex knowledge through repeated use.

- 🔧 Lightweight and Simple: No dependencies, easy to drop into any Python project.

- 🔍 Description-Based Search: Useful when you remember the purpose but not the exact symbol.

### Ideal For

- Beginners learning regex 🧑‍🎓

- Developers needing a handy regex cheatsheet 🧑‍💻

- Anyone tired of regex headaches 😵‍💫

Feel free to expand this reference dictionary or customize the helper functions for your workflow!

## Fun Fact

I used  `re` module to delvelop this project to explain the module itself.😂 
**ChatGPT** helped me to to find functions like `re.findall()`, `re.search()`, `re.escape()` etc.
