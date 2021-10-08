from use_regex_to_filter_url import filter_stuff
from check_if_valid_url import check_if_valid_url
from char_to_py_code import char_to_py_code

def main_to_ex(url):
    filter_stuff(url)
    check_if_valid_url(url)
    char_to_py_code(url)

    # for item in filter_stuff(url):
    #     print(item)

main_to_ex(r"sel-simple/|https://www.python.org|/^print('yee')^/?febn=q/c/k-pycon?K-RETURN/}")


