from PIL import Image, ImageChops


def are_images_identical(image_name_1, image_name_2):
    image_1 = Image.open(image_name_1)
    image_2 = Image.open(image_name_2)
    result = ImageChops.difference(image_1, image_2).getbbox()
    if result:
        return False
    return True
