# input: list of numbers, they can be positive or negatives
# output: the sublist which has maximum sum of elements


def compute_max(num_list, low, high, middle):
    # compute the left side
    left_max_sum = float('-inf')
    left_index = middle - 1
    left_sum = 0
    for left in range(middle, low - 1, -1):
        left_sum += num_list[left]
        if left_sum > left_max_sum:
            left_max_sum = left_sum
            left_index = left

    # compute the 
    right_max_sum = float('-inf')
    right_index = middle
    right_sum = 0
    for right in range(middle, high):
        right_sum += num_list[right]




def maximum_sublist(num_list, low, high):
    """
    compute the maximum sublist
    :param num_list: numerical list
    :param low: start index
    :param high: end index
    :return:
    """
    if high - low > 1:
        middle = (low + high) // 2
        left_low_index, left_high_index, left_max = maximum_sublist(num_list, low, middle)
        right_low_index, right_high_index, right_max = maximum_sublist(num_list, middle, high)


    return 1, 2, 3


if __name__ == '__main__':
    test_case = [5, 6, -8, 2, 4, -9, 8, 7, -4, 1, 3, 5, 8, -10]

