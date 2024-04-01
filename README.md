# Custom-picture-puzzle-maker-using-Flask-and-JavaScript

This project creates a simple image puzzle game where an image is uploaded and then divided into a 3x3 grid. The player can then shuffle the tiles and attempt to solve the puzzle by rearranging them.

## Prerequisites

- Python
- Flask
- PIL (Python Imaging Library)
- Basic knowledge of HTML, CSS, and JavaScript

## Installation

1. Clone the repository:

    ```bash
    git clone (https://github.com/abhinavbibek/Custom-picture-puzzle-maker)
    ```

2. Install dependencies:

    ```bash
    pip install flask pillow
    ```

## Usage

1. Run the Flask application:

    ```bash
    python app.py
    ```

2. Open a web browser and go to `http://localhost:5000`.
3. Upload an image file using the provided form.
4. The image will be divided into tiles and displayed as a puzzle.
5. Click and drag the tiles to rearrange them and solve the puzzle.
6. The number of turns taken to solve the puzzle will be displayed.

## File Structure

- `app.py`: Contains the Flask application with routes for uploading images and serving the puzzle game.
- `templates/index.html`: HTML file containing the structure of the puzzle game.
- `static/`: Directory containing static files such as images used in the game.
  - `white.jpg`: Blank tile image.
  - `1.jpg`, `2.jpg`, ..., `9.jpg`: Images representing each tile of the puzzle.

## Contributing

Contributions are welcome! Please feel free to submit issues and pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
