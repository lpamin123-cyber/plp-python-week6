# PLP Python Week 6 Assignment

## File Descriptions
* **safe_tools.py**: Contains `safe_divide`, `safe_number`, and `get_field` functions that handle potential runtime exceptions (`ZeroDivisionError`, `ValueError`, `KeyError`) gracefully without crashing.
* **unbreakable.py**: Demonstrates continuous user input validation using exception handling.

## Reflection Question
**Why can an `if` check not catch `"abc"` when converting to an integer on its own?**

An `if` statement like `if text:` only checks whether the variable is truthy (non-empty), not whether its contents are composed entirely of valid numerical characters. Calling `int("abc")` causes Python to raise a `ValueError` during parsing, which conditional evaluation alone cannot intercept; an exception handler (`try/except`) is strictly required to catch the runtime parse failure and prevent the program from crashing.
