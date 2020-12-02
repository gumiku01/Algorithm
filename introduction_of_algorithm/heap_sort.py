# heap sort: sort in place, with complexity: nlgn
import random
import time
import matplotlib.pyplot as plt


def max_heapify(num_list, index, limit):
    """
    check and move the number from index to limit to ensure the property of max_heap
    :param num_list:
    :param index: start point
    :param limit: end point, because sometime we don't bring the number until the last position of list
    :return:
    """
    # for example: if index is 1, the left child has 3 and right child has index 4
    right = (index + 1) * 2
    left = right - 1
    # check there is a number greater than parent node
    massimo = index
    if left < limit and num_list[left] > num_list[massimo]:
        massimo = left
    if right < limit and num_list[right] > num_list[massimo]:
        massimo = right

    # if find changeable node: switch the position and check again in sub_heap
    if massimo != index:
        num_list[massimo], num_list[index] = num_list[index], num_list[massimo]

        max_heapify(num_list, massimo, limit)


def create_max_heap(num_list):
    """
    it make the numerical list  have the property of max_heap: the parent node is greater(or equal) than its children
    :param num_list:
    :return:
    """
    # we start from the first of penultimate level of the heap and go up to the top.
    # in this way, we keep the property for each sub_heap
    for index in range(len(num_list) // 2, -1, -1):
        max_heapify(num_list, index, len(num_list))


def heap_sort(num_list):
    """
    sort the numerical list using heap sorting
    :param num_list:
    :return:
    """
    # create the max_heap
    create_max_heap(num_list)

    # we put the root node to the tail of list, since it is the greatest number of list, and reduce the limit of size
    for limit in range(len(num_list) - 1, 0, -1):
        num_list[0], num_list[limit] = num_list[limit], num_list[0]
        # the the smaller one become the root node, and we need function max_heapify to bring if to proper position
        max_heapify(num_list, 0, limit)


if __name__ == '__main__':
    test_list = [5, 13, 2, 25, 7, 17, 20, 8, 4]
    heap_sort(test_list)
    print(test_list)

    start_length = 10
    time_usage = []
    length_list = []
    iterations = 7
    for i in range(iterations):
        random_list = random.sample(range(10000000000), start_length)
        start_time = time.time()
        heap_sort(random_list)
        length_list.append(start_length)
        time_usage.append(time.time() - start_time)
        start_length *= 10

    for i in range(len(time_usage)):
        print("time for test %d  with list length %d : %f \t " % (i + 1, length_list[i], time_usage[i]))

    plt.plot([i for i in range(iterations)], time_usage, 'ro-')
    plt.xticks([i for i in range(iterations)], ["10^" + str(i) for i in range(1, iterations + 1)])
    plt.xlabel("list length")
    plt.ylabel("time usage")
    plt.show()
