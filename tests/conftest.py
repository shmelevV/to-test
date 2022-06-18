import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import warnings

from pages.Admin_page import AdminPage
from pages.DB_Page import DataBasePage
from pages.Groups_page import GroupsPage
from pages.Login_page import LoginPage
from pages.Main_page import MainPage
from pages.Add_user_page import AddUserPage
from pages.Posts_page import PostsPage
from pages.User_page import UserPage

from configs.ui_parsing import username, password, new_username, new_password
from configs.db_parser import delete_group, delete_user, delete_auth_user_group


@pytest.fixture(scope='class')
def browser():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-gpu')
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(),
                              options=chrome_options)
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.fixture(scope="class")
def login_page(browser):
    login_page = LoginPage(browser)
    login_page.open_login_page()
    yield login_page
    browser.quit()


@pytest.fixture(scope="class")
def main_page(browser):
    main_page = MainPage(browser)
    main_page.open_main_page()
    yield main_page
    browser.quit()


@pytest.fixture()
def groups_page(browser):
    login_page = LoginPage(browser)
    login_page.open_login_page()
    login_page.login(username, password)
    groups_page = GroupsPage(browser)
    groups_page.open_groups_page()
    yield groups_page


@pytest.fixture()
def add_user_page(browser):
    add_user_page = AddUserPage(browser)
    add_user_page.open_add_user_page()
    yield add_user_page


@pytest.fixture()
def log_in_new_user(browser):
    user_page = UserPage(browser)
    user_page.click_logout_field()
    login_page = LoginPage(browser)
    login_page.open_login_page()
    login_page.login(new_username, new_password)
    admin_page = AdminPage(browser)
    admin_page.open_admin_page()
    yield admin_page
    browser.quit()


@pytest.fixture(scope="class")
def posts_page(browser):
    posts_page = PostsPage(browser)
    posts_page.open_posts_page()
    yield posts_page
    browser.quit()


@pytest.fixture(scope="class")
def db_conn():
    db = DataBasePage()
    conn = db.create_connection()
    yield conn
    db.executions(conn, delete_auth_user_group)
    db.executions(conn, delete_user)
    db.executions(conn, delete_group)
    conn.close()
