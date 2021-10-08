from use_regex_to_filter_url import filter_stuff
import warnings

# ex_str = r'sel-simple/|https://www.python.org/|/^assert "Python" in title^/?febn=q/c/k-pycon?K-RETURN/}'

def check_if_valid_url(url):
    """Checks if the URL is in the correct format
    """

    getting_route_data = filter_stuff(url)
    route = getting_route_data[0]
    url_to_use = getting_route_data[1]

    # print(route, url_to_use)

    if route.startswith('sel-simple'):
        pass
    else:
        print(warnings.WarningMessage("The route must start with 'sel-simple/|URL|...'", UserWarning, 'check_if_valid_url.py', 12))

    return [route.split('/'), url_to_use]

# print(check_if_valid_url(ex_str))

# print(check_if_valid_url(ex_str))

