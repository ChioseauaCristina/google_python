l = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6 ]
l_asc = sorted(l)
print(l_asc)
print(l)

l_desc = sorted(l, reverse=True)
print(l_desc)
print(l)

sliced_par = l[0:9:2]
print(sliced_par)

sliced_imp = l[1:10:2]
print(sliced_imp)

for item in l:
    if item % 3 == 0:
        print(item)