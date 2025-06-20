# TermiSTL

TermiSTL is a command-line tool to view 3D STL models as ASCII art in your terminal. It uses Python with Textual for the interface, `numpy-stl` for STL loading, and `numba` for faster rendering.

## Core Features

*   View STL models in ASCII.
*   Displays model info (dimensions, volume, etc.).
*   Built-in file explorer that shows only `.stl` files and directories.
*   Navigate between STL files in the current directory.
*   Delete the currently viewed STL file (with confirmation).
*   Interactive controls:
    *   Mouse drag to rotate.
    *   Arrow keys, `u`/`o` for rotation.
    *   `PageUp`/`PageDown` to zoom.
    *   `r` to cycle through auto-rotation modes (horizontal, vertical, combined).
    *   `f`, `t`, `s` for preset views (Front, Top, Side).
    *   `a`/`d` to cycle through STL files in the current directory.
    *   `Delete` key to delete the current STL file (press again to confirm).
    *   `q` to quit.

## Requirements

*   Python 3.x
*   `numpy`, `numpy-stl`, `textual`, `numba`

## Installation

1.  Make sure Python is installed.
2.  Install dependencies:
    ```bash
    pip install numpy numpy-stl textual numba
    ```

## Usage

Run from the terminal:

```bash
python termistl.py path/to/your_model.stl
```

**Example:**

```bash
python termistl.py 3DBenchy.stl
```
