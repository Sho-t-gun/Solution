def modify_list(l):
    l[:] = [x // 2 for x in l if x % 2 == 0]


lst = [1, 2, 3, 4, 5, 6]
modify_list(lst)
print(lst)  # [1, 2, 3]
modify_list(lst)
print(lst)  # [1]

lst = [10, 5, 8, 3]
modify_list(lst)
print(lst)  # [5, 4]