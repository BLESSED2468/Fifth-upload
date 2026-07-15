## Task 1 — Smart Identity Card Generator

### Scenario

A company wants every intern to have a generated identity code.

### Concepts Practiced

- Strings
- Slicing
- String methods
- Concatenation

### Requirements

Ask the user for:

- First name
- Last name
- Year of birth

Generate an ID using:

- First 2 letters of first name
- Last 2 letters of last name
- Last 2 digits of birth year
- Convert everything to uppercase

### Example

Input:

```python
Samuel
Johnson
2003
```

Output:

```python
SAON03
```

### Brain Task

Figure out how to extract:

- first characters
- last characters
- last digits

### Checklist

-  Uses slicing correctly
-  Uses `.upper()`
-  Uses concatenation
-  Includes comments


# how to run
1. clone the repository

```bash
git clone <repository-url>

2. Navigate to the project directory:

```bash
cd project-folder
``

3. Run the script:

```bash
python task1.py
