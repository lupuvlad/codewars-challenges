# Write Number in Expanded Form
# You will be given a number and you will need to return it as a string in Expanded Form. For example:

# expanded_form(12) # Should return '10 + 2'
# expanded_form(42) # Should return '40 + 2'
# expanded_form(70304) # Should return '70000 + 300 + 4'

# NOTE: All numbers will be whole numbers greater than 0.

def expanded_form(num):
    listNum = [int(x) for x in str(num)]
    expandedList = []
    
    for i in range(1, len(listNum) + 1):
        expand_number = listNum[-i] * (10 ** (i-1))
        expandedList.append(expand_number)
    print(expandedList)
    
    greater_than_zero = list(filter(lambda n: n > 0, expandedList[::-1]))
    return " + ".join(map(str, greater_than_zero))

print(expanded_form(12455))
print(expanded_form(70304))   
print(expanded_form(7574365345))    
print(expanded_form(10027604300))          