import pyautogui
import numpy
from PIL import ImageGrab, ImageOps
import time

class Coordinates:
    """
    Handles all of the coordinates for where to click

    """
    start_button = (340, 580)
    level1_squares = [(200, 300), (300, 300), (450, 300),
    (200, 400), (300, 400), (450, 400), (200, 540),
    (300, 540), (450, 540)]

def start_game():
    """
    Moves the mouse to the coordinates
    of the start button and clicks it

    """
    pyautogui.click(Coordinates.start_button)

def image_grab(square):
    """
    Takes a screenshot of the game
    
    """
    area = (square[0], square[1],
    square[0] + 10, square[1] + 10)
    image = ImageGrab.grab(area)
    gray_image = ImageOps.grayscale(image)
    color = numpy.array(gray_image.getcolors())
    return color.sum()

def click_square(square):
    pyautogui.click(square)

def main():
    start_game()
    time.sleep(.38)
    selected_squares = []
    start = time.perf_counter()
    for square in Coordinates.level1_squares:
        if (image_grab(square) == 355):
            selected_squares.append(square)
    end = time.perf_counter()
    print(end - start)

    time.sleep(1)
    for square in selected_squares:
        click_square(square)
    

main()


