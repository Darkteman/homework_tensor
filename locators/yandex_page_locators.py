from selenium.webdriver.common.by import By


class Locators:
    SEARCH_FIELD = (By.CSS_SELECTOR, '#text')
    SUGGEST_LIST = (By.XPATH, '/html/body/main/div[2]/form/div[1]/div/ul')
    SEARCH_RESULT = (By.CSS_SELECTOR, '#search-result')
    FIRST_LINK = (By.XPATH, '//*["search-result"]/li[1]/div/div[2]/div[1]/a/b')

    ALL_SERVICES = (By.CSS_SELECTOR, ('.home-link2.services-suggest__item.'
                                      'services-suggest__item-more'))
    IMAGES_SECTION = (By.XPATH, ('/html/body/div/div/div/div[1]/div/div[3]/'
                                 'div[1]/span[9]/a'))
    FIRST_CATEGORY_IMAGES = (By.CSS_SELECTOR, ('.PopularRequestList-Item.Pop'
                                               'ularRequestList-Item_pos_0'))
    SEARCH_FIELD_IMAGES = (By.XPATH, ('/html/body/header/div/div[1]/div[2]/'
                                      'form/div[1]/span/span/input'))
    FIRST_SEARCH_POSITION = (By.CSS_SELECTOR, ('.mini-suggest__item.mini-su'
                                               'ggest__item_type_fulltext'))
    FIRST_IMAGE = (By.CSS_SELECTOR, ('.serp-item.serp-item_type_search.serp'
                                     '-item_group_search.serp-item_pos_0'))
    OUTSIDE_FIELD = (By.CSS_SELECTOR, ('.mini-suggest__overlay.mini-suggest'
                                       '__overlay_visible'))
    IMAGE = (By.CSS_SELECTOR, '.MMImage-Preview')
    NEXT_BUTTON = (By.CSS_SELECTOR, '.CircleButton.CircleButton_type_next')
    PREV_BUTTON = (By.CSS_SELECTOR, '.CircleButton.CircleButton_type_prev')
