#consider which algorithim is appropriate on the given list
numbers = [27, -3, 4, 5, 35, 2, 1, -40, 7, 18, 9, -1, 16, 100]

def list_print(items):
    for i in items:
        print(i)
    print("")

#implement the algorithim and search for th enumber 9
#add a comment to explain why it is the best choice

def sequential_search(target, items):
    for index in range(len(items)):
        if items[index] == target:
            return index
    
    return None


print("original list:")
list_print(numbers)
print(f"The index for 9 is: {sequential_search(9, numbers)}\n\n")
#best to use linear search because it is an undordered list. 


#research and iplement insertion sort on this list
def insertion_sort(items):
    for i in range(1, len(items)):
        key = items[i]
        j = i - 1
        while j >= 0 and items[j] > key:
            items[j + 1] = items[j]
            j -= 1
            items[j + 1] = key

    return items        


print("original list:")
list_print(numbers)
print(f"insertion sort new list: ")
list_print(insertion_sort(numbers))


#implement a searching algorithim you havent tried yet in 
#this task on the sorted list to find the number 9.
#add a comment to explain where you would use this 
# algorithim in the real world

def partition(items, low, high):

    pivot = items[low]

    while low < high:

        while low < high and items[high] >= pivot:
            high -= 1

        if low < high:
            items[low] = items[high]

            while low < high and items[low] <= pivot:
                low += 1
            
            if low < high: 
                items[high] = items[low]

    items[low] = pivot
    return low            


def quick_sort(items, low, high):
    if low < high:
        mid = partition(items, low, high)

        items = quick_sort(items, low, mid - 1)

        items = quick_sort(items, mid + 1, high)

    return items

numbers = [27, -3, 4, 5, 35, 2, 1, -40, 7, 18, 9, -1, 16, 100]

print("original list: ")
list_print(numbers)
print("sorted list quick sort: ")
list_print(quick_sort(numbers, 0, len(numbers) - 1))

def binary_search(target, items):
    low, high = 0, len(items) - 1

    print(f"low: {low}\n"
          f"high: {high}\n")

    while high >= low:
        mid = (low + high) // 2

        if items[mid] == target:
            return mid
        elif items[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

        print(f"mid: {mid}\n"
            f"low: {low}\n"
            f"high: {high}\n")

    return None

#numbers = [27, -3, 4, 5, 35, 2, 1, -40, 7, 18, 9, -1, 16, 100]

print(f"number 9 is in index: {binary_search(9, numbers)}")
#Maybe you could use the binary search to find a keyID
#  in a database to search for that data quickly