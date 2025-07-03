def is_valid_triangle(a, b, c):
    """Check if the sides can form a valid triangle."""
    return a + b > c and a + c > b and b + c > a

def calculate_area(a, b, c):
    """Calculate area using Heron's formula."""
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return round(area, 2)

def is_close(x, y, tol=1e-9):
    """Check if two floating point numbers are close to each other."""
    return abs(x - y) <= tol

def is_right_angle(a, b, c):
    """Check if the triangle is right-angled using Pythagoras theorem."""
    sides = sorted([a, b, c])
    return is_close(sides[2]**2, sides[0]**2 + sides[1]**2)

def classify_triangle(a, b, c):
    """Classify triangle type and calculate area."""
    if not is_valid_triangle(a, b, c):
        return "Invalid triangle: sides do not satisfy triangle inequality."

    area = calculate_area(a, b, c)

    if a == b == c:
        return f"The triangle is equilateral with an area of {area}"
    elif a == b or b == c or a == c:
        if is_right_angle(a, b, c):
            return f"The triangle is an isosceles right-angled triangle with an area of {area}"
        else:
            return f"The triangle is isosceles with an area of {area}"
    else:
        if is_right_angle(a, b, c):
            return f"The triangle is a right-angled scalene triangle with an area of {area}"
        else:
            return f"The triangle is scalene with an area of {area}"

# Example usage
print(classify_triangle(3, 4, 5))
print(classify_triangle(5, 5, 5))
print(classify_triangle(5, 5, 7))
print(classify_triangle(2, 3, 4))
