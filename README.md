# Week 6 Assignment - Safe Functions

## Files

- `safe_tools.py` - Contains safe functions for division, number conversion, and dictionary lookup.
- `unbreakable.py` - Demonstrates handling invalid input without crashing.
- `README.md` - Describes the assignment and the purpose of each file.

## Question

Why can the `if` check not catch `abc` on its own?

An `if` check can test a condition, but converting `"abc"` with `int()` causes a `ValueError`. The `try/except` block catches this error and keeps the program from crashing.