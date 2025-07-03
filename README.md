# Triangle Classifier

This Python project classifies a triangle based on the lengths of its sides and calculates its area.

## Features

- Checks if the given sides form a valid triangle
- Classifies the triangle as:
  - Equilateral
  - Isosceles
  - Scalene
  - Right-angled variants
- Calculates and returns the area using Heron's formula

## Usage

```python
from triangle import classify_triangle

print(classify_triangle(3, 4, 5))
print(classify_triangle(5, 5, 5))
print(classify_triangle(5, 5, 7))
print(classify_triangle(2, 3, 4))
