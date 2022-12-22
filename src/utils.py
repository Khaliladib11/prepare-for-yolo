# Utils file that has some useful functions

import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image


def check_file_path(file_path) -> bool:
    """
    Function to check if the file exists at a given path
    :param file_path: string
    :return: Boolean (True ot False)
    """
    if os.path.isfile(file_path):
        return True
    else:
        return False


def check_file_type(file_path, types=('.png', '.jpg', '.jpeg')) -> bool:
    """
    Function to check the file type
    :param file_path: string
    :param types: types of which you want to check
    :return: Boolean (True or False)
    """
    if file_path.lower().endswith(types):
        return True
    else:
        return False


def load_image(image_path) -> Image:
    """
    Function to load an image from a given path
    :param image_path: string - path to the image
    :return: PIL image
    """
    assert check_file_path(image_path), f"File does not exists at {image_path}"
    assert check_file_type(image_path), f"{image_path} is does not have an image extension."
    image = Image.open(image_path)
    return image


# Define color map to be used when displaying the images with bounding boxes
COLOR_MAP = ['blue', 'orange', 'green', 'red', 'purple', 'brown', 'pink', 'gray', 'olive', 'cyan', 'blue']


def show(image_path, bbox, idx, idx2cls, save_path=None) -> None:
    """
    Function to show an image with bounding boxes
    :param image_path: string - the path to the image
    :param bbox: list - list of bounding boxes
    :param idx: list - list of indexes
    :param idx2cls: dictionary - mapping from indexes to class names
    :param save_path: path tp save the image in (None by default so no save)
    :return: None
    """
    image = load_image(image_path)
    assert len(bbox) == len(idx), "Length of bounding boxes and classes do not match."
    # plot the image
    fig, ax = plt.subplots()
    ax.imshow(image)
    for i in range(len(bbox)):
        box = bbox[i]
        rect = patches.Rectangle((box[0], box[1]), box[2] - box[0], box[3] - box[1],
                                 edgecolor=COLOR_MAP[idx[i]],
                                 facecolor="none", linewidth=2)
        ax.add_patch(rect)
        plt.text(bbox[0], bbox[1], idx2cls[idx[i]], verticalalignment="top", color="white",
                 bbox={'facecolor': COLOR_MAP[idx[i]], 'pad': 0})

    plt.axis('off')
    plt.show()

    if save_path:
        assert not check_file_path(save_path), f"There is file is the same name at {save_path}."
        plt.savefig(save_path)
