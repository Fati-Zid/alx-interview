# Making Change

The **Making Change** project solves the **coin change problem**. The goal is to determine the minimum number of coins needed to make up a given total amount, given a list of coin denominations. This project focuses on algorithm efficiency, applying concepts like **Greedy Algorithms** and **Dynamic Programming** to create an optimal solution.

## Table of Contents

- [Description](#description)
- [Concepts](#concepts)
- [Usage](#usage)
- [Testing](#Testing the Solution)
- [Contributing](#contributing)

## Description

The coin change problem is a classic algorithmic challenge where you are given a set of coin denominations and need to find the fewest number of coins that sum up to a given total. This project implements the solution using efficient algorithms to handle a variety of coin sets and amounts. The runtime of your solution will be an important factor in evaluating its efficiency.

## Concepts

The following key concepts are essential to understanding and solving the **coin change problem**:

- **Greedy Algorithms**: A problem-solving technique that makes the locally optimal choice at each step, aiming for a global optimum.
- **Dynamic Programming**: A method for solving problems by breaking them down into simpler subproblems and storing their results to avoid redundant calculations.
- **Algorithmic Complexity**: Understanding time and space complexity to evaluate how efficiently your algorithm runs.
- **Problem-Solving Strategies**: Developing a structured approach to solving algorithmic challenges.
- **Python Programming**: Basic to advanced Python skills required to implement and test the solution.

## Usage

### Function Prototype

```python
def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet the total.

    Args:
        coins (list): A list of integers representing coin denominations.
        total (int): The total amount you need to make change for.

    Returns:
        int: The fewest number of coins needed to make the total amount.
             If the total cannot be met with the given coins, return -1.
             If the total is 0 or less, return 0.
    """
```

### Example Usage:

```python
coins = [1, 2, 5]
total = 11
print(makeChange(coins, total)) # Output: 3 (5 + 5 + 1)
```

### Testing the Solution:

```python
#!/usr/bin/python3
"""
Main file for testing
"""

makeChange = __import__('0-making_change').makeChange

print(makeChange([1, 2, 25], 37))

print(makeChange([1256, 54, 48, 16, 102], 1453))
```

### Contributing

Contributions are welcome! Please follow these steps:

Fork the repository.
Create your feature branch: git checkout -b my-feature-branch
Commit your changes: git commit -m 'Add my new feature'
Push to the branch: git push origin my-feature-branch
Open a pull request.

### Author:

Fatima Zohra EZZAIDANI ( Fati-Zid)
