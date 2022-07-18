def merge_two(list_a, list_b):
    count = {}
    for x in list_a:
        count[x] = 1
    for y in list_b:
        if count.get(y, 0) == 0:
            list_a.append(y)

    return list_a


def merge_k_lists(super_list):
    # make a dict for everything in all lists

    # make a unique list

    # for every element, mark if the list scontains it
    # if two lists contain the same element, exclude them from searches