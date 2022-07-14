
def binary_search (array, element_to_find):
    lower_bound = 0
    upper_bound = len(array) - 1

    while lower_bound <= upper_bound:
        mid_point = round((upper_bound + lower_bound) / 2)

        mid_value = array[mid_point]

        if element_to_find == mid_value:
            return mid_point
        elif element_to_find < mid_value:
            upper_bound = mid_point - 1
        elif element_to_find > mid_value:
            lower_bound = mid_point + 1


def itarate_user_input():

    arr = [1,2,3,4,5,6,7]
    question = 'Please insert the number you want to search: (press "q" to exit) '

    print(f'Binary search on {arr}')
    input_search = input(question)

    while input_search != 'q':
        position = binary_search(arr, int(input_search))
        print(f'The value {input_search} was found in the {position}')
        input_search = input(question)


itarate_user_input()
