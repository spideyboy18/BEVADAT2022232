# %%
#Create a function that decides if a list contains any odd numbers.
#return type: bool
#function name must be: contains_odd
#input parameters: input_list

# %%
def contains_odd(input_list):
     for number in input_list:
        if number % 2 != 0:
            return True
     return False
contains_odd([1,2,3,4,5])

# %%
#Create a function that accepts a list of integers, and returns a list of bool.
#The return list should be a "mask" and indicate whether the list element is odd or not.
#(return should look like this: [True,False,False,.....])
#return type: list
#function name must be: is_odd
#input parameters: input_list

# %%
def is_odd(input_list):
     result_list = []
     i = 0
     for number in input_list:
        result_list.append(number % 2 != 0)
        i+=1
     return result_list
is_odd([1,2,3,4,5])

# %%

#Create a function that accepts 2 lists of integers and returns their element wise sum. <br>
#(return should be a list)
#return type: list
#function name must be: element_wise_sum
#input parameters: input_list_1, input_list_2

# %%
def element_wise_sum(input_list_1, input_list_2):
    result = []
    for i in range(len(input_list_1)):
        result.append(input_list_1[i] + input_list_2[i])
    return result
element_wise_sum([1,2,3,4],[5,6,7,8,9])


# %%
#Create a function that accepts a dictionary and returns its items as a list of tuples
#(return should look like this: [(key,value),(key,value),....])
#return type: list
#function name must be: dict_to_list
#input parameters: input_dict

# %%
def dict_to_list(input_dict):
    result = []
    for key, value in input_dict.items():
        result.append((key, value))
    return result
dict_to_list({'a': 1, 'b': 2, 'c': 3})

# %%
#If all the functions are created convert this notebook into a .py file and push to your repo


