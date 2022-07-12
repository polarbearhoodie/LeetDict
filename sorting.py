def sort_square(list_in):
    n = len(list_in)
    for i in range(n):
        for j in range(n):
            if list_in[i] < list_in[j]:
                tmp = list_in[i]
                list_in[i] = list_in[j]
                list_in[j] = tmp
