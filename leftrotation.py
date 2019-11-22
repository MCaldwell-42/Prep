

def leftrotation(the_array, times):
    i=0
    while i < times:
        array_var = the_array[0]
        the_array.append(array_var)
        the_array.remove(array_var)
        i += 1
    print(the_array)


array_1 = [1,2,3,4,5]

leftrotation(array_1, 3)