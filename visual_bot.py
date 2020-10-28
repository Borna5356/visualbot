import pyautogui
import numpy
import PIL
import time

class Coordinates:
    """
    Handles all of the coordinates for where to click

    """
    start_button = (340, 580)
    level1_squares = [(200, 300), (300, 300), (450, 300),
    (200, 400), (300, 400), (450, 400), (200, 540),
    (300, 540), (450, 540)]

def start():
    """
    Moves the mouse to the coordinates
    of the start button and clicks it

    """
    pyautogui.click(Coordinates.start_button)

def main():
    start()

main()


