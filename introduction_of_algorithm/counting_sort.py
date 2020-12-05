# counting sort: linear sorting method, but it need additional space to save the result
# in this case we suppose that the all element to be sorted is positive integer number, 0 included
import time
import random
import matplotlib.pylot as plt


def counting_sort(num_list, tot_n_elem):
    # initialize the counting list
    counting_list = [0] * tot_n_elem
    result_list = [0] * len(num_list)

    # starting count how many times occurs each number
    for number in num_list:
        counting_list[number] += 1

    # we modify the counting list to represent where is last position to be allocated for each number
    for number in range(tot_n_elem):
        if number == 0:
            counting_list[number] -= 1
        else:
            counting_list[number] += counting_list[number - 1]

    # rearrange the list
    for index in range(len(num_list) - 1, -1, -1):
        # assign the number at the position indicated at counting list
        result_list[counting_list[num_list[index]]] = num_list[index]
        counting_list[num_list[index]] -= 1

    return result_list


if __name__ == '__main__':
    test_list = [6, 0, 2, 0, 1, 3, 4, 6, 1, 3, 2]
    start_time = time.time()
    result = counting_sort(test_list, 7)
    print("the final list is: {list} \t time usage: {time:.2f}".format(list=result, time=time.time() - start_time))

    start_length = 10
    time_usage = []
    length_list = []
    iteration = 7

    for i in range(iteration):
        random_list = random.sample(range(10000000000), start_length)
        start_time = time.time()
        result = counting_sort(random_list, len(set(random_list)))
        end_time = time.time() - start_time
        time_usage.append(end_time)
        length_list.append(start_length)
        print("time for iteration number {} with length {}: {}".format(i, start_length, end_time))
        start_length *= 10


        