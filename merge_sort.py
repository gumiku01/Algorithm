import time
import matplotlib.pyplot as plt
import random


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
    left_list = num_list[start:middle]
    right_list = num_list[middle:end]

    # add +inf to indicate the end of list
    left_list.append(float('inf'))
    right_list.append(float('inf'))

    left_index = 0
    right_index = 0

    for num_list_index in range(start, end):
        left_value = left_list[left_index]
        right_value = right_list[right_index]

        if left_value <= right_value:
            num_list[num_list_index] = left_value
            left_index += 1
        else:
            num_list[num_list_index] = right_value
            right_index += 1


def merge_sort(num_list, start, end):
    """
    split recursively the list into 2 sublist, end it ends when sublist contains only one element, and then start merge operation
    :param num_list: list of numbers
    :param start: start index in list
    :param end: end index (not included)
    :return: list sorted in range start and end index
    """
    # we make sure that the difference between start and end is more than 1,
    # otherwise there is a problem which middle may become 0 when the input is (start=0,end=1)
    # then the second merge_sort enters in loop (middle=0, end=1), that the same as before
    if start + 1 < end:
        middle = (start + end) // 2
        merge_sort(num_list, start, middle)
        merge_sort(num_list, middle, end)
        merge(num_list, start, end, middle)


if __name__ == '__main__':

    test_list = [4, 3, 2, 5, 7, 1, 6, 9, 8, 5]
    test_start = time.time()
    merge_sort(test_list, 0, len(test_list))
    print("list sorted: ", test_list, "\ttime usage: ", time.time()-test_start)

    start_length = 10
    time_usage = []
    length_list = []
    interactions = 7
    for i in range(interactions):
        random_list = random.sample(range(10000000000), start_length)
        start_time = time.time()
        merge_sort(random_list, 0, len(random_list))
        length_list.append(start_length)
        time_usage.append(time.time() - start_time)
        start_length *= 10

    for i in range(len(time_usage)):
        print("time for test %d  with list length %d : %f \t " % (i + 1, length_list[i], time_usage[i]))

    plt.plot([i for i in range(interactions)], time_usage, 'ro-')
    plt.xticks([i for i in range(interactions)], ["10^" + str(i) for i in range(1, interactions + 1)])
    plt.xlabel("list length")
    plt.ylabel("time usage")
    plt.show()