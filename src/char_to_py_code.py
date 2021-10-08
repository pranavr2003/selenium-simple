from check_if_valid_url import *

def str_to_py_code(get_input_str:str):
    """Converts the given string starting with `^` to Python code \n
    Every char more than one `^` counts one indent up
    """
    if get_input_str.startswith('^'):
        count = get_input_str.count('^')
        # print(count)
        count_divided = count/2
        keep_indent_count = -1
        check_indent_count = int(keep_indent_count + count_divided)

        code_to_exec = '\n' + '    '*check_indent_count + get_input_str.replace('^', '')

        return code_to_exec


def char_to_py_code(url):
    """Converts char `^` to Python code \n
    Every char more than one `^` counts one indent up
    """
    check_for_validity = check_if_valid_url(url)
    get_split_list = check_for_validity[0]

    store_code_to_exec = ''

    for item in get_split_list:

        if item.startswith('^'):
            store_code_to_exec += str_to_py_code(item)
        else:
            pass

    exec(store_code_to_exec)

# char_to_py_code("sel-simple/|google.com|/^if 1==2:^/^^print('yo mama')^^/^else:^/^^print('yee')^^/")
