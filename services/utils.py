from PIL import Image, ImageChops


def are_images_identical(image_name_1, image_name_2):
    """
    Возвращает булево значение при сравнении 2ух картинок.
    Если изображения одинаковые, вернется True.
    """
    image_1 = Image.open(image_name_1)
    image_2 = Image.open(image_name_2)
    result = ImageChops.difference(image_1, image_2).getbbox()
    if result:
        return False
    return True


def add_empty_line_in_logs():
    """
    Добавляет пустую строку в конце файла логов.
    """
    with open('services/logging/debag.log', 'a') as file:
        file.write('\n')
