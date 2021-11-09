from use_regex_to_filter_url import filter_stuff
from check_if_valid_url import check_if_valid_url
from char_to_py_code import char_to_py_code
from add_options_def_driver import *

def main_to_ex(url):

    """Executes the mentioned URL"""

    filter_stuff(url)
    check_if_valid_url(url)
    
    add_arg_options(url)


main_to_ex(r'sel-simple/|https://python.org|/#user-data-dir=\home\pi\.config\chromium\/#profile-directory=Default/^assert "fuck" in driver.title^/?febn=q/c/k-pycon?K-RETURN/}')
