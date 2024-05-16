def fun(d,k,v):
    d[k] = v

my_dictionary = {}
print(fun(my_dictionary, '1', 'v')) # print None as there's no return statement
print(my_dictionary) # the actual dictionary