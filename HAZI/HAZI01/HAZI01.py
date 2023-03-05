# %%
#Create a function that returns with a subsest of a list.
#The subset's starting and ending indexes should be set as input parameters (the list aswell).
#return type: list
#function name must be: subset
#input parameters: input_list,start_index,end_index

# %%
def subset(input_list, start_index, end_index):
    return input_list[start_index:end_index]
my_list = [1, 2, 3, 4, 5]
my_subset = subset(my_list, 1, 4)
print(my_subset);

# %%
#Create a function that returns every nth element of a list.
#return type: list
#function name must be: every_nth
#input parameters: input_list,step_size

# %%
def every_nth(input_list, step_size):
    result_list = []
    for i in range(0,len(input_list),step_size):
        result_list.append(input_list[i])
    return result_list
every_nth([1,2,3,4,5,6,7,8,9],3)

# %%
#Create a function that can decide whether a list contains unique values or not
#return type: bool
#function name must be: unique
#input parameters: input_list

# %%
def unique(input_list):
    set_of_list = set(input_list)
    return len(input_list) == len(set_of_list)
unique([1,1,1,1,2])

# %%
#Create a function that can flatten a nested list ([[..],[..],..])
#return type: list
#function name must be: flatten
#input parameters: input_list

# %%
def flatten(input_list):
    result = []
    for item in input_list:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result
flatten([1, [2, [3, [4, [5, [6, [7]]]]]]])

# %%
#Create a function that concatenates n lists
#return type: list
#function name must be: merge_lists
#input parameters: *args


# %%
def merge_lists(*args):
    result = []
    for arg in args:
        result.extend(arg)
    return result
merge_lists([1,2,3,4], [5,6,7,8,9])

# %%
#Create a function that can reverse a list of tuples
#example [(1,2),...] => [(2,1),...]
#return type: list
#function name must be: reverse_tuples
#input parameters: input_list

# %%
def reverse_tuples(input_list):
    result = []
    for tup in input_list:
        result.append(tuple(reversed(tup)))
    return result
reverse_tuples([(1, 2), (3, 4), (5, 6)])

# %%
#Create a function that removes duplicates from a list
#return type: list
#function name must be: remove_duplicates
#input parameters: input_list

# %%
def remove_duplicates(input_list):
    return list(set(input_list))
remove_duplicates([1,1,2,3,4,4,4,5])

# %%
#Create a function that transposes a nested list (matrix)
#return type: list
#function name must be: transpose
#input parameters: input_list

# %%
def transpose(input_list):
    num_rows = len(input_list)
    num_cols = len(input_list[0])
    result = [[None] * num_rows for _ in range(num_cols)]
    for i in range(num_rows):
        for j in range(num_cols):
            result[j][i] = input_list[i][j]
    return result
transpose([[1, 2, 3], [4, 5, 6]])

# %%
#Create a function that can split a nested list into chunks
#chunk size is given by parameter
#return type: list
#function name must be: split_into_chunks
#input parameters: input_list,chunk_size

# %%
def split_into_chunks(input_list, chunk_size):
    result = []
    for i in range(0, len(input_list), chunk_size):
        result.append(input_list[i:i+chunk_size])
    return result

# %%
#Create a function that can merge n dictionaries
#return type: dictionary
#function name must be: merge_dicts
#input parameters: *dict

# %%
def merge_dicts(*dicts):
    result = {}
    for d in dicts:
        result.update(d)
    return result

# %%
#Create a function that receives a list of integers and sort them by parity
#and returns with a dictionary like this: {"even":[...],"odd":[...]}
#return type: dict
#function name must be: by_parity
#input parameters: input_list

# %%
def by_parity(input_list):
    even = []
    odd = []
    for num in input_list:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    result = {'even': sorted(even), 'odd': sorted(odd)}
    return result

# %%
#Create a function that receives a dictionary like this: {"some_key":[1,2,3,4],"another_key":[1,2,3,4],....}
#and return a dictionary like this : {"some_key":mean_of_values,"another_key":mean_of_values,....}
#in short calculates the mean of the values key wise
#return type: dict
#function name must be: mean_key_value
#input parameters: input_dict

# %%
def mean_key_value(input_dict):
    result_dict = {}
    for key, values in input_dict.items():
        mean_value = sum(values) / len(values)
        result_dict[key] = mean_value
    return result_dict

# %%
#If all the functions are created convert this notebook into a .py file and push to your repo


