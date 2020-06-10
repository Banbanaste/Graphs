
def earliest_ancestor(ancestors, starting_node):
    parent_list = list()
    for relationship in ancestors:
        r = list(relationship)
        if starting_node is r[1]:
            parent_list.append(r[0])
    if len(parent_list) is 0:
        return -1
    else:
        parent_list.sort()
        return parent_list[0]


if __name__ == '__main__':
    test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
                      (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
    print(earliest_ancestor(test_ancestors, 10))
