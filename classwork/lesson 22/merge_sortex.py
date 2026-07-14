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

    print(f"temp index left: {temp_index}")
    print(f"left index: {left_index}")
    print(f"right index: {right_index}\n")

    #loop until both sections have been fully merged
    while left_index < first_section_end or right_index < second_section_end:

        #check if both sections still have elements to compare
        if left_index < first_section_end and right_index < second_section_end:

            #compare elements
            if items[left_index] < items[right_index]:

                #place smaller element in temp storage
                temp_storage[temp_index] = items[left_index]
                left_index += 1

            else: #items[right_index] <= items[left_index]
                temp_storage[temp_index] = items[right_index]
                right_index += 1
            
            temp_index += 1
            print(f"temp index both: {temp_index}\n"
                f"left index: {left_index}\n"
                f"right index: {right_index}\n"
                f"temp: {temp_storage}\n"
                f"items: {items}\n")

        #if section 1 still has elements left to merge
        elif left_index < first_section_end:

            #copy remaining elements from section 1 to temp storage
            for i in range(left_index, first_section_end):
                temp_storage[temp_index] = items[left_index]
                left_index += 1
                temp_index += 1
                print(f"temp index left: {temp_index}")
                print(f"left index: {left_index}\n"
                      f"temp: {temp_storage}\n"
                      f"items: {items}\n")
        
        #if section 2 still has elements left to merge
        else: #right_index < second_section_end
            
            #copy remaining elements from section 2 to temp storage
            for i in range(right_index, second_section_end):
                temp_storage[temp_index] = items[right_index]
                right_index += 1
                temp_index += 1
                print(f"temp index right: {temp_index}")
                print(f"right index: {right_index}\n"
                      f"temp: {temp_storage}\n"
                      f"items: {items}\n")

    #copy sorted elemetns from temporary storage back to original list
    print(f"start of merge loop.\n"
          f"temp index: {temp_index}\n"
          f"first sec start: {first_section_start}\n"
          f"temp storage: {temp_storage}\n"
          f"items: {items}")

    for i in range(temp_index):
        print(f"i: {i}")
        items[first_section_start + i] = temp_storage[i]
        print(f"item: {items[first_section_start + i]}\n"
              f"temp storage: {temp_storage[i]}\n")

    print(f"temp storage: {temp_storage}\n"
          f"items: {items}\n")


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


            print(f"first sec start: {first_section_start}\n" 
                  f"first sec end: {first_section_end }\n" 
                  f"second sec start: {second_section_start}\n" 
                  f"second sec end: {second_section_end} ")

            #call the merge function to merge the subsections
            merge(items, sections, temp_storage)

        print(f"items after merge: {items}")
        #double the size of subsections for next interation
        size_of_subsections *= 2

        print(f"size of sub section: {size_of_subsections}")

    #return sorted list
    return items


def list_print(items):
    for i in items:
        print(i)
    print("\n")    

import random

numbers = [39, 10, 46,52, 36, 35, 59, 19, 4, 54]

#for i in range(0,10):
#    numbers.append(random.randint(0,100))

list_print(numbers)
list_print(merge_sort(numbers))


