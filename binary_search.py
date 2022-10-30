# //////////////// BINARY SEARCH ////////////////

# a function that takes a list and a target parameter
def binary_search(list, n):
    # initialize multiple variables: middle(mid), lower boundary(lb), Upper Boundary(ub), steps
    mid = 0
    lb = 0
    ub = len(list) - 1
    # -1 is added because pyhon's indexing starts from 0... might otherwise leave it at len(list) with the first item at index 0
    steps = 0

    while(lb <= ub):
        print("step", steps, ":", str(list[lb:ub+1]))
        # increase steps each time a split is done
        steps = steps + 1

        # mid point
        mid = (lb + ub) // 2

        # conditions for execution
        if n == list[mid]:
            return mid

        else:
            if n < list[mid]:
                ub = mid - 1
            else:
                lb = mid + 1

    return None


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(my_list)
target = int(input("Insert element within the list to locate: "))

print("Location:", binary_search(my_list, target))
