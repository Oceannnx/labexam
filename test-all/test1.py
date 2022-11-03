# def a(b):   
#     return b+10
# print(a(10))

# number = [-1,-2,-3,0,1,2,3]
# print(number)

# numbers = list(int(i) for i in input().split())
# print(list(filter(lambda x : x >=0 ,numbers)))

# (lambda (Parametre) : (arg...))
# x = (lambda i : i+10)
# print(x(10))
# Output : 20

# thisdict = {
#   "bread": 10,
#   "milk": 12,
#   "coffee": 15
# }
# thisdict[toffie] = 10   ###เพิ่ม dict ใหม่
# thisdict[toffie] = 20   ###อัพเดตค่า dict ใหม่
# new_dict = {key : value/40 for (key,value) in thisdict.items()}
# print(new_dict)

# a = list(range(10))
# b = list(range(10,18))
# print(list("{} + {} = {}".format(i,j,i+j) for i,j in zip(a,b)))

# list_a = ["bread","milk","coffee"]
# list_b = [10,20,30]
# dict_a = dict(zip(list_a,list_b))

# print(dict_a)

# dict_a = {'bread': 10, 'milk': 12, 'coffee': 14}

# list_c = list(dict_a.keys())
# print(list_c)
# list_d = list(i for i in dict_a.values() if i >=20)
# print(list_d)

# import functools
 
# # initializing list
# lis = [1, 3, 5, 6, 2]
 
# # using reduce to compute sum of list
# print("The sum of the list elements is : ", end="")
# print(functools.reduce(lambda a, b: a+b, lis))

# li1 = [0.2, -1000, 1000, 33.21, -101.12, 0.01, 212, 0.4, -0.3, -100]
# print(list(map(lambda x : x+10000 if x>-0.5 and x<0.5 else x ,li1)))

# li2 = [i+10000 if i>-0.5 and i<0.5 else i for i in li1]
# print(li2)

# switch = input()
# swap_count = 0
# for i in range(len(switch)-1):
#     if switch[i] != switch[i+1]:
#         swap_count+=1
#     else : continue
# print(swap_count)

# a = input()
# print(sum(list(1 for i in range(len(a)-1) if a[i]!=a[i+1])))

# p='100111001'
# print(len([i for i in range(len(p)-1) if p[i] != p[i+1]]) )

# round = int(input())
# list_1 = [(input()) for i in round]
# print(list_1)

