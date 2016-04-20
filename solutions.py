from basic_functions import *

def is_list_of_strings(l):
    if is_empty(l):
        return True
    else:
        if is_str(head(l)):
            return is_list_of_strings(tail(l))
        else:
            return False
