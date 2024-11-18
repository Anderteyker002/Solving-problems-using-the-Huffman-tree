def sort_dicts(dicts):# A function that sorts the dictionary in ascending order of values
    list_of_dict = sorted(dicts.items(), key=lambda i: i[1]) 
    list_of_dict.reverse()                                      # The dictionary is converted into a list, after which we format the resulting list and return it. A dictionary based on a formatted list
    return dict(list_of_dict)


str_original = input('Enter the string you want to compress ')
str_changed_orig = str_original.replace(' ', '_') # We get the string that needs to be compressed, replace the spaces with _ 
str_changed_orig_2 = str_changed_orig.lower() # Converting the resulting string to lowercase

dict_of_symbol = {} # 'dict_of_symbol' - dictionary in which: The key is a character, the value is the number of repetitions of a character in a string
count_symbol = 0 


for i in str_changed_orig_2:
    count_symbol = 0 # Iterate through all the characters in the string
    x = i in dict_of_symbol.keys()
    if x == False:                      # If the symbol is not among the keys in 'dict_of_symbol', then:
        for j in str_changed_orig_2:
            if i == j:                  # Counting the number of repetitions of the symbol
                count_symbol += 1
        dict_of_symbol[i] = count_symbol # Adding the key and value to the dictionary 'dict_of_symbol'. Where: i is the key, count_symbol is the value

sorted_dict = sort_dicts(dict_of_symbol) # In 'sorted_dict' we put the dictionary 'dict_of_symbol' sorted in ascending order of values. Sorting using the 'sort_dicts' function
dict_for_verification = sort_dicts(dict_of_symbol) # Creating a second dictionary, which stores the same thing as in 'sorted_dict' (useful later)
lst = list(sorted_dict.keys())# Moving the keys from 'sorted_dict' to the list


dict_unification = {}           # 'dict_unification' is a dictionary in which characters will be stored as a key, and the values will contain the number of 0 and 1 that will replace this character
for x in lst:                   # Fill in 'dict_unification' while 0 is stored in the values
    dict_unification[x] = 0


list_for_tree = []


while len(lst) != 1: # Start the loop, which will go on until there is 1 character left in the list


    a, b = lst[-1], lst[-2]
    symbol = b + a


    list_for_tree.append(list(sorted_dict))


    sorted_dict[symbol] = sorted_dict[a] + sorted_dict[b]  # Combine the penultimate character with the last character (as in the Huffman algorithm)
    del sorted_dict[a] # After combining, it is added as a key to the dictionary, and the characters that make up the new line are removed from the dictionary
    del sorted_dict[b]


    sorted_dict = sort_dicts(sorted_dict)
    lst = list(sorted_dict.keys())       # Sorting the dictionary and list again after adding new items and deleting old ones
    

    for j in dict_unification.keys():
        if symbol.find(j) != -1:                # The number of combinations is the number of 0 and 1. So, we can calculate how much 1 such symbol weighs just by counting how many times it was combined
            dict_unification[j] = dict_unification[j] + 1


lst_answer = []

for i in dict_unification.keys():
    a1, b1 = dict_unification[i], dict_for_verification[i]      # Multiply the weight of one character by how many such characters are in the source string and add the values to the list
    lst_answer.append(a1*b1)

x = sorted(sorted_dict.values(), key=lambda i: i) 
ans = x[0] * 8                                      # We calculate the initial weight of the string


summ_ans = sum(lst_answer) # Counting the weight after compression

print()
print(' Weight before compression = ', ans, '\n', 'Weight after compression = ', summ_ans, '\n', 'Compression ratio = ', round((summ_ans/ans), 2) * 100, '%')

#002Corp