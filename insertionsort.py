unsorted_list=[45,23,87,12,32,4]
for index in range(1,len(unsorted_list)):
    search_index=index
    insert_value=unsorted_list[index]
    while search_index>0 and unsorted_list[search_index-1]>insert_value:
        unsorted_list[search_index]=unsorted_list[search_index-1]
        search_index-=1

    unsorted_list[search_index]=insert_value
print(unsorted_list)    
