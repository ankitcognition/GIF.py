# GIF Creator using Python

A Python project that generates an animated GIF by combining multiple images using **imageio**, **Pillow**, and **NumPy**.

## Features

* Load multiple images automatically
* Resize images to a uniform size
* Generate an animated GIF
* Control frame duration and looping

## Technologies Used

* Python
* imageio
* Pillow (PIL)
* NumPy

## Installation

Install the required dependencies:

```bash
pip install imageio pillow numpy
```

## Project Structure

```plaintext
project/
│
├── .gitignore
├── README.md
├── create_gif.py
├── image1.jpeg
├── image2.jpeg
└── output.gif
```

## How It Works

1. Load input images
2. Read dimensions from the first image
3. Resize remaining images
4. Convert images into arrays
5. Export the final animated GIF

## Usage

Run:

```bash
python create_gif.py
```

Output:

```plaintext
GIF created successfully!
```

Generated file:

```plaintext
output.gif
```

## Example

Input:

* image1.jpeg
* image2.jpeg

Output:

* output.gif

## Future Improvements

* Support unlimited images
* Add transition effects
* Allow custom output filename
* Create a graphical user interface (GUI)

## Author

Ankit Singh


