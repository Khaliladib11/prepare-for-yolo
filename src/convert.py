# In this file you will find functions to help you to convert between formats
# For now: between PASCAL VOC (XYXY) and YOLO (XYWH)

def convert_pascal_to_yolo(x_min, y_min, x_max, y_max, image_width, image_height):
    """
    Function convert pascal voc annotation format (xyxy) to yolo format (xywh)
    :param x_min: x min, it can be int or float, it must be positive
    :param y_min: y min, it can be int or float, it must be positive
    :param x_max: x max, it can be int or float, it must be positive and greater than xmin
    :param y_max: y max, it can be int or float, it must be positive and greater than ymin
    :param image_width: the width of the image, it must be positive
    :param image_height: the height of the image, it must be positive
    :return: tuple with x, y, w, h
    """

    # test
    assert check_float_type(x_min) or check_int_type(x_min), "x_min must be float or int."
    assert check_float_type(y_min) or check_int_type(y_min), "y_min must be float or int."
    assert check_float_type(x_max) or check_int_type(x_max), "x_max must be float or int."
    assert check_float_type(y_max) or check_int_type(y_max), "y_max must be float or int."

    assert check_positive(x_min), "x_min must be positive."
    assert check_positive(y_min), "y_min must be positive."
    assert check_positive(x_max), "x_max must be positive."
    assert check_positive(y_max), "y_max must be positive."

    assert x_min+x_max <= image_width, "x_min+x_max must be <= image_width"
    assert y_min+y_max <= image_height, "y_min+y_max must be <= image_height"

    assert check_positive(image_width), "image width must be greater than 0.0"  # check the image width
    assert check_positive(image_height), "image height must be greater than 0.0"  # check the image height

    x = ((x_max + x_min) / (2 * image_width))
    y = ((y_max + y_min) / (2 * image_height))
    w = (x_max - x_min) / image_width
    h = (y_max - y_min) / image_height

    return x, y, w, h


def convert_yolo_to_pascal(x, y, w, h, image_width, image_height):
    """
    Function converts YOLO annotation format (xywh) to the pascal voc format (xyxy)
    :param x: x_center, it must be a float type, it must be between 0.0 and 1.0
    :param y: y_center, it must be a float type, it must be between 0.0 and 1.0
    :param w: the width of the bounding box, it must be a float type
    :param h: the height of the bounding box, it must be a float type
    :param image_width: the width of the image, it must be positive
    :param image_height: the height of the image, it must be positive
    :return: tuple with xmin, ymin, xmax, ymax
    """

    # test
    assert check_float_type(x), "x must be float"
    assert check_float_type(y), "y must be float"
    assert check_float_type(w), "w must be float"
    assert check_float_type(h), "h must be float"

    assert check_normalized_range(x), "x must be between 0.0 and 1.0"  # check x
    assert check_normalized_range(y), "y must be between 0.0 and 1.0"  # check y
    assert check_normalized_range(w), "w must be between 0.0 and 1.0"  # check w
    assert check_normalized_range(h), "h must be between 0.0 and 1.0"  # check h

    assert check_positive(image_width), "image width must be greater than 0.0"  # check the image width
    assert check_positive(image_height), "image height must be greater than 0.0"  # check the image height

    assert x + w <= image_width, "(x+w) must be <= image width."
    assert x - w >= 0.0, "(x-w) must be >= 0.0"
    assert y + h <= image_height, "(y+h) must be <= image height."
    #assert y - h >= 0.0, "(y-h) must be >= 0.0"

    # converting
    x_min = int((x * image_width) - (w * image_width) / 2.0)  # calculating x_min
    x_max = int((x * image_width) + (w * image_width) / 2.0)  # calculating x_max

    y_min = int((y * image_height) - (h * image_height) / 2.0)  # calculating y_min
    y_max = int((y * image_height) + (h * image_height) / 2.0)  # calculating y_max

    return x_min, y_min, x_max, y_max


# Test Functions

def check_float_type(value):
    return isinstance(value, float)


def check_int_type(value):
    return isinstance(value, int)


def check_normalized_range(value):
    if 0.0 <= value <= 1.0:
        return True
    else:
        return False


def check_positive(value):
    if value >= 0.0:
        return True
    else:
        return False


if __name__ == "__main__":
    pascal = [100, 50, 300, 200]
    img_w = 500
    img_h = 400
    yolo = convert_pascal_to_yolo(pascal[0], pascal[1], pascal[2], pascal[3], img_w, img_h)
    print("YOLO ", yolo)
    pascal_conv = convert_yolo_to_pascal(yolo[0], yolo[1], yolo[2], yolo[3], img_w, img_h)
    print(pascal_conv)
    print(convert_pascal_to_yolo(pascal_conv[0], pascal_conv[1], pascal_conv[2], pascal_conv[3], img_w, img_h))
