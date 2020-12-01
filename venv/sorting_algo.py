
def selection_sort(a):
    counter = 0
    minimum_index = counter
    traversing_index = counter + 1
    while(counter < len(a)):
        is_greater = False

        while(traversing_index < len(a)):
            if a[traversing_index] < a[minimum_index]:
                minimum_index = traversing_index
                is_greater = True
            traversing_index += 1

        if is_greater is True:
            min = a[counter]
            max = a[minimum_index]
            a[counter] = max
            a[minimum_index] = min

        counter += 1
        minimum_index = counter
        traversing_index = counter + 1


    return a

a = [30,2,4,122,23,43,12,6,43,2,34,6,76,]

print(selection_sort(a))

