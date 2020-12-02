# input: list of numbers, they can be positive or negatives
# output: the sublist which has maximum sum of elements


def compute_cross_max(num_list, low, high, middle):
    # compute the left side
    left_max_sum = float('-inf')
    left_index = middle - 1
    left_sum = 0
    for left in range(middle - 1, low - 1, -1):
        left_sum += num_list[left]
        if left_sum > left_max_sum:
            left_max_sum = left_sum
            left_index = left

    # compute the right side
    right_max_sum = float('-inf')
    right_index = middle
    right_sum = 0
    for right in range(middle, high):
        right_sum += num_list[right]
        if right_sum > right_max_sum:
            right_max_sum = right_sum
            right_index = right

    return left_index, right_index, left_max_sum + right_max_sum


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
        # the possible result can be contained into 3 cases:
        # 1) sum of the elements on the left side
        # 2) sum of the elements on the right side
        # 3) sum of the elements across the middle point
        left_low_index, left_high_index, left_max = maximum_sublist(num_list, low, middle)
        right_low_index, right_high_index, right_max = maximum_sublist(num_list, middle, high)
        cross_low_index, cross_high_index, cross_max = compute_cross_max(num_list, low, high, middle)
        print(cross_max)
        if left_max >= right_max and left_max >= cross_max:
            return left_low_index, left_high_index, left_max
        elif right_max >= left_max and right_max >= cross_max:
            return right_low_index, right_high_index, right_max
        else:
            return cross_low_index, cross_high_index, cross_max
    # otherwise only one element in list
    return low, high, num_list[low]


if __name__ == '__main__':
    test_case = [5, 6, -8, 2, 4, -9, 8, 7, -4, 1, 3, 5, 8, -10]
    left_index, right_index, max_sum = maximum_sublist(test_case, 0, len(test_case))
    print("the resutl: the max sum is %d from index %d to %d -> " % (max_sum, left_index, right_index),
          test_case[left_index: right_index+1])
