
def print_name_function_and_agruments(name_func, *args):
    name_func = name_func.__name__.replace("_", " ").upper()
    print(name_func, *args)


def open_browser(browser_name):
    print_name_function_and_agruments(open_browser, browser_name)


def go_to_companyname_homepage(page_url):
    print_name_function_and_agruments(go_to_companyname_homepage, page_url)


def find_registration_button_on_login_page(page_url, button_text):
    print_name_function_and_agruments(find_registration_button_on_login_page, button_text, page_url)


open_browser(browser_name="Chrome")
go_to_companyname_homepage(page_url="https://qa.guru/")
find_registration_button_on_login_page(page_url="https://qa.guru/", button_text="login")