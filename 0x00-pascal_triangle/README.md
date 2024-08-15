
# Pascal's Triangle Generator

## Introduction
This Python script generates Pascal's Triangle up to a given number of rows `n`. Pascal's Triangle is a triangular array of binomial coefficients, where each number is the sum of the two directly above it. This implementation returns a list of lists of integers representing Pascal’s triangle of `n`.

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Dependencies](#dependencies)
- [Configuration](#configuration)
- [Examples](#examples)
- [Troubleshooting](#troubleshooting)
- [Contributors](#contributors)
- [License](#license)

## Installation
Ensure you have Python 3 installed on your machine. This script does not require any external libraries.

```sh
sudo apt-get install python3
```

Save the script as `pascal_triangle.py`.

## Usage
Run the script by passing the desired number of rows for Pascal's Triangle as an argument to the `pascal_triangle` function.

### Example
```python
from pascal_triangle import pascal_triangle

n = 5
triangle = pascal_triangle(n)
for row in triangle:
    print(row)
```

### Script Description
```python
#!/usr/bin/python3
cat 0-main.py
#!/usr/bin/python3
"""
0-main
"""
pascal_triangle = __import__('0-pascal_triangle').pascal_triangle

def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    print_triangle(pascal_triangle(5))
```

## Features
- Generates Pascal's Triangle for a given number of rows `n`.
- Handles cases where `n <= 0` by returning an empty list.

## Dependencies
This script is implemented using standard Python 3. No additional libraries are required.

## Configuration
No configuration is required. Simply ensure you have Python 3 installed and run the script.

## Examples
Generate and print Pascal's Triangle for 5 rows:
```python
from pascal_triangle import pascal_triangle

n = 5
triangle = pascal_triangle(n)
for row in triangle:
    print(row)
```

Expected output:
```
[1]
[1, 1]
[1, 2, 1]
[1, 3, 3, 1]
[1, 4, 6, 4, 1]
```

## Troubleshooting
- Ensure `n` is a positive integer.
- If the output is an empty list, verify that `n > 0`.

## Contributors
- [Fatima ZOhra EZZAIDANI](https://github.com/Fati-Zid)

## License
This project is licensed under the MIT License.
