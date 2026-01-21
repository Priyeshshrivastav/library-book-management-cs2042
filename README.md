# Library Book Management System

## Overview
A Library Book Management System developed in Python using Agile methodology for CS2042 Assignment #1.

## Features
- **Sprint 1**: Add books, prevent duplicates.
- **Sprint 2**: Borrow and return books with validation.
- **Sprint 3**: Generate library status report.

## Folder Structure
- `src/`: Source code (`library.py`)
- `tests/`: Unit tests (`test_library.py`)
- `docs/`: User stories and traceability matrix.

## Usage
Run the following script to see a demo (if applicable) or use the `Library` class in your code.

```python
from src.library import Library
lib = Library()
lib.add_book(1, "Title", "Author")
print(lib.generate_report())
```

## Running Tests
To run all unit tests:
```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

## Git Workflow
Features were developed on `feature/sprint-x` branches and merged into `main` with tags `v0.1`, `v0.2`, `v0.3`.
