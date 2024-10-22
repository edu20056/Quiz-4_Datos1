from datetime import datetime
import random


def bubble_sort(arr):
    start_time = datetime.now()

    # Outer loop to iterate through the list n times
    for n in range(len(arr) - 1, 0, -1):

        # Inner loop to compare adjacent elements
        for i in range(n):
            if arr[i] > arr[i + 1]:

                # Swap elements if they are in the wrong order
                swapped = True
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                finish_time = datetime.now()

    total_time = finish_time - start_time
    print(f"El tiempo de Bubble Sort fue de: {total_time}")


# Function to find the partition position
def partition(array, low, high):

    # choose the rightmost element as pivot
    pivot = array[high]

    # pointer for greater element
    i = low - 1

    # traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:

            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1

            # Swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])

    # Swap the pivot element with the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])

    # Return the position from where partition is done
    return i + 1

# function to perform quicksort


def quickSort(array, low, high):
    if low < high:

        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)

        # Recursive call on the left of pivot
        quickSort(array, low, pi - 1)

        # Recursive call on the right of pivot
        quickSort(array, pi + 1, high)

#Function to create random numbers on a array depending on entry number.
def create_random_array(n):
    return [random.randint(0, 100) for _ in range(n)]



for i in range(10):
    bubble_sort(create_random_array(5000)) #Change 5000 the number wanted

for i in range(10):
    start_time = datetime.now()
    quickSort(create_random_array(5000), 0, 4999) #Change 5000 and 4999 for the numbers wanted.
    finish_time = datetime.now()
    total_time = finish_time - start_time
    print(f"El tiempo de Quick Sort fue de: {total_time}")


#Both codes retrieves from:
#Quick sort: https://www.geeksforgeeks.org/python-program-for-quicksort/
#Bubble sort: https://www.geeksforgeeks.org/python-program-for-bubble-sort/