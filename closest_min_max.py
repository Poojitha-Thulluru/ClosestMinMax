# To find the length of smallest sub_array where the max(array) and min(array) are present

# Edge cases :
#    size           Array           Expected_output
# 1   0             []                  -1/0
# 2   1             [4]                  1
# 3   2             [4,15]               2
# 4   2             [4,4]                1
# 5   3             [10,15,21]           3
# 6   3             [21,10,15]           2
# 7   3             [10,10,15]           2
# 8   4             [21,7,5,10]          3

# Corner elements can be min or max In elements one min and one max should be there if there are more we need the one
# whose size is less Brute-Force takes O(N^3) - find max,min takes O(N), traverse every sub_array and checking it
# contains min or max takes O(N^2) The best approach is : "for max -> find latest min" and "for min -> find latest
# max" , we will get O(N) time complexity.


def len_closest_min_max_array(nums_array):
    max_element = max(nums_array)
    min_element = min(nums_array)
    latest_min_index = -1
    latest_max_index = -1
    length = len(nums_array)

    for index in range(len(nums_array)):
        if nums_array[index] == max_element:
            latest_max_index = index
            if latest_min_index >= 0:
                length = min(length, index - latest_min_index + 1)
        elif nums_array[index] == min_element:
            latest_min_index = index
            if latest_max_index >= 0:
                length = min(length, index - latest_max_index + 1)
    return length


try:
    print("Enter integer elements of an array separated by space to get the closest MinMax : ")
    numbers_array = list(map(int, input().split()))
    print("The length of minimum sub array is : ", len_closest_min_max_array(numbers_array))
except ValueError:
    print("Invalid input. Please Enter only Integers separated by space")