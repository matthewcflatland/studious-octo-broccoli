def merge(items, sections, temp_storage):
    #unpack the sections tuple to get the start and end
    #indices of each section.
    (first_section_start, first_section_end), (
        second_section_start,
        second_section_end,
    ) = sections

    #intialize indicies for 2 secionts and temp storage
    left_index = first_section_start
    right_index = second_section_start
    temp_index = 0

    #loop until both sections have been fully merged
    while left_index < first_section_end or right_index < second_section_end:

        #check if both sections still have elements to compare
        if left_index < first_section_end and right_index < second_section_end:

            #compare elements
            if len(items[left_index]) < len(items[right_index]):

                #place smaller element in temp storage
                temp_storage[temp_index] = items[left_index]
                left_index += 1

            else: #items[right_index] <= items[left_index]
                temp_storage[temp_index] = items[right_index]
                right_index += 1
            
            temp_index += 1

        #if section 1 still has elements left to merge
        elif left_index < first_section_end:

            #copy remaining elements from section 1 to temp storage
            for i in range(left_index, first_section_end):
                temp_storage[temp_index] = items[left_index]
                left_index += 1
                temp_index += 1

        
        #if section 2 still has elements left to merge
        else: #right_index < second_section_end
            
            #copy remaining elements from section 2 to temp storage
            for i in range(right_index, second_section_end):
                temp_storage[temp_index] = items[right_index]
                right_index += 1
                temp_index += 1


    #copy sorted elemetns from temporary storage back to original list

    for i in range(temp_index):
        items[first_section_start + i] = temp_storage[i]
        

def merge_sort(items):
    items_length = len(items)

    temp_storage = [None] * items_length

    size_of_subsections = 1

    #iterates while subsections is less than length of list
    while size_of_subsections < items_length:
        
        #iterate over the list in steps of subsections
        for i in range(0, items_length, size_of_subsections * 2):

            #determins the start and end indices of the 2 subsections
            #to merge
            first_section_start, first_section_end = i, min(
                i + size_of_subsections, items_length)
            second_section_start, second_section_end = first_section_end, min(
                first_section_end + size_of_subsections, items_length
            )

            #define the sections to merge
            sections = (first_section_start, first_section_end), (
                second_section_start, second_section_end,
            )

            #call the merge function to merge the subsections
            merge(items, sections, temp_storage)

        #double the size of subsections for next interation
        size_of_subsections *= 2

    #return sorted list
    return items


def list_print(items):
    for i in items:
        print(i)
    print("")    

import random

#numbers = []

#for i in range(0,10):
#    numbers.append(random.randint(0,100))

#list_print(numbers)
#list_print(merge_sort(numbers))

strings = ["hello world", "today is a wonderful day", "happy time"]

print("original list: ")
list_print(strings)

print("sorted list by string length: ")
new_strings = merge_sort(strings)
list_print(new_strings)


