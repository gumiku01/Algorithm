import time
import random
import matplotlib.pyplot as plt


# Input: sequence of n number <a1,a2,...,an>
# output: sorted sequence : a1' <= a2' <= ... <= a3'
def insertion_sort(num_list):

    for key_index in range(1, len(num_list)):
        key = num_list[key_index]
        prev_index = key_index - 1
        while prev_index >= 0 and num_list[prev_index] > key:
            num_list[prev_index + 1] = num_list[prev_index]
            prev_index -= 1

        num_list[prev_index + 1] = key


if __name__ == '__main__':
    test1 = [2, 4, 7, 3, 6, 1, 9]
    test2 = random.sample(range(1000000), 100000)

    test1_start = time.time()
    insertion_sort(test1)
    print("list sorted for test 1 {list} \t time usage : {time}s".format(list=test1, time=time.time()-test1_start))

    start_length = 10
    time_usage = []
    length_list = []
    interactions = 5
    for i in range(interactions):
        random_list = random.sample(range(10000000000), start_length)
        start_time = time.time()
        insertion_sort(random_list)
        length_list.append(start_length)
        time_usage.append(time.time() - start_time)
        start_length *= 10

    for i in range(len(time_usage)):
        print("time for test %d  with list length %d : %f \t " % (i+1, length_list[i], time_usage[i]))

    plt.plot([i for i in range(interactions)], time_usage, 'ro-')
    plt.xticks([i for i in range(interactions)], ["10^"+str(i) for i in range(1, interactions+1)])
    plt.xlabel("list length")
    plt.ylabel("time usage")
    plt.show()
