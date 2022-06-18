from selenium.webdriver.common.by import By


class PostsPageLocators:

    CHECKBOXES = (By.CLASS_NAME, "action-select")
    SELECT = (By.TAG_NAME, "select")
    GO = (By.CLASS_NAME, "button")
    SURE = (By.CSS_SELECTOR, "[type='submit']")
    ALL_PICS = (By.PARTIAL_LINK_TEXT, "Post object")
    DATE = (By.CLASS_NAME, "vDateField")
    TIME = (By.CLASS_NAME, "vTimeField")
    SAVE = (By.CSS_SELECTOR, "[type='submit']")
