###========= convert a string to list without using split() ==========

sentence = "this is my python program"
temp = ""
new_sentence = []

# for i in sentence :
#     if i != " ":
#         temp = temp + i 

#     else :
#         new_sentence.append(temp)
#         temp = ""

# print(new_sentence)

## ================================================================================


# for i in sentence :
#     if i == " ":
#         new_sentence.append(temp)
#         temp = ""
#     else :
#         temp = temp + i 
# print(new_sentence)
#

# ================= swap 2 numbers ===========================
# def swap2number(a,b):
#     temp = a 
#     a = b 
#     b = temp 

#     return a,b

# print(swap2number(16,24))

# ==================== check prime number =========================

# def check_prime(num):
#     for i in range(2, num):
#         if num % i == 0 :
#             print("{} is a composite number ".format(num))
#             break
#         print("{} is a prime number ".format(num))
            

# check_prime(23)

# def check_prime(num):
#     count = 0 
#     for i in range(2, num ):
#         if num % i == 0 :
#             count = count + 1 
#     if count > 0:
#         print(f"{num} is composite ")
#     else :
#         print(f"{num} is prime ")

# check_prime(17)

# ========================== find factorial number =========================

# def find_fact_num(num):
#     facto = 1 
#     if num == 0 or num == 1 :
#         return 1 
#     else :
#         for i in range(2, num +1):
#             facto = facto * i 
#     return facto

# print(find_fact_num(6))

#==================== fibonacie series upto nth num ==============

 
# def find_fibb_num(nth):
#     a , b = 0, 1
#     fib_series = []
#     for i in range(0,nth ):
#         c = a +b 
#         fib_series.append(c)
#         a =b
#         b = c 
#     return c, fib_series
# print(find_fibb_num(7))

# =========  maximum number in array ==================== 


# def find_max_arr(arr):

#     max = arr[0]
#     for i in range(len(arr)):
#         if arr[i] > max :
#             max = arr[i]
#     return max 
# arr = [45,1,3,55,40,88,51,7,90,34,55]

# print(find_max_arr(arr))

# ------------------- CALCULATE THE COUNT OF ELEMENTS ----------------------

# lists = [1,2,1,1,2,2,3,3,3,4,4,4,4,4,4]
# d = {}
# for i in lists:
#     d[i] = lists.count(i)
# print(d)

l1 = [2,4,5,4,7,3,10,0,9,1]
for i in range(len(l1)):
    for j in range(len(l1)):
        if l1[i] + l1[j] == 10 :
            print("the 2 pairs for the targeted numbers is {} and {}".format(l1[i], l1[j]))




