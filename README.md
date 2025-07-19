# Chaos Game

A Python implementation of the Chaos Game algorithm that generates the famous Sierpinski triangle fractal using random iteration.

## Overview

The Chaos Game is a mathematical method for generating fractals using random processes. This implementation creates the Sierpinski triangle by:

1. Starting with an equilateral triangle and its three vertices
2. Selecting a random point inside the triangle
3. Repeatedly choosing a random vertex and moving halfway toward it
4. Plotting each new point to reveal the fractal pattern

After thousands of iterations, the plotted points form the beautiful self-similar pattern known as the Sierpinski triangle.

## Features

- **Interactive Visualization**: Real-time rendering using Tkinter
- **Mathematical Accuracy**: Proper geometric calculations for point-in-triangle detection
- **Clean Architecture**: Well-structured code with separate concerns for geometry and visualization
- **Unit Tests**: Comprehensive test coverage for core functionality
- **Type Hints**: Full type annotation for better code clarity

## Project Structure

```
juego-del-caos/
├── app/
│   ├── src/
│   │   ├── __init__.py
│   │   ├── caos.py          # Main application and visualization logic
│   │   └── triangle.py      # Point and Triangle classes with geometric operations
│   └── tests/
│       ├── __init__.py
│       ├── test_point.py    # Tests for Point class
│       └── test_triangle.py # Tests for Triangle class
├── .gitignore
└── README.md
```

## Requirements

- Python 3.7+
- tkinter (usually included with Python)
- No additional external dependencies required

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/juego-del-caos.git
cd juego-del-caos
```

2. The project uses only Python standard library modules, so no additional installation is needed.

## Usage

Run the main application:

```bash
cd app/src
python caos.py
```

This will open a window displaying:
- The initial triangle outline in black
- 10,000 points plotted in blue showing the Sierpinski triangle pattern

### Customization

You can modify the visualization by editing `caos.py`:

- **Number of iterations**: Change the value in the while loop (currently `1e4`)
- **Canvas size**: Modify the `width` and `height` parameters in `setup_canvas()`
- **Point color**: Change the `color` parameter in `add_point_to_canvas()`
- **Triangle vertices**: Modify the `vertices` list to create different triangle shapes

## Running Tests

Execute the test suite:

```bash
# From the project root directory
python -m pytest app/tests/
```

Or run individual test files:

```bash
python -m pytest app/tests/test_triangle.py
python -m pytest app/tests/test_point.py
```

## Core Classes

### Point

Represents a 2D point with x and y coordinates.

**Methods:**
- `get_mid_point(other: Point) -> Point`: Returns the midpoint between two points

### Triangle

Represents a triangle with three vertices and geometric operations.

**Methods:**
- `create_from_list(vertices: list[tuple[float, float]]) -> Triangle`: Class method to create a triangle from coordinate tuples
- `is_inside(point: Point) -> bool`: Determines if a point lies within the triangle using barycentric coordinates
- `get_vertex(index: int) -> Point`: Returns a specific vertex by index
- `get_random_vertex() -> Point`: Returns a randomly selected vertex
- `generate_inside_point() -> Point`: Generates a random point inside the triangle

## Mathematical Background

The Chaos Game demonstrates how simple rules can create complex, beautiful patterns. The Sierpinski triangle is a fractal with:

- **Self-similarity**: Each part resembles the whole at different scales
- **Fractional dimension**: Approximately 1.585 (between 1D and 2D)
- **Infinite detail**: Zooming in reveals the same pattern repeating

The algorithm converges to this fractal regardless of the starting point, showcasing the fascinating relationship between randomness and deterministic patterns.

## References

- [Sierpinski Triangle - Wikipedia](https://en.wikipedia.org/wiki/Sierpi%C5%84ski_triangle)
- [Chaos Game - Wikipedia](https://en.wikipedia.org/wiki/Chaos_game)
- [Fractals and the Chaos Game](https://mathworld.wolfram.com/ChaosGame.html)

---

**Note**: "Juego del Caos" is Spanish for "Chaos Game", reflecting the mathematical beauty that emerges from controlled randomness.
