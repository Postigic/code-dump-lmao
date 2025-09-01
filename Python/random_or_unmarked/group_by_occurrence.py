def group_by_occurence(num_list):
    groups = {}
    order = []

    for num in num_list:
        if num not in groups:
            groups[num] = []
            order.append(num)
        groups[num].append(num)

    return [groups[num] for num in order]

print(group_by_occurence([3, 2, 6, 2, 1, 3]))