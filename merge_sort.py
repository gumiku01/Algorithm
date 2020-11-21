# Input: sequence of n number <a1,a2,...,an>
# output: sorted sequence : a1' <= a2' <= ... <= a3'


def merge(num_list, start, end, middle):
    """
    merge the list of number between the start index and end index(not included)
    :param num_list: list of number
    :param start: start index
    :param end: end index (not included)
    :param middle: the middle index used to split into sublist
    :return: list sorted between start and end index
    """
    left_list = num_list[start: middle]
    right_list = num_list[middle : end]

    left_list.append(float('inf'))
    right_list.append(float('inf'))

    left_index = start
    right_index = middle

    for num_list_index in range(start, end):
        left_value = left_list[left_index]
        right_value = right_list[right_index]

        if left_value <= right_value:
            num_list[num_list_index] = left_value
            left_index += 1
        else:
            num_list[num_list_index] = right_value
            right_index += 1


def merge_sort(num_list, start, end, i, j):
    """
    split recursively the list into 2 sublist, end it ends when sublist contains only one element, and then start merge operation
    :param num_list: list of numbers
    :param start: start index in list
    :param end: end index (not included)
    :return: list sorted in range start and end index
    """
    print(i,",", j, "  ->  ",start, end)
    if start < end:
        middle = (start + end) // 2
        print("middle  ", middle)
        merge_sort(num_list, start, middle, i+1, j)

        merge_sort(num_list, middle+1, end, i, j+1)
        merge(num_list, start, end, middle+1)


if __name__ == '__main__':
    test_list = [3, 4, 2, 5, 7, 1, 6, 9, 8, 5]
    merge_sort(test_list, 0, len(test_list), 1, 1)

    print(test_list)