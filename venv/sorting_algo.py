
def selection_sort(a):
    counter = 0
    minimum_index = counter
    traversing_index = counter + 1
    while(counter < len(a)):
        for traversing_index in range(counter, len(a)):
            if a[traversing_index] < a[minimum_index]:
                minimum_index = traversing_index
            traversing_index += 1

        a[counter], a[minimum_index] = a[minimum_index], a[counter]
        counter += 1
        minimum_index = counter
        traversing_index = counter + 1

    return a

def bubble_sort(a):
    swapped_values = True
    traversing_index = 0

    while(swapped_values):
        swapped_values = False
        traversing_index = 0
        for traversing_index in range(len(a)-1):
            if a[traversing_index] > a[traversing_index + 1]:
                a[traversing_index], a[traversing_index + 1] = a[traversing_index + 1], a[traversing_index]
                swapped_values = True

    return a

def cocktail_shaker_sort(a):
    swapped_values = True
    traversing_index = 0

    while(swapped_values):
        swapped_values = False
        traversing_index = 0
        for i in range(0,len(a)-1):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                swapped_values = True
            traversing_index += 1

        if swapped_values:
            for i in range(traversing_index, (len(a)-len(a)+1), -1):
                if a[i] < a[i - 1]:
                    a[i], a[i - 1] = a[i - 1], a[i]
                    swapped_values = True
                traversing_index -= 1

    return a

def odd_even_sort(a):
    is_sorted = False
    while(is_sorted == False):
        is_sorted = True
        #Odd Face
        for i in range(1,len(a)-1,2):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                is_sorted = False
        #Even Face
        for i in range(0, len(a)-1,2):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                is_sorted = False

    return a

a = [30,2,4,8,23,1,6,9,2,45,2,34]

print(odd_even_sort(a))

