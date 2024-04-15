# The main idea is to count all the occurring characters in a string. If you have a string like aba, then the result should be {'a': 2, 'b': 1}.
# What if the string is empty? Then the result should be empty object literal, {}.

def count(s):
    counter = {}
    if len(s) > 0:
        for c in s:
            counter[c] = s.count(c)
        return counter
    else:
        return {}
    
print(count('aba'))
print(count(''))
print(count('aa'))
print(count('aabb'))