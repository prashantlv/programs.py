def main(arr):
    # sort
    arr.sort()
    n = len(arr)
    i, j = 1, 1
    while j < n:
        if arr[j] > 0:
            break
        j += 1

    # swap the numbers until the given condition gets satisfied
    while (arr[i] < 0) and (j < n):
        # swaping
        arr[i], arr[j] = arr[j], arr[i]

        # increment i by 2
        # because a negative number is followed by a positive number
        i += 2
        j += 1
    return arr 

if __name__ == '__main__':
    array = list(map(int, input().split()))
    result = main(array)
    print(result)
