# quick sort: sort in place, average complexity is nlgn, but the worse case is n^2
import random
import time
import matplotlib.pyplot as plt


def partition(num_list, start, end):
    """
    rearrange the numerical list based on the pivot, which it's last element of the list
    the target is the index of the pivot
    it must guarantee that all number of index less than target are also less than pivot, and the others are greater than it
    """
    pivot = num_list[end - 1]
    first_more = start
    for current_pos in range(start, end - 1):
        if num_list[current_pos] <= pivot:
            num_list[first_more], num_list[current_pos] = num_list[current_pos], num_list[first_more]
            first_more += 1
    # the element of first more switched with the pivot index
    num_list[first_more], num_list[end - 1] = num_list[end - 1], num_list[first_more]
    return first_more


def quick_sort(num_list, start, end):
    if start + 1 < end: # end of iteration condition
        pivot_index = partition(num_list, start, end)
        quick_sort(num_list, start, pivot_index)
        quick_sort(num_list, pivot_index, end)


if __name__ == '__main__':
    test_list = [13, 19, 9, 5, 12, 8, 7, 4, 21, 2, 6, 11]
    quick_sort(test_list, 0, len(test_list))
    print(test_list)

    start_length = 10
    time_usage = []
    length_list = []
    iterations = 7
    for iteration in range(iterations):
        random_list = random.sample(range(10000000000), start_length)
        start_time = time.time()
        quick_sort(random_list, 0, len(random_list))
        time_usage.append(time.time() - start_time)
        length_list.append(start_length)
        start_length *= 10

    for i in range(iterations):
        print("time for test {iteration} with length {length} : {time}"
              .format(iteration=i, length=length_list[i], time=time_usage[i]))

    # plot the graph
    plt.plot([i for i in range(iterations)], time_usage, 'ro-')
    plt.xticks([i for i in range(iterations)], ["10^"+str(i) for i in range(1, iterations + 1)])
    plt.xlabel("length")
    plt.ylabel("time usage")
    plt.show()