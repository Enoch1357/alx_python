#! /usr/bin/python3
def common_elements(set_1, set_2):
    counter = 0
    list_common = []
    while counter <= len(set_1):
        for i in set_1:
            for j in set_2:
                if i == j:
                    list_common.append(j)
        counter += 1            
    return sorted(set(list_common))