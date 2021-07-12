

def get_multiple_count(num_list):
    multiple_list={}
    for current_number in num_list:
        for x in range(1,10):
            if x not in multiple_list.keys(): # if that value is not in dictionary, first add it
                multiple_list[x]=0
            if (current_number%x == 0):
                multiple_list[x]+=1
    print(multiple_list)
    return(multiple_list)

get_multiple_count([1,2,3,9])