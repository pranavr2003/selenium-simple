from use_regex_to_filter_url import filter_stuff
from check_if_valid_url import check_if_valid_url
from char_to_py_code import char_to_py_code
from add_options_def_driver import add_arg_options

def main_to_ex(url):
    filter_stuff(url)
    check_if_valid_url(url)
    char_to_py_code(url)
    add_arg_options(url).get(filter_stuff(url)[1])

    driver = add_arg_options(url)

    # for item in filter_stuff(url):
    #     print(item)

main_to_ex('sel-simple/|https://python.org|/#user-data-dir=C:\Users\SONY\AppData\Local\Google\Chrome\User Data/#profile-directory=Default/^assert "Python" in driver.title^/?febn=q/c/k-pycon?K-RETURN/}')
