# GIF Creator using Python

A simple Python project that creates an animated GIF from multiple images using `imageio`, `Pillow`, and `NumPy`.

## Features

* Loads multiple images
* Resizes all images to the same dimensions
* Combines images into a GIF
* Supports custom frame duration and looping

## Technologies Used

* Python
* imageio
* Pillow (PIL)
* NumPy

## Installation

Install the required libraries:

```bash
pip install imageio pillow numpy
```

## Project Structure

```plaintext
project/
│
├── image1.jpeg
├── image2.jpeg
├── create_gif.py
├── team.gif
└── README.md
```

## Code Explanation

1. Load input images.
2. Read the size of the first image.
3. Resize all images to match.
4. Convert images into arrays.
5. Generate an animated GIF.

## Usage

Run:

```bash
python create_gif.py
```

Output:

```plaintext
GIF created successfully!
```

A file named `team.gif` will be generated in the project folder.

## Example

Input:

* image1.jpeg
* image2.jpeg

Output:

* team.gif

## Future Improvements

* Support more than two images
* Add image transition effects
* Allow custom output filename
* Add GUI interface

## Author

Ankit Singh

