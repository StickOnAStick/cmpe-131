my_list = [2, 10, 9, 3, 2, 8]

def sort_list(list):
    n = len(list)
    i = 0

    #Data type checking 
    print("This is a list of " + str(type(list[i])) )
    if( (type(list[0]) is not int) and (type(list[0]) is not float) ):
        #if not int or float array, exit function
        print("ERROR: Wrong data type for sorting, please enter int or float values")
        return 

    while i < n:
        j = i+1
        #print("Itteration: " + str(i) + " of the outer loop")
        while j < n:
            #print("--Itteration: " + str(j) + " of the inner loop")
            if list[i] > list[j]:
                list[i], list[j] = list[j], list[i]
            j = j + 1
        i = i + 1
    return list

print(sort_list(my_list))