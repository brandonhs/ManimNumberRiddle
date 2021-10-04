# Manim Number Riddle

## About The Project

This repo contains a manim animation for the 1.1.6 Number Riddle Project

### Built With

-   [python](https://www.python.org/)
-   [manim](https://www.manim.community/)

## Getting Started

To get a local copy up and running, run, `git clone https://github.com/brandonhs/ManimNumberRiddle`

### Prerequisites

Required dev tools

-   python
-   pip

### Running the test program

1.  Clone the repo
    ```sh
    git clone https://github.com/brandonhs/ManimNumberRiddle
    ```
2.  Install dependencies

    ```sh
    pip install manim
    ```

3.  Run

    For high quality:
    ```sh
    manim main.py S1 -qh
    manim main.py S2 -qh # Scene 2 will take a LONG time to render
    manim main.py S3 -qh
    ```

    For low quality:
    ```sh
    manim main.py S1 -ql
    manim main.py S2 -ql # Recommended for Scene 2
    manim main.py S3 -ql
    ```