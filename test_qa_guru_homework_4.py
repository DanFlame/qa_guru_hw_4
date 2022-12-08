def print_function_name_and_arguments(function, *function_argument):
    print(*function.__name__.capitalize().split(sep='_'), *function_argument, sep=" ")


def open_browser(browser_name):
    print_function_name_and_arguments(open_browser, browser_name)


def go_to_companyname_homepage(page_url):
    print_function_name_and_arguments(go_to_companyname_homepage, page_url)


def find_registration_button_on_login_page(page_url, button_text):
    print_function_name_and_arguments(find_registration_button_on_login_page,page_url,button_text)

open_browser('Browser')
go_to_companyname_homepage('https://company.com')
find_registration_button_on_login_page('https://company.com', '"Sign in"')
