# You will be given an array of numbers. You have to sort the odd numbers in ascending order while leaving the even numbers at their original positions.
def sort_array(arr):

    odd = []
    for i in range(len(arr)):
        if arr[i] % 2 != 0:
            odd.append(arr[i])
            arr[i] = 'odd'

    odd.sort()

    for index, n in enumerate(arr):
        if n == 'odd':
            arr[index] = odd[0]
            odd.pop(0)
    return arr


print(sort_array([5, 8, 6, 3, 4]))
