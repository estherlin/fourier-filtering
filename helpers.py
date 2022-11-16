import cv2
import numpy as np

def read_im(filename, colour):
    """Read in a .jpg or .png image

    Args:
        filename (str): path to image
        colour (int): imread flag for differentiating greyscale vs colour

    Returns:
        (np.ndarray): image of shape
    """
    return cv2.imread(filename, colour) # TODO: replace line with your own implementation


def write_im(filename, image):
    """Write a .jpg or .png image

    Args:
        filename (str): path to write to
        image (np.ndarray): image to be written
    """
    cv2.imwrite(filename, image)