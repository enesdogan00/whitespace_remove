from sys import argv
from cv2 import imwrite, imread


def img_read(filename):
    """Reads $filename and returns np array."""
    image = imread(filename)
    return image


def main():
    """Get an image and remove blank lines"""
    pass


if __name__ == "__main__":
    main()
    filename = argv[-1]
    image = img_read(filename)
    image_mono = image[:, :, 0]
    image = image[image_mono.std(axis=1) > 5]
    # > 5 is a threashold and could be changed.
    imwrite(filename, image)
