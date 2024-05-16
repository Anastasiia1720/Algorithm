def sorting_algorithm_1(list_of_numbers):
    new_list = []
    while len(list_of_numbers) > 0:
        for x in list_of_numbers:
            if x == min(list_of_numbers):
                list_of_numbers.remove(x)
                new_list.append(x)
    return new_list


print(sorting_algorithm_1([3, 2, 9, 7, 1, 4]))
