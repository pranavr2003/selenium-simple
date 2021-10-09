# Add option.add_experimental_option("detach", True)

import re
import warnings
from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.chrome.options import Options
from use_regex_to_filter_url import filter_stuff
from check_if_valid_url import check_if_valid_url
from char_to_py_code import char_to_py_code

test_str = r'sel-simple/|https://python.org|/#user-data-dir=C:\Users\SONY\AppData\Local\Google\Chrome\User Data/#profile-directory=Default/^assert "Python" in title^/?febn=q/c/k-pycon?K-RETURN/}'

global driver    # im sorry
global option    # at this point i hope the lord indeed is merciful
driver = webdriver.Chrome()
option = webdriver.ChromeOptions()

def add_arg_options(url):
    """Adds argument options before defining `driver`"""
    getting_route_list = check_if_valid_url(url)
    get_split_list = getting_route_list[0]
    print(get_split_list)

    # option = webdriver.ChromeOptions()
    # driver = None

    raw_double_bslash = '\\\\'

    for item in get_split_list:
        if item.startswith('#'):
            arg_to_add = item.replace('#', '').replace('\\', raw_double_bslash)
            # print(arg_to_add)
            option.add_argument(str(arg_to_add))

        else:
            print(warnings.WarningMessage("The route MUST specify a Chrome Profile to execute from", UserWarning, 'add_options_def_driver.py', 32))
        

    option.add_experimental_option("detach", True)

    driver = webdriver.Chrome(executable_path=r'C:\Windows\chromedriver.exe', chrome_options=option)
    # driver.get(filter_stuff(url)[1])

    # route_with_driver_def = check_if_valid_url(url)[0]

    # route_with_driver_def.insert(3, r"^from selenium import webdriver^")
    # route_with_driver_def.insert(2, "^from selenium.webdriver.chrome import options^")
    # route_with_driver_def.insert(3, "^from selenium.webdriver.chrome.options import Options^")
    # route_with_driver_def.insert(4, r"^driver = webdriver.Chrome()^")

    driver.get(filter_stuff(url)[1])
    exec(char_to_py_code(url))

# add_arg_options(test_str).get(filter_stuff(test_str)[1])

# THERE'S NO DRIVER.GET!!!! Added now.

