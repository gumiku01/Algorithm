import numpy as np


def get_matrix_value(matrix, i, j):
    if i < 0 or j < 0:
        return 0
    else:
        return matrix[i, j]


# input: 2 string x and y, which x = <x1, ..., xm> and y = <y1, ..., yn>
# output: the longest common substring with elements <z1, ...,zk>
#         where the index of z1 is less than index of z2 in both string x and y, and so on for others
# method: dynamic programming
def longest_common_subsequence(x, y):

    result = ""
    max_count = 0
    storage = np.zeros([len(x), len(y)])     # results of sub_problem, they can be reused to improve the performance

    # first we need to define the characteristics of of the problem and how implement them recursively
    # in our case x = <x1, ..., xm>, y = <y1, ...,yn>, suppose we have lsp = <z1, ...,zk>, it has properties:
    # 1) if xm == yn, then xm == yn == zk, and lsp' = <z1, ..., zk-1> is a lsp of x and y
    # 2) if xm != yn, then xm != zk implies z is a lsp of x = <x1, ..., xm-1> and y
    # 3) if xm != yn, then yn != zk implies z is a lsp of x and y = <y1, ..., yn-1>
    # so for storage[i,j] = {0: i < 0 or j < 0
    #                        storage[i-1, j-1]: xi == yj
    #                        max(storage[i-1, j], storage[i, j-1])}

    for i in range(len(x)):
        for j in range(len(y)):
            if x[i] == y[j]:
                storage[i, j] = get_matrix_value(storage, i-1, j-1) + 1
            elif get_matrix_value(storage, i-1, j) < get_matrix_value(storage, i, j-1):
                storage[i, j] = get_matrix_value(storage, i, j-1)
            else:
                storage[i, j] = get_matrix_value(storage, j-1, i)

    # get the lcs string
    i, j = len(x)-1, len(y)-1
    while i >= 0 or j >= 0:
        if x[i] == y[j]:
            result += x[i]
            i -= 1
            j -= 1
        else:
            possibilities = [storage[i-1, j], storage[i, j-1]]
            case = np.argmax(possibilities)
            if case == 0:
                i -= 1
            else:
                j -= 1

    return result, storage[len(x)-1, len(y)-1]


if __name__ == '__main__':
    test_x = "10010101"
    test_y = "010110110"
    lcs, count = longest_common_subsequence(test_x, test_y)
    print("the longest common subsequence of {} and {} is {} has length {}".format(test_x, test_y, lcs, count))
