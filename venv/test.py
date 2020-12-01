
a = [2,3,5]

for item in range(len(a)):
    print(a[item])




    while(counter <= len(a)):
        present_count = counter
        for present_count in range(len(a)):
            if a[minimum_index] > a[traversing_index]:
                minimum_index = traversing_index
        min = a[minimum_index]
        max = a[traversing_index]
        a[minimum_index] = max
        a[traversing_index] = min

        counter = counter + 1
        minimum_index = counter
        traversing_index = counter + 1
