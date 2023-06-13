def new_in_list(original_list, position, new_element):

    if position >= len(original_list) or position < 0:
        return original_list

    modified_list = original_list[:]
    modified_list[position] = new_element
    return modified_list

