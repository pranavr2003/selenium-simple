import re

ex_str = r'sel-simple/|https://www.python.org|/^assert "Python" in title^/?febn=q/c/k-pycon?K-RETURN/}'

# global get_url_from_route
# get url with regex, remove |url| from the input, return it.

def filter_stuff(sel_str:str, get_url_from_route=''):
    """Filters the input route and returns the URL and the route minus the URL

    The URL must follow the specified guidelines."""
    test_str = list(sel_str)
    get_url_and_remove = re.findall("\\|(.*?)\\|", sel_str)

    #for item in get_url_and_remove:
    #    get_url_and_remove = list(item)
    #    get_url_from_route = item

    get_len = len(get_url_and_remove)
    test2_str = test_str[12:]
    test3_str = test_str[:10]

    url_subtracted_list = [item for item in test2_str if item not in get_url_and_remove or get_url_and_remove.remove(item)]
    url_subtracted_list.remove(url_subtracted_list[0])
    # print(url_subtracted_list)

    final_list = test3_str + url_subtracted_list
    final_str = ''.join(final_list)
    
    return [final_str, get_url_from_route]

    # print(final_str, get_url_from_route)
# print(filter_stuff(r'sel-simple/|google.us|/^from selenium import webdriver^/^driver = webdriver.Chrome()^/#user-data-dir=C:\Users\SONY\AppData\Local\Google\Chrome\User Data/#profile-directory=Default/^print("yeet")^/?febn=q/c/k-pycon?K-RETURN/}'))

