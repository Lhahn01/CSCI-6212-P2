# Quick Select, Median of Medians Algorithm
# Name: Lauren Hahn
# GWID: G32735160

from numpy import random
import time

def pivotSelect(arr, k):
    # Step 1: Divide array into groups of 5
    subarrays = [arr[i : i + 5] for i in range(0, len(arr), 5)]

    # Step 2: Sort each subarrays using insertion sort
    for sub in subarrays:
        for i in range(1, len(sub)):
            key = sub[i]
            j = i - 1

            while j >= 0 and key < sub[j]:
                sub[j + 1] = sub[j]
                j = j - 1
            sub[j + 1] = key
    
    # Step 3: Identify all medians from each subarray
    allMedians = [sub[len(sub) // 2] for sub in subarrays]

    # Step 4: Find median of medians recursively using QuickSelect algorithm
    if len(allMedians) <= 5:
        pivot = allMedians[len(allMedians) // 2]
    else:
        pivot = pivotSelect(allMedians, len(allMedians) // 2)

    # Step 5: Partition the array on the median of medians
    part = partitionArray(arr, pivot)

    # Step 6: Invoke algorihtm recursively on left or right side
    if k == part:
        return pivot
    elif k < part:
         # Algotithm recursively on left partion
        return pivotSelect(arr[0 : part], k)
    else:
        # Algorithm recursively on right partition
        return pivotSelect(arr[part + 1 : len(arr)], k - part - 1)

# Method that partitions a given array
def partitionArray(arr, pivot):
    left = 0
    right = len(arr) - 1
    
    i = 0
    while i <= right:
        if arr[i] == pivot:
            i += 1
        elif arr[i] < pivot:
            # Swap with left
            temp = arr[left]
            arr[left] = arr[i]
            arr[i] = temp

            left += 1
            i += 1
        else:
            # Swap with right
            temp = arr[right]
            arr[right] = arr[i]
            arr[i] = arr[right]

            right -= 1
    return left


def main():
    # Random unsorted array:
    arr = random.randint(100, size=(95))
    if len(arr) == 0 or arr is None:
        print("Empty array")
    else:
        # Calculate time elapsed for each entry
        start = time.time_ns()
        result = pivotSelect(arr, len(arr) // 2)
        end = time.time_ns()

        # Printing portion to see time elapsed and median
        print(end - start)
        print(result)


if __name__ == "__main__":
    main()