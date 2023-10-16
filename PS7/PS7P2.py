#Input Phase
a = 1
b = 1

#Process Phase
print (a)
print (b)

#Output Phase
for x in range (1, 20, 1):
    c = a + b
    print (c)
    a = b
    b = c