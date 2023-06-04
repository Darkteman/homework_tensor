from selenium.webdriver.common.by import By


class Locators:
    """
    Описывает локаторы для выбора объектов на страницах.
    """
    SEARCH_FIELD = ((
        By.CSS_SELECTOR,
        '#text'),
        'поле поиска'
    )
    SUGGEST_LIST = ((
        By.XPATH,
        '/html/body/main/div[2]/form/div[1]/div/ul'),
        'таблица с подсказками'
    )
    SEARCH_RESULT = ((
        By.CSS_SELECTOR,
        '#search-result'),
        'результаты поиска'
    )
    FIRST_LINK = ((
        By.XPATH,
        '//*["search-result"]/li[1]/div/div[2]/div[1]/a/b'),
        'первая ссылка'
    )
    ALL_SERVICES = ((
        By.CSS_SELECTOR,
        '.home-link2.services-suggest__item.services-suggest__item-more'),
        'раздел Все сервисы'
    )
    IMAGES_SECTION = ((
        By.XPATH,
        '/html/body/div/div/div/div[1]/div/div[3]/div[1]/span[9]/a'),
        'раздел Картинки'
    )
    FIRST_CATEGORY_IMAGES = ((
        By.CSS_SELECTOR,
        '.PopularRequestList-Item.PopularRequestList-Item_pos_0'),
        'первая категория картинок'
    )
    SEARCH_FIELD_IMAGES = ((
        By.XPATH,
        '/html/body/header/div/div[1]/div[2]/form/div[1]/span/span/input'),
        'поле поиска на странице Яндекс Картинки'
    )
    FIRST_SEARCH_POSITION = ((
        By.CSS_SELECTOR,
        '.mini-suggest__item.mini-suggest__item_type_fulltext'),
        'первая позиция в таблице подсказок поля поиска Яндекс Каринки'
    )
    OUTSIDE_FIELD = ((
        By.CSS_SELECTOR,
        '.mini-suggest__overlay.mini-suggest__overlay_visible'),
        'область вне поля поиска'
    )
    FIRST_IMAGE = ((
        By.CSS_SELECTOR,
        '.serp-item.serp-item_pos_0'),
        'первое изображение в категории картинок'
    )
    IMAGE = ((
        By.CSS_SELECTOR,
        '.MMImage-Preview'),
        'открытая картинка'
    )
    NEXT_BUTTON = ((
        By.CSS_SELECTOR,
        '.CircleButton.CircleButton_type_next'),
        'кнопка перехода к следующему изображению'
    )
    PREV_BUTTON = ((
        By.CSS_SELECTOR,
        '.CircleButton.CircleButton_type_prev'),
        'кнопка перехода к предыдущему изображению'
    )
