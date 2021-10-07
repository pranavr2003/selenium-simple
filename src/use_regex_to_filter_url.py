import re

ex_str = r'sel-simple/|https://www.google.com|/^assert "Python" in title^/?febn=q/c/k-pycon?K-RETURN/}'
test_str = list(ex_str)

# get url with regex, remove |url| from the input, return it. globalized url, hope the lord forgives me

def filter_stuff(sel_str):
    get_url_and_remove = re.findall("\\|(.*?)\\|", sel_str)

    for item in get_url_and_remove:
        get_url_and_remove = list(item)

        global get_url_from_route   # im sorry
        get_url_from_route = item

    get_len = len(get_url_and_remove)
    test2_str = test_str[12:]
    test3_str = test_str[:10]

    url_subtracted_list = [item for item in test2_str if item not in get_url_and_remove or get_url_and_remove.remove(item)]
    url_subtracted_list.remove(url_subtracted_list[0])
    # print(url_subtracted_list)

    final_list = test3_str + url_subtracted_list
    final_str = ''.join(final_list)
    
    return final_str

# print(filter_stuff(ex_str))
# print(get_url_from_route)

